<script setup>
import TermWindow from './TermWindow.vue'
import LiveStats from './LiveStats.vue'
import { homelab } from '../data.js'

const rows = [
  ['Hardware', homelab.specs],
  ['Hypervisor', homelab.hypervisor],
  ['Role', homelab.role],
  ['Router', homelab.router],
  ['Switch', homelab.switch],
]
</script>

<template>
  <TermWindow title="homelab" command="htop">
    <LiveStats />

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
  </TermWindow>
</template>

<style scoped>
/* key: value lines, no rules between them: terminal output, not a table. */
.row {
  display: flex;
  gap: 1ch;
}

dt {
  flex: 0 0 11ch;
  color: var(--accent);
}

dt::after {
  content: ':';
  color: var(--fg);
}

dd {
  flex: 1;
  min-width: 0;
}

.services {
  display: flex;
  flex-wrap: wrap;
  gap: 0 var(--space-1);
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
