<script setup>
import { ref } from 'vue'

// Project templates
const projects = ref([
  {
    id: 1,
    title: 'Uchase Downloader',
    description: 'A Browser extension to download videos from Uchase.bg',
    technologies: ['Javascript'],
    github: 'https://github.com/hope61/Uchase-Downloader',
  },
  {
    id: 2,
    title: 'Discord Auto Badge',
    description:
      'A small project which automatically keeps your active developer badge added to your discord account.',
    technologies: ['Python', 'Docker'],
    github: 'https://github.com/hope61/Discord-Auto-Badge',
  },
])
</script>

<template>
  <div class="projects-disclaimer">
    <p>
      Note: Not all of my projects are shown here. Some are still in development, and others contain
      sensitive information like environment keys that I prefer to keep private.
    </p>
  </div>

  <div class="projects-grid">
    <div v-for="project in projects" :key="project.id" class="project-card">
      <div class="project-info">
        <h3 class="project-title">{{ project.title }}</h3>
        <p class="project-description">{{ project.description }}</p>
        <div class="project-technologies">
          <span v-for="(tech, index) in project.technologies" :key="index" class="tech-tag">
            {{ tech }}
          </span>
        </div>
        <div class="project-links">
          <a :href="project.github" class="project-link" target="_blank" rel="noopener noreferrer">
            Code
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.projects-disclaimer {
  max-width: 600px;
  margin: 0 auto 2rem;
  padding: 1rem 1.5rem;
  background-color: var(--background-elevated);
  border-radius: var(--border-radius-md);
  border-left: 4px solid var(--accent-color);
}

.projects-disclaimer p {
  margin: 0;
  color: var(--text-secondary);
  font-size: 0.9rem;
  line-height: 1.6;
  font-style: italic;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}

.project-card {
  background-color: var(--background-secondary);
  border-radius: var(--border-radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.project-info {
  padding: 1.5rem;
}

.project-title {
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
  color: var(--text-primary);
}

.project-description {
  color: var(--text-secondary);
  margin-bottom: 1rem;
  line-height: 1.5;
  font-size: 0.9rem;
}

.project-technologies {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
}

.tech-tag {
  background-color: var(--background-elevated);
  color: var(--text-primary);
  padding: 0.25rem 0.5rem;
  border-radius: var(--border-radius-sm);
  font-size: 0.75rem;
  border: 1px solid var(--border-color);
}

.project-links {
  display: flex;
  gap: 0.75rem;
}

.project-link {
  display: inline-block;
  padding: 0.4rem 0.8rem;
  background-color: var(--accent-color);
  color: var(--text-primary);
  border-radius: var(--border-radius-sm);
  font-weight: 500;
  font-size: 0.8rem;
  transition: all 0.3s ease;
}

.project-link:hover {
  background-color: var(--accent-color-hover);
  transform: translateY(-2px);
}

@media (max-width: 480px) {
  .projects-disclaimer {
    margin: 0 1rem 2rem;
    padding: 0.75rem 1rem;
  }

  .projects-disclaimer p {
    font-size: 0.85rem;
  }

  .project-links {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .project-link {
    width: 100%;
    text-align: center;
  }
}
</style>
