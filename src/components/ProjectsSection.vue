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
        <p class="description">{{ project.description }}</p>
        <p v-if="project.aiNote" class="ai-note">{{ project.aiNote }}</p>
        <ul class="tech">
          <li v-for="item in project.tech" :key="item" class="chip">{{ item }}</li>
        </ul>
      </li>
    </ul>
  </section>
</template>

<style scoped>
section > ul > li {
  padding: var(--space-3) 0;
  border-bottom: 1px solid var(--rule);
}

section > ul > li:first-child {
  padding-top: 0;
}

.description {
  margin-top: var(--space-1);
  color: var(--fg-muted);
}

.ai-note {
  margin-top: var(--space-1);
  font-size: var(--text-sm);
  color: var(--fg-muted);
  font-style: italic;
}

.tech {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-1);
  margin-top: var(--space-2);
}
</style>
