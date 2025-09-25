<template>
  <div>
    <section id="home" class="section home-section">
      <HomeView />
    </section>

    <section id="timeline" class="section timeline-section">
      <div class="container">
        <h2 class="section-title">My Journey</h2>
        <TimelineView />
      </div>
    </section>

    <section id="projects" class="section projects-section">
      <div class="container">
        <h2 class="section-title">My Projects</h2>
        <ProjectsView />
      </div>
    </section>

    <section id="certifications" class="section certifications-section">
      <div class="container">
        <h2 class="section-title">My Certifications</h2>
        <CertificationsView />
      </div>
    </section>

    <section id="contact" class="section contact-section">
      <div class="container">
        <h2 class="section-title">Contact Me</h2>
        <ContactView />
      </div>
    </section>
  </div>
</template>

<script setup>
import HomeView from './HomeView.vue'
import TimelineView from './TimelineView.vue'
import ProjectsView from './ProjectsView.vue'
import CertificationsView from './CertificationsView.vue'
import ContactView from './ContactView.vue'
</script>

<style scoped>
.section {
  padding-top: 3rem;
  padding-bottom: 3rem;
  scroll-margin-top: 90px;
}

.section:not(:last-child) {
  border-bottom: 1px solid var(--border-color);
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 2rem;
  text-align: center;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

@media (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }

  .section-title {
    font-size: 1.75rem;
  }
}
</style>
