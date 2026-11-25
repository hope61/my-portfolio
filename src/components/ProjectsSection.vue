<script setup>
import TermWindow from './TermWindow.vue'
import { projects } from '../data.js'
</script>

<template>
  <TermWindow title="projects" dir="projects" command="ls -l">
    <ul class="cards">
      <li v-for="project in projects" :key="project.id">
        <h3>
          <span class="dir" aria-hidden="true">drwxr-xr-x</span>
          <a :href="project.url" target="_blank" rel="noopener noreferrer">{{ project.name }}/</a>
        </h3>
        <p class="description">{{ project.description }}</p>
        <ul class="tech">
          <li v-for="item in project.tech" :key="item" class="chip">{{ item }}</li>
        </ul>
      </li>
    </ul>
  </TermWindow>
</template>

<style scoped>
/* Card grid, like GitHub's pinned repositories. */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(18rem, 1fr));
  gap: var(--space-2);
}

.cards > li {
  display: flex;
  flex-direction: column;
  padding: var(--space-1) var(--space-2) var(--space-2);
  border: 1px dashed var(--rule);
}

.cards > li:hover {
  border-style: solid;
  border-color: var(--amber);
}

.dir {
  display: block;
  font-size: var(--text-sm);
  color: var(--fg-muted);
}

.description {
  margin-top: var(--space-1);
  font-size: var(--text-sm);
  color: var(--fg-muted);
}

.tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0 var(--space-1);
  /* Pins the chips to the bottom so cards in a row line up. */
  margin-top: auto;
  padding-top: var(--space-1);
  font-size: var(--text-sm);
}
</style>
