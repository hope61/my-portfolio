<script setup>
import TermWindow from './TermWindow.vue'
import { certifications } from '../data.js'
</script>

<template>
  <TermWindow title="certs" dir="certs" command="ls">
    <ul>
      <li v-for="cert in certifications" :key="cert.id">
        <a :href="cert.url" target="_blank" rel="noopener noreferrer">{{ cert.title }}</a>
        <span class="meta">{{ cert.issuer }} · {{ cert.date }}</span>
      </li>
    </ul>
  </TermWindow>
</template>

<style scoped>
/* Stacked rather than side by side: the sidebar is too narrow for both on one line. */
li {
  display: flex;
  flex-direction: column;
}

li + li {
  margin-top: var(--space-1);
}

.meta {
  font-size: var(--text-sm);
  color: var(--fg-muted);
}
</style>
