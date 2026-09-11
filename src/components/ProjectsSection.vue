<script setup>
import { projects } from '../data.js'
</script>

<template>
  <section>
    <h2>Projects</h2>

    <ul>
      <li v-for="project in projects" :key="project.id">
        <h3>
          <a :href="project.url" target="_blank" rel="noopener noreferrer">{{ project.name }}</a>
        </h3>
        <p>{{ project.description }}</p>
        <p class="tech">{{ project.tech.join(' · ') }}</p>
      </li>
    </ul>
  </section>
</template>

<style scoped>
li {
  padding: var(--space-2) 0;
  border-bottom: 1px solid var(--rule);
}

p {
  color: var(--fg-muted);
}

.tech {
  font-family: var(--mono);
  font-size: var(--text-sm);
}
</style>
