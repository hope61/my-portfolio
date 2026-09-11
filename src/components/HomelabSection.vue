<script setup>
import LiveStats from './LiveStats.vue'
import { homelab } from '../data.js'
import homelabImage from '../assets/homelab.webp'
</script>

<template>
  <section>
    <h2>Homelab</h2>

    <LiveStats />

    <img :src="homelabImage" alt="The homelab server rack" />

    <dl>
      <div class="row">
        <dt>Hardware</dt>
        <dd>{{ homelab.specs }}</dd>
      </div>
      <div class="row">
        <dt>Hypervisor</dt>
        <dd>{{ homelab.hypervisor }}</dd>
      </div>
      <div class="row">
        <dt>Role</dt>
        <dd>{{ homelab.role }}</dd>
      </div>
      <div class="row">
        <dt>Router</dt>
        <dd>{{ homelab.router }}</dd>
      </div>
      <div class="row">
        <dt>Switch</dt>
        <dd>{{ homelab.switch }}</dd>
      </div>
      <div class="row">
        <dt>Services</dt>
        <dd>{{ homelab.services.join(', ') }}</dd>
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
}

@media (max-width: 480px) {
  .row {
    flex-direction: column;
    gap: 0;
  }

  dt {
    flex: none;
  }
}
</style>
