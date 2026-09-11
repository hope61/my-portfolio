<script setup>
import { certifications } from '../data.js'
</script>

<template>
  <section>
    <h2>Certifications</h2>

    <ul>
      <li v-for="cert in certifications" :key="cert.id">
        <a :href="cert.url" target="_blank" rel="noopener noreferrer">{{ cert.title }}</a>
        <span class="meta">{{ cert.issuer }} · {{ cert.date }}</span>
      </li>
    </ul>
  </section>
</template>

<style scoped>
li {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: var(--space-2);
  padding: var(--space-1) 0;
  border-bottom: 1px solid var(--rule);
}

.meta {
  flex-shrink: 0;
  font-size: var(--text-sm);
  color: var(--fg-muted);
}

@media (max-width: 600px) {
  li {
    flex-direction: column;
    align-items: stretch;
    gap: 0;
  }
}
</style>
