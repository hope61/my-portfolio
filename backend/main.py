from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import httpx
from datetime import datetime
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Rate limiter setup
def client_ip(request: Request) -> str:
    """Real client IP, honoring X-Forwarded-For set by the nginx proxy."""
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    return get_remote_address(request)


limiter = Limiter(key_func=client_ip)
app = FastAPI(title="Portfolio Backend API", version="1.0.0")

# Add rate limit error handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Add CORS middleware
cors_origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:4173",
    "https://dicki.org",
    "https://www.dicki.org",
    "https://portfolio.dicki.org",
    "https://www.portfolio.dicki.org",
]

# Optional comma-separated override for ad-hoc origins (useful for phone/LAN testing)
extra_origins = [
    origin.strip()
    for origin in os.getenv("CORS_EXTRA_ORIGINS", "").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins + extra_origins,
    # Support LAN development origins, e.g. http://192.168.x.x:5173 from a phone.
    allow_origin_regex=r"^http://(localhost|127\.0\.0\.1|192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3})(:\d+)?$",
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# --- Proxmox VE configuration -------------------------------------------
# Read-only API token. Create it on the PVE host with:
#   pveum user add portfolio@pve
#   pveum user token add portfolio@pve readonly --privsep 1
#   pveum acl modify /nodes/<node> --users portfolio@pve --roles PVEAuditor
#   pveum acl modify /nodes/<node> --tokens 'portfolio@pve!readonly' --roles PVEAuditor
# Both grants are required: with privsep the token's effective rights are the
# INTERSECTION of the user's and the token's, so granting only one yields none.
# Single-quote the token id - the '!' triggers shell history expansion.
PVE_HOST = os.getenv("PVE_HOST", "").rstrip("/")
PVE_NODE = os.getenv("PVE_NODE", "")
PVE_TOKEN_ID = os.getenv("PVE_TOKEN_ID", "")
PVE_TOKEN_SECRET = os.getenv("PVE_TOKEN_SECRET", "")

# TLS: prefer pinning the node's CA (/etc/pve/pve-root-ca.pem). Setting
# PVE_VERIFY_SSL=false disables verification entirely and is unsafe.
PVE_CA_PATH = os.getenv("PVE_CA_PATH", "")
PVE_VERIFY_SSL = os.getenv("PVE_VERIFY_SSL", "true").lower() != "false"

if not PVE_VERIFY_SSL and not PVE_CA_PATH:
    # Stated once at startup, not per request: this is a deliberate setting,
    # and repeating it every fetch just buries the logs that matter.
    logger.warning(
        "PVE_VERIFY_SSL=false - TLS certificate verification is disabled for "
        "%s. Acceptable on a trusted LAN; set PVE_CA_PATH to pin the node's "
        "pve-root-ca.pem if this ever traverses an untrusted network.",
        PVE_HOST or "<unset>",
    )

# Which storage IDs to total for the "disk" figure. Empty = the node's root
# filesystem. Listing them explicitly avoids double-counting stores that sit
# on the same physical disk (e.g. local and local-lvm).
PVE_STORAGE = [s.strip() for s in os.getenv("PVE_STORAGE", "").split(",") if s.strip()]

CACHE_DURATION = int(os.getenv("STATS_CACHE_SECONDS", "30"))  # seconds
stats_cache = {"data": None, "timestamp": None}


def _tls_verify():
    """httpx verify= value: a pinned CA path, or a plain on/off flag."""
    return PVE_CA_PATH or PVE_VERIFY_SSL


def _fmt_bytes(n: float) -> str:
    """Bytes to a compact binary-unit string, e.g. '12.8 GiB'."""
    for unit in ("B", "KiB", "MiB", "GiB"):
        if abs(n) < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.2f} TiB"


def _fmt_pair(used: float, total: float) -> str:
    """'12.8 GiB / 23.3 GiB', or an em dash when the total is unknown."""
    if not total:
        return "—"
    return f"{_fmt_bytes(used)} / {_fmt_bytes(total)}"


def _fmt_uptime(seconds: int) -> str:
    """Seconds to '3d 18h' / '18h 4m' / '4m'."""
    seconds = int(seconds)
    days, rem = divmod(seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes = rem // 60
    if days:
        return f"{days}d {hours}h"
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


async def _pve_get(client: httpx.AsyncClient, path: str):
    """GET a Proxmox API path and return its `data` payload."""
    response = await client.get(f"{PVE_HOST}/api2/json{path}")
    if response.status_code in (401, 403):
        logger.error(
            "Proxmox rejected the API token (%s) for %s - check the token "
            "secret and its PVEAuditor ACL.", response.status_code, path
        )
        raise HTTPException(status_code=502, detail="Upstream auth failed")
    response.raise_for_status()
    return response.json().get("data") or {}


async def _fetch_storage_totals(client: httpx.AsyncClient):
    """Sum used/total across the storage IDs named in PVE_STORAGE."""
    entries = await _pve_get(client, f"/nodes/{PVE_NODE}/storage")
    wanted = [e for e in entries if e.get("storage") in PVE_STORAGE]
    missing = set(PVE_STORAGE) - {e.get("storage") for e in wanted}
    if missing:
        logger.warning("PVE_STORAGE names not found on node: %s", ", ".join(sorted(missing)))
    used = sum(e.get("used", 0) for e in wanted)
    total = sum(e.get("total", 0) for e in wanted)
    return used, total


async def _fetch_guest_counts(client: httpx.AsyncClient):
    """Count running and total QEMU VMs and LXC containers on the node.

    Only guests Proxmox itself manages are visible here. Docker containers
    running inside a VM are not, so these are deliberately labelled VMs and
    LXC rather than a single "containers" figure.
    """
    counts = {}
    for kind, key in (("qemu", "vms"), ("lxc", "lxc")):
        guests = await _pve_get(client, f"/nodes/{PVE_NODE}/{kind}")
        if not isinstance(guests, list):
            guests = []
        # Templates are not running guests and would inflate the total.
        guests = [g for g in guests if not g.get("template")]
        running = sum(1 for g in guests if g.get("status") == "running")
        counts[key] = f"{running} / {len(guests)}"
    return counts


async def fetch_server_stats():
    """Fetch node stats from the Proxmox API, with caching."""
    if not (PVE_HOST and PVE_NODE and PVE_TOKEN_ID and PVE_TOKEN_SECRET):
        logger.error(
            "Proxmox is not configured - set PVE_HOST, PVE_NODE, "
            "PVE_TOKEN_ID and PVE_TOKEN_SECRET."
        )
        raise HTTPException(status_code=503, detail="Server stats unavailable")

    now = datetime.now()

    # Check if we have cached data that's still valid
    if (stats_cache["data"] is not None and
        stats_cache["timestamp"] is not None and
            (now - stats_cache["timestamp"]).total_seconds() < CACHE_DURATION):
        return stats_cache["data"]

    headers = {"Authorization": f"PVEAPIToken={PVE_TOKEN_ID}={PVE_TOKEN_SECRET}"}

    try:
        async with httpx.AsyncClient(
            timeout=10.0, verify=_tls_verify(), headers=headers
        ) as client:
            status = await _pve_get(client, f"/nodes/{PVE_NODE}/status")

            memory = status.get("memory", {})
            rootfs = status.get("rootfs", {})

            if PVE_STORAGE:
                disk_used, disk_total = await _fetch_storage_totals(client)
            else:
                disk_used, disk_total = rootfs.get("used", 0), rootfs.get("total", 0)

            guests = await _fetch_guest_counts(client)

            # Whitelist the fields we publish. Never pass the raw payload
            # through: it carries pveversion and kversion, which advertise
            # exactly which CVEs apply to this host.
            stats_data = {
                "cpu": f"{status.get('cpu', 0) * 100:.1f}%",
                "ram": _fmt_pair(memory.get("used", 0), memory.get("total", 0)),
                "disk": _fmt_pair(disk_used, disk_total),
                "uptime": _fmt_uptime(status.get("uptime", 0)),
                "vms": guests["vms"],
                "lxc": guests["lxc"],
            }

            stats_cache["data"] = stats_data
            stats_cache["timestamp"] = now
            return stats_data

    except HTTPException:
        raise
    except httpx.TimeoutException:
        logger.error("Timeout while fetching Proxmox stats")
        raise HTTPException(status_code=504, detail="Server stats timeout")
    except httpx.RequestError as e:
        logger.error(f"Request error while fetching Proxmox stats: {e}")
        raise HTTPException(status_code=503, detail="Server stats unavailable")
    except Exception as e:
        logger.error(f"Unexpected error while fetching Proxmox stats: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Portfolio Backend API",
        "version": "1.0.0",
        "endpoints": {
            "server_stats": "/api/server/stats",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "portfolio-backend"
    }


@app.get("/api/server/stats")
@limiter.limit("10/minute")  # Allow 10 requests per minute per IP
async def get_server_stats(request: Request):
    """Get server statistics with rate limiting"""
    try:
        stats = await fetch_server_stats()

        return {
            "success": True,
            "data": stats,
            "timestamp": datetime.now().isoformat(),
        }

    except HTTPException:
        # Re-raise HTTP exceptions (they have proper error codes)
        raise
    except Exception as e:
        logger.error(f"Unexpected error in get_server_stats: {e}")
        raise HTTPException(
            status_code=500, detail="Failed to fetch server stats")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
