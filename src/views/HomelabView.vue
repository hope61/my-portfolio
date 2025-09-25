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
      status: 'online',
      cpu: 'Loading...',
      ram: 'Loading...',
      disk: 'Loading...',
      uptime: 'Loading...',
      isLive: false,
      portainerServices: ['Speed Test Tracker', 'Vaultwarden', 'Transmission'],
    },
  ],
  network: {
    router: 'TP-Link Archer AX50',
    switches: ['Ubiquiti Flex Mini'],
    accessPoints: [],
    vlans: [],
  },
  services: [
    {
      name: 'Pi-hole',
      description: 'Network-wide ad blocking and DNS filtering',
      status: 'running',
    },
    {
      name: 'AMP Game Server',
      description: 'Game server management and automation',
      status: 'running',
    },
    {
      name: 'Unifi',
      description: 'Network management and monitoring',
      status: 'running',
    },
    {
      name: 'Twingate',
      description: 'Zero trust network access solution',
      status: 'running',
    },
    {
      name: 'Immich',
      description: 'Self-hosted photo and video backup solution',
      status: 'running',
    },
    {
      name: 'Portainer',
      description: 'Docker container management interface',
      status: 'running',
    },
    {
      name: 'CasaOS',
      description: 'Personal cloud operating system for file sharing',
      status: 'running',
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
        server.disk = `${data.disk} (1.65 TB of 2.25 TB)`
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
  <div class="homelab-container">
    <!-- Header Section -->
    <div class="header-section">
      <h1 class="main-title">My Homelab</h1>

      <!-- Server Image -->
      <div class="server-image-container">
        <div class="server-image">
          <img src="/src/assets/homelab.webp" alt="My Homelab Server Setup" />
        </div>
      </div>
    </div>

    <!-- Server Section -->
    <div class="servers-section">
      <h3 class="subsection-title">Server Hardware & Stats</h3>
      <div class="servers-grid">
        <div v-for="server in homelabData.servers" :key="server.id" class="server-card">
          <div class="server-header">
            <h4 class="server-name">{{ server.name }}</h4>
            <div class="status-indicators">
              <span v-if="server.isLive" class="live-indicator"> 🔴 LIVE </span>
              <span v-else-if="connectionError" class="offline-indicator"> ⚪ OFFLINE </span>
            </div>
          </div>
          <div class="server-specs">
            <p><strong>Hardware:</strong> {{ server.specs }}</p>
            <p><strong>Hypervisor:</strong> {{ server.hypervisor }}</p>
            <p><strong>Role:</strong> {{ server.role }}</p>
          </div>

          <div class="server-stats">
            <div class="stats-header">
              <h5>System Stats:</h5>
              <div class="stats-meta">
                <span v-if="isLoading" class="loading-indicator">🔄 Updating...</span>
                <span v-else-if="rateLimitExceeded" class="rate-limit-error"
                  >⚠️ Rate limit exceeded. Please wait...</span
                >
                <span v-else-if="connectionError" class="connection-error"
                  >❌ Connection error</span
                >
                <span v-else-if="lastUpdated" class="last-updated">
                  Updated: {{ lastUpdated.toLocaleString() }}
                </span>
              </div>
            </div>
            <div class="stats-grid">
              <div class="stat-item">
                <span class="stat-label">CPU Usage:</span>
                <span class="stat-value">{{ server.cpu }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">RAM Usage:</span>
                <span class="stat-value">{{ server.ram }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Disk Usage:</span>
                <span class="stat-value">{{ server.disk }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Uptime:</span>
                <span class="stat-value">{{ server.uptime }}</span>
              </div>
            </div>
          </div>

          <div class="server-services">
            <h5>Main Services:</h5>
            <div class="services-list">
              <span v-for="service in server.services" :key="service" class="service-tag">
                {{ service }}
              </span>
            </div>
          </div>

          <div class="portainer-services" v-if="server.portainerServices">
            <h5>Portainer Services:</h5>
            <div class="services-list">
              <span
                v-for="service in server.portainerServices"
                :key="service"
                class="service-tag portainer-tag"
              >
                {{ service }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Network Section -->
    <div class="network-section">
      <h3 class="subsection-title">Network Infrastructure</h3>
      <div class="network-grid">
        <div class="network-item">
          <h4>Router</h4>
          <p>{{ homelabData.network.router }}</p>
        </div>
        <div class="network-item">
          <h4>Switch</h4>
          <p>{{ homelabData.network.switches[0] }}</p>
        </div>
      </div>
    </div>

    <!-- Services Section -->
    <div class="services-section">
      <h3 class="subsection-title">Self-Hosted Services</h3>
      <div class="services-grid">
        <div v-for="service in homelabData.services" :key="service.name" class="service-card">
          <div class="service-header">
            <h4 class="service-name">{{ service.name }}</h4>
          </div>
          <p class="service-description">{{ service.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.homelab-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.header-section {
  text-align: center;
  margin-bottom: 3rem;
}

.main-title {
  font-size: 3rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 2rem;
  text-align: center;
  position: relative;
  padding-top: 2rem;
}

.server-image-container {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.server-image {
  background-color: var(--background-secondary);
  border-radius: var(--border-radius-md);
  padding: 1rem;
  border: 1px solid var(--border-color);
  max-width: 600px;
  width: 100%;
  box-shadow: var(--shadow-md);
  transition: all 0.3s ease;
}

.server-image:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}

.server-image img {
  width: 100%;
  height: auto;
  border-radius: var(--border-radius-sm);
  display: block;
}

.subsection-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 1.5rem;
  border-bottom: 2px solid var(--accent-color);
  padding-bottom: 0.5rem;
}

/* Servers Section */
.servers-section,
.network-section,
.services-section {
  margin-bottom: 3rem;
}

.servers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.server-card {
  background-color: var(--background-secondary);
  border-radius: var(--border-radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.server-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}

.server-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.server-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.status-indicators {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.25rem;
}

.live-indicator {
  font-size: 0.7rem;
  font-weight: 700;
  color: #dc2626;
  animation: pulse 2s infinite;
}

.offline-indicator {
  font-size: 0.7rem;
  font-weight: 600;
  color: var(--text-secondary);
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

.server-specs {
  margin-bottom: 1rem;
}

.server-specs p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.server-stats {
  margin-bottom: 1.5rem;
}

.stats-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.server-stats h5 {
  margin: 0;
  color: var(--text-primary);
  font-size: 1rem;
}

.stats-meta {
  font-size: 0.7rem;
  color: var(--text-secondary);
}

.loading-indicator {
  color: var(--accent-color);
  font-weight: 600;
}

.last-updated {
  font-style: italic;
}

.rate-limit-error {
  font-size: 0.8rem;
  color: #ff9800;
  font-weight: 500;
}

.connection-error {
  font-size: 0.8rem;
  color: #f44336;
  font-weight: 500;
}

.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  background-color: var(--background-elevated);
  padding: 0.5rem;
  border-radius: var(--border-radius-sm);
  border: 1px solid var(--border-color);
}

.stat-label {
  font-size: 0.75rem;
  color: var(--text-secondary);
  font-weight: 500;
  margin-bottom: 0.25rem;
}

.stat-value {
  font-size: 0.8rem;
  color: var(--text-primary);
  font-weight: 600;
  font-family: monospace;
}

.server-services,
.portainer-services {
  margin-bottom: 1.5rem;
}

.server-services h5,
.portainer-services h5 {
  margin: 0 0 0.75rem 0;
  color: var(--text-primary);
  font-size: 1rem;
}

.services-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.service-tag {
  background-color: var(--background-elevated);
  color: var(--text-primary);
  padding: 0.25rem 0.5rem;
  border-radius: var(--border-radius-sm);
  font-size: 0.75rem;
  border: 1px solid var(--border-color);
}

.portainer-tag {
  background-color: var(--accent-color);
  color: white;
  border: 1px solid var(--accent-color);
}

/* Network Section */
.network-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.network-item {
  background-color: var(--background-secondary);
  border-radius: var(--border-radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
}

.network-item h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 1rem 0;
}

.network-item p {
  color: var(--text-secondary);
  margin: 0;
}

.network-item ul {
  margin: 0;
  padding-left: 1.25rem;
}

.network-item li {
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}

/* Services Section */
.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.service-card {
  background-color: var(--background-secondary);
  border-radius: var(--border-radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.service-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}

.service-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.service-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.service-description {
  color: var(--text-secondary);
  margin-bottom: 1rem;
  font-size: 0.9rem;
  line-height: 1.5;
}

/* Responsive Design */
@media (max-width: 768px) {
  .homelab-container {
    padding: 0 0.5rem;
  }

  .main-title {
    font-size: 2.25rem;
  }

  .subsection-title {
    font-size: 1.25rem;
  }

  .servers-grid,
  .network-grid,
  .services-grid {
    grid-template-columns: 1fr;
  }

  .server-header,
  .service-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .server-image {
    padding: 0.75rem;
    max-width: 350px;
  }
}
</style>
