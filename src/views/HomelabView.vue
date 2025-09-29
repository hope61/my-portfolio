<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Homelab equipment and services
const homelabData = ref({
  servers: [
    {
      id: 1,
      name: 'Home Server',
      specs: '6 x Intel Core i5-8500T @ 2.10GHz, 23.30 GiB RAM, 224GB M.2 SSD + 1TB SSD',
      role: 'Self-hosted services and file sharing',
      hypervisor: 'Proxmox VE',
      services: [
        'Pi-hole',
        'AMP Game Server',
        'Unifi',
        'Twingate',
        'Immich',
        'Portainer',
        'CasaOS',
      ],
    },
  ],
  network: {
    router: 'TP-Link Archer AX50',
    switches: ['Ubiquiti Flex Mini'],
  },
  services: [
    {
      name: 'Pi-hole',
      description: 'Network-wide ad blocking and DNS filtering',
    },
    {
      name: 'AMP Game Server',
      description: 'Game server management and automation',
    },
    {
      name: 'Unifi',
      description: 'Network management and monitoring',
    },
    {
      name: 'Twingate',
      description: 'Zero trust network access solution',
    },
    {
      name: 'Immich',
      description: 'Self-hosted photo and video backup solution',
    },
    {
      name: 'Portainer',
      description: 'Docker container management interface',
    },
    {
      name: 'CasaOS',
      description: 'Personal cloud operating system for file sharing',
    },
  ],
})

// Live stats functionality
const backendUrl = 'https://portfolio-api.dicki.org'
const updateInterval = ref(null)
const lastUpdated = ref(null)
const isLoading = ref(false)
const connectionError = ref(false)
const rateLimitExceeded = ref(false)

const fetchLiveStats = async () => {
  if (isLoading.value) return

  isLoading.value = true
  connectionError.value = false

  try {
    console.log('Fetching stats from:', `${backendUrl}/api/server/stats`)
    const response = await fetch(`${backendUrl}/api/server/stats`)

    console.log('Response status:', response.status)

    if (!response.ok) {
      if (response.status === 429) {
        // Rate limit exceeded
        rateLimitExceeded.value = true
        connectionError.value = false
        return
      }
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const result = await response.json()
    console.log('Full API response:', result)

    if (result.success && result.data) {
      // Update server stats with live data
      const server = homelabData.value.servers[0]

      // Map the API response to your display format
      const data = result.data

      // CPU mapping - data.cpu is "1.5%" format
      if (data.cpu !== undefined) {
        server.cpu = `${data.cpu} of 6 CPU(s)`
      }

      // RAM mapping - data.ram is "68.9%" format
      if (data.ram !== undefined) {
        server.ram = `${data.ram} (15.99 GiB of 23.30 GiB)`
      }

      // Disk mapping - data.disk is "73.6%" format
      if (data.disk !== undefined) {
        server.disk = `${data.disk} Used of 2.25 TB`
      }

      // Uptime mapping - data.uptime is "34d 7h" format
      if (data.uptime !== undefined) {
        server.uptime = data.uptime
      }

      server.isLive = true
      // Use the timestamp from the server API response
      console.log('API timestamp:', result.timestamp)
      console.log('Parsed timestamp:', new Date(result.timestamp))
      lastUpdated.value = new Date(result.timestamp)
      connectionError.value = false
      rateLimitExceeded.value = false

      console.log('Updated server stats:', {
        cpu: server.cpu,
        ram: server.ram,
        disk: server.disk,
        uptime: server.uptime,
        isLive: server.isLive,
      })
    }
  } catch (error) {
    console.error('Failed to fetch live stats:', error)
    connectionError.value = true
    homelabData.value.servers[0].isLive = false
  } finally {
    isLoading.value = false
  }
}

const startLiveUpdates = () => {
  // Fetch immediately
  fetchLiveStats()

  // Then fetch every 30 seconds
  updateInterval.value = setInterval(fetchLiveStats, 30000)
}

const stopLiveUpdates = () => {
  if (updateInterval.value) {
    clearInterval(updateInterval.value)
    updateInterval.value = null
  }
}

// Lifecycle hooks
onMounted(() => {
  startLiveUpdates()
})

onUnmounted(() => {
  stopLiveUpdates()
})
</script>

<template>
  <div class="homelab-content">
    <!-- Header -->
    <div class="content-header">
      <h1 class="main-title">Homelab Infrastructure</h1>
    </div>

    <!-- Live Status - Full Width -->
    <div class="live-status-section">
      <div class="status-header">
        <h2 class="status-title">Live Server Status</h2>
        <div class="status-indicator">
          <div
            class="status-dot"
            :class="{ online: homelabData.servers[0].isLive, offline: connectionError }"
          ></div>
          <span class="status-text">
            {{
              homelabData.servers[0].isLive ? 'ONLINE' : connectionError ? 'OFFLINE' : 'CONNECTING'
            }}
          </span>
        </div>
      </div>

      <div class="live-stats-grid">
        <div class="stat-card">
          <div class="stat-icon">
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
              <line x1="8" y1="21" x2="16" y2="21" />
              <line x1="12" y1="17" x2="12" y2="21" />
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-label">CPU</div>
            <div class="stat-value">{{ homelabData.servers[0].cpu }}</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon">
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
              <line x1="8" y1="21" x2="16" y2="21" />
              <line x1="12" y1="17" x2="12" y2="21" />
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-label">Memory</div>
            <div class="stat-value">{{ homelabData.servers[0].ram }}</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon">
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
              <line x1="8" y1="21" x2="16" y2="21" />
              <line x1="12" y1="17" x2="12" y2="21" />
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-label">Storage</div>
            <div class="stat-value">{{ homelabData.servers[0].disk }}</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon">
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <circle cx="12" cy="12" r="10" />
              <polyline points="12,6 12,12 16,14" />
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-label">Uptime</div>
            <div class="stat-value">{{ homelabData.servers[0].uptime }}</div>
          </div>
        </div>
      </div>

      <div class="last-updated">
        <span v-if="isLoading">Updating...</span>
        <span v-else-if="rateLimitExceeded">Rate Limited</span>
        <span v-else-if="connectionError">Connection Error</span>
        <span v-else-if="lastUpdated">Last Updated: {{ lastUpdated.toLocaleTimeString() }}</span>
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="main-grid">
      <!-- Left Column: Image and Services -->
      <div class="left-column">
        <div class="image-section">
          <div class="image-container">
            <img src="/src/assets/homelab.webp" alt="Homelab Server Setup" />
          </div>
        </div>

        <!-- Services -->
        <div class="info-section">
          <h3 class="section-title">Active Services</h3>
          <div class="services-grid">
            <div v-for="service in homelabData.services" :key="service.name" class="service-item">
              <div class="service-name">{{ service.name }}</div>
              <div class="service-description">{{ service.description }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Information -->
      <div class="right-column">
        <!-- Server Information -->
        <div class="info-section">
          <h3 class="section-title">Server Specifications</h3>
          <div class="info-card">
            <div class="info-item">
              <span class="label">Hardware:</span>
              <span class="value">{{ homelabData.servers[0].specs }}</span>
            </div>
            <div class="info-item">
              <span class="label">Hypervisor:</span>
              <span class="value">{{ homelabData.servers[0].hypervisor }}</span>
            </div>
            <div class="info-item">
              <span class="label">Role:</span>
              <span class="value">{{ homelabData.servers[0].role }}</span>
            </div>
          </div>
        </div>

        <!-- Network Infrastructure -->
        <div class="info-section">
          <h3 class="section-title">Network Infrastructure</h3>
          <div class="info-card">
            <div class="info-item">
              <span class="label">Router:</span>
              <span class="value">{{ homelabData.network.router }}</span>
            </div>
            <div class="info-item">
              <span class="label">Switch:</span>
              <span class="value">{{ homelabData.network.switches[0] }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.homelab-content {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.content-header {
  margin-bottom: 3rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border);
  text-align: center;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 300;
  color: var(--text-primary);
  letter-spacing: 1px;
}

/* Main Grid Layout */
.main-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: start;
}

.left-column {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.right-column {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.image-section {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-container {
  width: 100%;
  max-width: 300px;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: var(--shadow);
}

.image-container img {
  width: 100%;
  height: auto;
  display: block;
}

/* Live Status Section */
.live-status-section {
  background: var(--bg-secondary);
  border-radius: 15px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 16px rgba(0, 102, 204, 0.1);
}

.status-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.status-title {
  font-size: 1.3rem;
  font-weight: 300;
  color: var(--text-primary);
  letter-spacing: 1px;
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--text-muted);
  animation: pulse 2s infinite;
}

.status-dot.online {
  background: #00cc66;
}

.status-dot.offline {
  background: #ff4444;
}

.status-text {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  letter-spacing: 1px;
}

@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.live-stats-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin-bottom: 1rem;
}

.stat-card {
  background: var(--bg-primary);
  border-radius: 10px;
  border: 1px solid var(--border);
  padding: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.stat-icon {
  color: var(--accent);
  flex-shrink: 0;
}

.stat-content {
  flex: 1;
}

.stat-label {
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--text-secondary);
  margin-bottom: 0.25rem;
}

.stat-value {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-primary);
  font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
}

.last-updated {
  text-align: center;
  font-size: 0.75rem;
  color: var(--text-muted);
  font-style: italic;
}

.section-title {
  font-size: 1.3rem;
  font-weight: 300;
  color: var(--text-primary);
  margin-bottom: 1rem;
  letter-spacing: 1px;
}

.section-title::after {
  display: none;
}

.info-card {
  background: var(--bg-secondary);
  padding: 1.5rem;
  border-radius: 15px;
  border: 1px solid var(--border);
}

.info-item {
  display: flex;
  margin-bottom: 1rem;
  gap: 1rem;
}

.info-item:last-child {
  margin-bottom: 0;
}

.label {
  font-weight: 500;
  color: var(--accent);
  min-width: 100px;
  flex-shrink: 0;
}

.value {
  color: var(--text-secondary);
  line-height: 1.5;
  word-break: break-word;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}

.service-item {
  background: var(--bg-secondary);
  padding: 0.75rem;
  border-radius: 10px;
  border: 1px solid var(--border);
}

.service-name {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.service-description {
  color: var(--text-secondary);
  line-height: 1.3;
  font-size: 0.8rem;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .main-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .services-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .homelab-content {
    padding: 1rem;
  }

  .main-title {
    font-size: 2rem;
  }

  .live-status-section {
    padding: 1.5rem;
  }

  .status-header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .status-title {
    font-size: 1.4rem;
  }

  .live-stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .stat-card {
    padding: 1rem;
  }

  .info-card {
    padding: 1rem;
  }

  .info-item {
    flex-direction: column;
    gap: 0.25rem;
  }

  .label {
    min-width: auto;
  }

  .image-container {
    max-width: 250px;
  }
}

@media (max-width: 480px) {
  .main-title {
    font-size: 1.8rem;
  }

  .status-title {
    font-size: 1.2rem;
  }

  .service-item {
    padding: 0.5rem;
  }

  .image-container {
    max-width: 200px;
  }
}
</style>
