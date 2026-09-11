<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Production: same-origin, nginx proxies /api/ to the backend container (see nginx.conf).
// Dev: point at a reachable backend via VITE_API_BASE_URL in .env.
const backendUrl = import.meta.env.DEV ? (import.meta.env.VITE_API_BASE_URL ?? '') : ''

const stats = ref({ cpu: '—', ram: '—', disk: '—', uptime: '—' })
const isLive = ref(false)
const updateInterval = ref(null)
const lastUpdated = ref(null)
const isLoading = ref(false)
const connectionError = ref(false)
const rateLimitExceeded = ref(false)

const applyStats = (data, timestamp) => {
  if (data.cpu !== undefined) stats.value.cpu = data.cpu
  if (data.ram !== undefined) stats.value.ram = data.ram
  if (data.disk !== undefined) stats.value.disk = data.disk
  if (data.uptime !== undefined) stats.value.uptime = data.uptime

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
    <div class="status">
      <span
        class="dot"
        :class="{ online: isLive, offline: connectionError }"
        aria-hidden="true"
      ></span>
      <span>{{ isLive ? 'Online' : connectionError ? 'Offline' : 'Connecting' }}</span>
    </div>

    <dl>
      <div class="row">
        <dt>CPU</dt>
        <dd>{{ stats.cpu }}</dd>
      </div>
      <div class="row">
        <dt>Memory</dt>
        <dd>{{ stats.ram }}</dd>
      </div>
      <div class="row">
        <dt>Storage</dt>
        <dd>{{ stats.disk }}</dd>
      </div>
      <div class="row">
        <dt>Uptime</dt>
        <dd>{{ stats.uptime }}</dd>
      </div>
    </dl>

    <p class="meta">
      <span v-if="isLoading">Updating…</span>
      <span v-else-if="rateLimitExceeded">Rate limited</span>
      <span v-else-if="connectionError">Connection error</span>
      <span v-else-if="lastUpdated">Updated {{ lastUpdated.toLocaleTimeString() }}</span>
    </p>
  </div>
</template>

<style scoped>
.live {
  margin-bottom: var(--space-4);
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
  background: var(--fg-muted);
  animation: pulse 2s infinite;
}

.dot.online {
  background: var(--ok);
}

.dot.offline {
  background: var(--down);
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

.row {
  display: flex;
  justify-content: space-between;
  gap: var(--space-2);
  padding: var(--space-1) 0;
  border-bottom: 1px solid var(--rule);
}

dt {
  color: var(--fg-muted);
}

dd {
  font-family: var(--mono);
  text-align: right;
}

.meta {
  margin-top: var(--space-1);
  font-size: var(--text-sm);
  color: var(--fg-muted);
}
</style>
