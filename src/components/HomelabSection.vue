<script setup>
import LiveStats from './LiveStats.vue'
import { homelab } from '../data.js'
import homelabImage from '../assets/homelab.webp'

const rows = [
  ['Hardware', homelab.specs],
  ['Hypervisor', homelab.hypervisor],
  ['Role', homelab.role],
  ['Router', homelab.router],
  ['Switch', homelab.switch],
]
</script>

<template>
  <section>
    <h2>Homelab</h2>

    <LiveStats />

    <img
      :src="homelabImage"
      width="1600"
      height="1200"
      loading="lazy"
      decoding="async"
      alt="The homelab server rack"
    />

    <dl>
      <div v-for="[label, value] in rows" :key="label" class="row">
        <dt>{{ label }}</dt>
        <dd>{{ value }}</dd>
      </div>
      <div class="row">
        <dt>Services</dt>
        <dd>
          <ul class="services">
            <li v-for="service in homelab.services" :key="service" class="chip">{{ service }}</li>
          </ul>
        </dd>
      </div>
    </dl>
  </section>
</template>

<style scoped>
img {
  margin-bottom: var(--space-4);
}

.row {
  display: flex;
  gap: var(--space-2);
  padding: var(--space-1) 0;
  border-bottom: 1px solid var(--rule);
}

dt {
  flex: 0 0 7rem;
  color: var(--fg-muted);
}

dd {
  flex: 1;
  min-width: 0;
}

.services {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-1);
}

@media (max-width: 600px) {
  .row {
    flex-direction: column;
    gap: 0;
  }

  dt {
    flex: none;
  }
}
</style>
