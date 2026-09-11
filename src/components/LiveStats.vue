<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// Production: same-origin, nginx proxies /api/ to the backend container (see nginx.conf).
// Dev: point at a reachable backend via VITE_API_BASE_URL in .env.
const backendUrl = import.meta.env.DEV ? (import.meta.env.VITE_API_BASE_URL ?? '') : ''

const stats = ref({ cpu: '—', ram: '—', disk: '—', uptime: '—', vms: '—', lxc: '—' })
const isLive = ref(false)
const updateInterval = ref(null)
const lastUpdated = ref(null)
const isLoading = ref(false)
const connectionError = ref(false)
const rateLimitExceeded = ref(false)

// One source of truth for the indicator. Rate limiting is its own state:
// previously it left the dot reading "Connecting" forever while the line
// below it said "Rate limited".
const statusLabel = computed(() => {
  if (connectionError.value) return 'Offline'
  if (rateLimitExceeded.value) return 'Rate limited'
  if (isLive.value) return 'Online'
  return 'Connecting'
})

const applyStats = (data, timestamp) => {
  if (data.cpu !== undefined) stats.value.cpu = data.cpu
  if (data.ram !== undefined) stats.value.ram = data.ram
  if (data.disk !== undefined) stats.value.disk = data.disk
  if (data.uptime !== undefined) stats.value.uptime = data.uptime
  if (data.vms !== undefined) stats.value.vms = data.vms
  if (data.lxc !== undefined) stats.value.lxc = data.lxc

  isLive.value = true
  lastUpdated.value = new Date(timestamp)
}

const fetchLiveStats = async () => {
  if (isLoading.value) return

  isLoading.value = true

  // Abort slow/hung requests (some mobile browsers never surface network errors).
  const controller = new AbortController()
  const timeout = setTimeout(() => controller.abort(), 10000)

  try {
    const response = await fetch(`${backendUrl}/api/server/stats`, {
      signal: controller.signal,
    })

    if (response.status === 429) {
      rateLimitExceeded.value = true
      connectionError.value = false
      return
    }
    if (!response.ok) throw new Error(`HTTP ${response.status}`)

    const result = await response.json()
    if (!result.success || !result.data) throw new Error('Malformed API response')

    applyStats(result.data, result.timestamp)
    connectionError.value = false
    rateLimitExceeded.value = false
  } catch (error) {
    console.error('Failed to fetch live stats:', error)
    connectionError.value = true
    isLive.value = false
  } finally {
    clearTimeout(timeout)
    isLoading.value = false
  }
}

onMounted(() => {
  fetchLiveStats()
  updateInterval.value = setInterval(fetchLiveStats, 30000)
})

onUnmounted(() => {
  if (updateInterval.value) {
    clearInterval(updateInterval.value)
    updateInterval.value = null
  }
})
</script>

<template>
  <div class="live">
    <div class="status" aria-live="polite">
      <span
        class="dot"
        :class="{ online: statusLabel === 'Online', offline: connectionError }"
        aria-hidden="true"
      ></span>
      <span>{{ statusLabel }}</span>
    </div>

    <dl>
      <div class="stat">
        <dt>CPU</dt>
        <dd>{{ stats.cpu }}</dd>
      </div>
      <div class="stat">
        <dt>Memory</dt>
        <dd>{{ stats.ram }}</dd>
      </div>
      <div class="stat">
        <dt>Storage</dt>
        <dd>{{ stats.disk }}</dd>
      </div>
      <div class="stat">
        <dt>Uptime</dt>
        <dd>{{ stats.uptime }}</dd>
      </div>
      <div class="stat">
        <dt>VMs</dt>
        <dd>{{ stats.vms }}</dd>
      </div>
      <div class="stat">
        <dt>LXC</dt>
        <dd>{{ stats.lxc }}</dd>
      </div>
    </dl>

    <p class="meta">
      <span v-if="isLoading">Updating…</span>
      <span v-else-if="lastUpdated">Updated {{ lastUpdated.toLocaleTimeString() }}</span>
    </p>
  </div>
</template>

<style scoped>
.live {
  margin-bottom: var(--space-4);
  padding: var(--space-2);
  border: 1px solid var(--rule);
}

.status {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  font-size: var(--text-sm);
  color: var(--fg-muted);
  margin-bottom: var(--space-2);
}

.dot {
  width: 8px;
  height: 8px;
  flex: none;
  background: var(--fg-muted);
  animation: pulse 2s infinite;
}

.dot.online {
  background: var(--ok);
}

.dot.offline {
  background: var(--down);
  animation: none;
}

@keyframes pulse {
  50% {
    opacity: 0.4;
  }
}

@media (prefers-reduced-motion: reduce) {
  .dot {
    animation: none;
  }
}

dl {
  display: grid;
  /* auto-fit rather than a fixed 2-up: values like "512.0 GiB / 1.1 TiB" need
     ~13rem, so the grid drops to one column before it would wrap them. */
  grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr));
  gap: var(--space-2);
}

dt {
  font-size: var(--text-sm);
  color: var(--fg-muted);
}

dd {
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  overflow-wrap: anywhere;
}

.meta {
  /* Reserved so the first successful fetch does not shift the page. */
  min-height: calc(var(--text-sm) * 1.6);
  margin-top: var(--space-2);
  font-size: var(--text-sm);
  color: var(--fg-muted);
}

@media (max-width: 480px) {
  /* One column, label and value on a shared baseline: the two-up grid is too
     narrow for the longest values ("512.0 GiB / 1.1 TiB") and wraps them. */
  dl {
    grid-template-columns: minmax(0, 1fr);
    gap: 0;
  }

  .stat {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: var(--space-2);
    padding: var(--space-1) 0;
    border-bottom: 1px solid var(--rule);
  }

  .stat:last-child {
    border-bottom: 0;
    padding-bottom: 0;
  }

  dd {
    text-align: right;
  }
}
</style>
