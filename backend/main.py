from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import httpx
import asyncio
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Portfolio Backend API", version="1.0.0")

# Add rate limit error handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Server stats configuration
SERVER_STATS_URL = "http://192.168.0.230:5069/stats"
CACHE_DURATION = 5  # Cache for 30 seconds
stats_cache = {
    "data": None,
    "timestamp": None
}


async def fetch_server_stats():
    """Fetch stats from the server with caching"""
    now = datetime.now()

    # Check if we have cached data that's still valid
    if (stats_cache["data"] is not None and
        stats_cache["timestamp"] is not None and
            (now - stats_cache["timestamp"]).seconds < CACHE_DURATION):
        return stats_cache["data"]

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(SERVER_STATS_URL)
            response.raise_for_status()

            stats_data = response.json()

            # Update cache
            stats_cache["data"] = stats_data
            stats_cache["timestamp"] = now

            logger.info("Successfully fetched server stats")
            return stats_data

    except httpx.TimeoutException:
        logger.error("Timeout while fetching server stats")
        raise HTTPException(status_code=504, detail="Server stats timeout")
    except httpx.RequestError as e:
        logger.error(f"Request error while fetching server stats: {e}")
        raise HTTPException(status_code=503, detail="Server stats unavailable")
    except Exception as e:
        logger.error(f"Unexpected error while fetching server stats: {e}")
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

        # Use the timestamp from the server API if available, otherwise use current time
        server_timestamp = stats.get("timestamp", datetime.now().isoformat())
        
        logger.info(f"Server timestamp: {server_timestamp}")
        logger.info(f"Stats data keys: {list(stats.keys())}")
        
        return {
            "success": True,
            "data": stats,
            "timestamp": server_timestamp,
            "cached": stats_cache["timestamp"] is not None
        }

    except HTTPException:
        # Re-raise HTTP exceptions (they have proper error codes)
        raise
    except Exception as e:
        logger.error(f"Unexpected error in get_server_stats: {e}")
        raise HTTPException(
            status_code=500, detail="Failed to fetch server stats")


@app.get("/api/server/health")
@limiter.limit("30/minute")  # More lenient for health checks
async def check_server_health(request: Request):
    """Check if the server is responding"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(SERVER_STATS_URL)

            return {
                "server_reachable": response.status_code == 200,
                "status_code": response.status_code,
                "response_time_ms": response.elapsed.total_seconds() * 1000,
                "timestamp": datetime.now().isoformat()
            }

    except Exception as e:
        return {
            "server_reachable": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
