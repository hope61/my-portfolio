<script setup>
import HomelabSection from './components/HomelabSection.vue'
import ProjectsSection from './components/ProjectsSection.vue'
import CertsSection from './components/CertsSection.vue'
import { profile } from './data.js'
</script>

<template>
  <main>
    <header>
      <h1>{{ profile.name }}</h1>
      <p>{{ profile.bio }}</p>
    </header>

    <HomelabSection />
    <ProjectsSection />
    <CertsSection />

    <footer>
      <a :href="`mailto:${profile.email}`">{{ profile.email }}</a>
      <a :href="profile.github" target="_blank" rel="noopener noreferrer">GitHub</a>
    </footer>
  </main>
</template>

<style scoped>
main {
  max-width: 40rem;
  margin: 0 auto;
  padding: var(--space-8) var(--space-3);
}

header {
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--rule);
}

header p {
  color: var(--fg-muted);
}

main > :deep(section) {
  margin-top: var(--space-8);
}

main > :deep(section) h2 {
  margin-bottom: var(--space-3);
}

footer {
  display: flex;
  gap: var(--space-3);
  margin-top: var(--space-8);
  padding-top: var(--space-3);
  border-top: 1px solid var(--rule);
  font-size: var(--text-sm);
}

@media (max-width: 480px) {
  main {
    padding: var(--space-4) var(--space-2);
  }
}
</style>
