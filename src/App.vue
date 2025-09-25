<script setup>
import { useRouter } from 'vue-router'

// GitHub profile link
const githubUrl = 'https://github.com/hope61'
const router = useRouter()

// Scroll navigation function
const scrollToSection = (sectionId) => {
  // Check if we're on the main page
  if (router.currentRoute.value.path === '/') {
    const element = document.getElementById(sectionId)
    if (element) {
      element.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
      })
    }
  } else {
    // If not on main page, navigate to main page first
    router.push('/').then(() => {
      setTimeout(() => {
        const element = document.getElementById(sectionId)
        if (element) {
          element.scrollIntoView({
            behavior: 'smooth',
            block: 'start',
          })
        }
      }, 100)
    })
  }
}
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
          <router-link to="/" class="nav-link">Home</router-link>
          <a href="#timeline" @click.prevent="scrollToSection('timeline')" class="nav-link"
            >About</a
          >
          <a href="#timeline" @click.prevent="scrollToSection('timeline')" class="nav-link"
            >Timeline</a
          >
          <a href="#projects" @click.prevent="scrollToSection('projects')" class="nav-link"
            >Projects</a
          >
          <a
            href="#certifications"
            @click.prevent="scrollToSection('certifications')"
            class="nav-link"
            >Certs</a
          >
          <router-link to="/homelab" class="nav-link">Lab</router-link>
          <a href="#contact" @click.prevent="scrollToSection('contact')" class="nav-link"
            >Contact</a
          >
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
          </a>
        </nav>
      </header>

      <main>
        <router-view />
      </main>

      <footer>
        <div class="footer-links"></div>
      </footer>
    </div>
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
  flex-wrap: wrap;
  align-items: center;
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

/* Large tablets and small laptops */
@media (max-width: 1024px) {
  nav {
    gap: 1rem;
  }

  .nav-link {
    font-size: 0.9rem;
  }
}

/* Tablets */
@media (max-width: 900px) {
  header {
    padding: 1.25rem 1.5rem;
  }

  nav {
    gap: 0.75rem;
  }

  .nav-link {
    font-size: 0.85rem;
    padding: 0.4rem 0;
  }
}

/* Mobile and small tablets */
@media (max-width: 768px) {
  header {
    flex-direction: row;
    gap: 0.25rem;
    padding: 0.5rem 0.75rem;
    min-height: auto;
  }

  .logo-text {
    font-size: 0.85rem;
    min-width: fit-content;
  }

  nav {
    flex: 1;
    justify-content: flex-end;
    gap: 0.15rem;
    flex-wrap: nowrap;
    overflow: hidden;
  }

  .nav-link {
    font-size: 0.6rem;
    padding: 0.2rem 0.1rem;
    white-space: nowrap;
    min-width: fit-content;
  }

  .github-link span {
    display: none;
  }

  .github-link svg {
    width: 14px;
    height: 14px;
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

/* Small mobile devices */
@media (max-width: 480px) {
  header {
    padding: 0.4rem 0.5rem;
  }

  .logo-text {
    font-size: 0.75rem;
  }

  nav {
    gap: 0.1rem;
  }

  .nav-link {
    font-size: 0.55rem;
    padding: 0.15rem 0.08rem;
  }

  .github-link svg {
    width: 12px;
    height: 12px;
  }
}

/* Extra small mobile devices */
@media (max-width: 360px) {
  header {
    padding: 0.3rem 0.4rem;
  }

  .logo-text {
    font-size: 0.7rem;
  }

  nav {
    gap: 0.08rem;
  }

  .nav-link {
    font-size: 0.5rem;
    padding: 0.1rem 0.05rem;
  }

  .github-link svg {
    width: 10px;
    height: 10px;
  }
}
</style>
