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

// htop-style meter fill, 0..1, from '9.4%' or '19.2 GiB / 31.2 GiB' (the backend's
// _fmt_pair). Anything unparseable, like the '—' placeholder, draws an empty meter.
const UNITS = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
const bytes = (text) => {
  const [n, unit] = text.trim().split(' ')
  return n * 1024 ** UNITS.indexOf(unit)
}
const fraction = (value) => {
  const [used, total] = value.split(' / ')
  const f = value.endsWith('%') ? parseFloat(value) / 100 : total ? bytes(used) / bytes(total) : 0
  return Math.min(Math.max(f, 0), 1) || 0
}

const meters = computed(() => [
  ['CPU', stats.value.cpu],
  ['Mem', stats.value.ram],
  ['Disk', stats.value.disk],
])

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
      <span class="updated">
        <template v-if="isLoading">updating…</template>
        <template v-else-if="lastUpdated">updated {{ lastUpdated.toLocaleTimeString() }}</template>
      </span>
    </div>

    <dl class="meters">
      <div v-for="[label, value] in meters" :key="label" class="meter">
        <dt>{{ label }}</dt>
        <dd class="bar">
          <!-- A long run of pipes clipped to the fill width, so it scales with the window. -->
          <span class="fill" :style="{ width: `${fraction(value) * 100}%` }" aria-hidden="true">{{
            '|'.repeat(200)
          }}</span>
          <span class="value">{{ value }}</span>
        </dd>
      </div>
    </dl>

    <dl class="counts">
      <div>
        <dt>Uptime</dt>
        <dd>{{ stats.uptime }}</dd>
      </div>
      <div>
        <dt>VMs</dt>
        <dd>{{ stats.vms }}</dd>
      </div>
      <div>
        <dt>LXC</dt>
        <dd>{{ stats.lxc }}</dd>
      </div>
    </dl>
  </div>
</template>

<style scoped>
.live {
  margin-bottom: var(--space-2);
}

.status {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  margin-bottom: var(--space-1);
}

.updated {
  margin-left: auto;
  /* Reserved so the first successful fetch does not shift the line. */
  min-width: 1ch;
  color: var(--fg-muted);
}

.dot {
  width: 0.6em;
  height: 0.6em;
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

.meter {
  display: grid;
  grid-template-columns: 5ch minmax(0, 1fr);
  align-items: baseline;
  gap: 1ch;
}

.meter dt {
  color: var(--accent);
}

.bar {
  display: flex;
  overflow: hidden;
  white-space: nowrap;
  color: var(--ok);
}

.bar::before {
  content: '[';
  color: var(--fg);
}

.bar::after {
  content: ']';
  color: var(--fg);
}

/* Shrinks before the value does, so a full meter never pushes the value out. */
.fill {
  flex: 0 1 auto;
  min-width: 0;
  overflow: hidden;
}

/* Inside the brackets at the right end, as htop prints it. */
.value {
  flex: none;
  margin-left: auto;
  padding-left: 1ch;
  color: var(--fg);
  font-variant-numeric: tabular-nums;
}

.counts {
  display: flex;
  flex-wrap: wrap;
  gap: 0 var(--space-3);
  margin-top: var(--space-1);
}

.counts div {
  display: flex;
  gap: 0.5ch;
}

.counts dt {
  color: var(--accent);
}

.counts dt::after {
  content: ':';
  color: var(--fg);
}
</style>
