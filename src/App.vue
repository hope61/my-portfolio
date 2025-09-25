<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import HomeView from './views/HomeView.vue'
import TimelineView from './views/TimelineView.vue'
import ProjectsView from './views/ProjectsView.vue'
import ContactView from './views/ContactView.vue'

// Navigation
const activeSection = ref('home')
const showBackToTop = ref(false)

const scrollToSection = (sectionId) => {
  activeSection.value = sectionId
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  })
  activeSection.value = 'home'
}

const checkScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

onMounted(() => {
  window.addEventListener('scroll', checkScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', checkScroll)
})

// GitHub profile link
const githubUrl = 'https://github.com/hope61'
</script>

<template>
  <div class="bg-pattern"></div>

  <div class="app-container">
    <div class="island-container">
      <header>
        <div class="logo">
          <span class="logo-text">Portfolio</span>
        </div>
        <nav>
          <a
            href="#home"
            @click.prevent="scrollToSection('home')"
            class="nav-link"
            :class="{ active: activeSection === 'home' }"
          >
            Home
          </a>
          <a
            href="#about"
            @click.prevent="scrollToSection('about')"
            class="nav-link"
            :class="{ active: activeSection === 'about' }"
          >
            About
          </a>
          <a
            href="#timeline"
            @click.prevent="scrollToSection('timeline')"
            class="nav-link"
            :class="{ active: activeSection === 'timeline' }"
          >
            Timeline
          </a>
          <a
            href="#projects"
            @click.prevent="scrollToSection('projects')"
            class="nav-link"
            :class="{ active: activeSection === 'projects' }"
          >
            Projects
          </a>
          <a
            href="#contact"
            @click.prevent="scrollToSection('contact')"
            class="nav-link"
            :class="{ active: activeSection === 'contact' }"
          >
            Contact
          </a>
          <a
            :href="githubUrl"
            target="_blank"
            rel="noopener noreferrer"
            class="nav-link github-link"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path
                d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"
              ></path>
            </svg>
            GitHub
          </a>
        </nav>
      </header>

      <main>
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

        <section id="contact" class="section contact-section">
          <div class="container">
            <h2 class="section-title">Contact Me</h2>
            <ContactView />
          </div>
        </section>
      </main>

      <footer>
        <div class="footer-links"></div>
      </footer>
    </div>

    <button
      v-show="showBackToTop"
      @click="scrollToTop"
      class="back-to-top"
      aria-label="Back to top"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <polyline points="18 15 12 9 6 15"></polyline>
      </svg>
    </button>
  </div>
</template>

<style scoped>
/* Hide scrollbar for Chrome, Safari and Opera */
::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
html,
body {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  background-color: var(--background-secondary);
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid var(--border-color);
}

.logo {
  display: flex;
  align-items: center;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: 1px;
}

nav {
  display: flex;
  gap: 1.5rem;
}

.nav-link {
  color: var(--text-primary);
  font-weight: 500;
  transition: all 0.2s ease;
  position: relative;
  padding: 0.5rem 0;
  font-size: 0.95rem;
}

.nav-link:hover {
  color: var(--accent-color);
}

.nav-link.active {
  color: var(--accent-color);
}

.github-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

main {
  flex: 1;
}

.section {
  padding-top: 3rem;
  padding-bottom: 3rem;
  scroll-margin-top: 90px;
}

.section:not(:last-child) {
  border-bottom: 1px solid var(--border-color);
}

footer {
  padding: 1.5rem;
  background-color: var(--background-secondary);
  text-align: center;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-links {
  display: flex;
  gap: 1rem;
}

.footer-link {
  color: var(--text-primary);
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: var(--accent-color);
}

/* Back to Top Button */
.back-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background-color: var(--accent-color);
  color: white;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: var(--shadow-md);
  transition: all 0.3s ease;
  z-index: 100;
}

.back-to-top:hover {
  background-color: var(--accent-color-hover);
  transform: translateY(-3px);
}

@media (max-width: 768px) {
  header {
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
  }

  nav {
    width: 100%;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .nav-link {
    font-size: 0.85rem;
  }

  footer {
    flex-direction: column;
    gap: 1rem;
  }

  .back-to-top {
    bottom: 1.5rem;
    right: 1.5rem;
    width: 40px;
    height: 40px;
  }
}
</style>
