<script setup>
// Animation library for text effects
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const titles = ref(['System Administrator', 'DevOps Engineer'])
const currentTitleIndex = ref(0)
const displayedTitle = ref('')
const isTyping = ref(true)
const typingSpeed = 100
const erasingSpeed = 50
const pauseTime = 1500

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

onMounted(() => {
  typeEffect()
})

function typeEffect() {
  const currentTitle = titles.value[currentTitleIndex.value]

  if (isTyping.value) {
    if (displayedTitle.value.length < currentTitle.length) {
      displayedTitle.value = currentTitle.substring(0, displayedTitle.value.length + 1)
      setTimeout(typeEffect, typingSpeed)
    } else {
      isTyping.value = false
      setTimeout(typeEffect, pauseTime)
    }
  } else {
    if (displayedTitle.value.length > 0) {
      displayedTitle.value = displayedTitle.value.substring(0, displayedTitle.value.length - 1)
      setTimeout(typeEffect, erasingSpeed)
    } else {
      isTyping.value = true
      currentTitleIndex.value = (currentTitleIndex.value + 1) % titles.value.length
      setTimeout(typeEffect, typingSpeed)
    }
  }
}
</script>

<template>
  <div class="container">
    <div class="hero-content">
      <h1 class="hero-title">
        <span class="greeting">Hello, I'm</span>
        <span class="name">Ege Musa</span>
      </h1>
      <div class="typing-container">
        <span class="typing-text">{{ displayedTitle }}</span>
        <span class="cursor" :class="{ blink: !isTyping }">|</span>
      </div>
      <p class="hero-description">
        System administrator and DevOps engineer focused on managing systems and infrastructure.
      </p>
      <div class="hero-buttons">
        <div class="button-group">
          <a href="#projects" @click.prevent="scrollToSection('projects')" class="btn btn-primary">
            <svg
              class="btn-icon"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
              <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
            </svg>
            <span>View My Work</span>
          </a>

          <router-link to="/homelab" class="btn btn-secondary">
            <svg
              class="btn-icon"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
              <line x1="8" y1="21" x2="16" y2="21" />
              <line x1="12" y1="17" x2="12" y2="21" />
            </svg>
            <span>View My Homelab</span>
          </router-link>
        </div>

        <a href="#contact" @click.prevent="scrollToSection('contact')" class="btn btn-cta">
          <svg
            class="btn-icon"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
            <polyline points="22,6 12,13 2,6" />
          </svg>
          <span>Get In Touch</span>
        </a>
      </div>
    </div>

    <div id="about" class="about-section">
      <h2 class="section-title">About Me</h2>
      <div class="about-content">
        <div class="about-text">
          <p>
            System administrator and DevOps engineer focused on managing systems and infrastructure.
          </p>
          <p>I have experience with Python, Bash, GoLang, Docker, and Linux.</p>
          <p>
            I like to build and maintain systems and infrastructure. i also like to automate tasks
            and processes.
          </p>
        </div>
        <div class="skills">
          <h3>My Skills</h3>
          <div class="skill-tags">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">RESTful APIs</span>
            <span class="skill-tag">Docker</span>
            <span class="skill-tag">CI/CD</span>
            <span class="skill-tag">Git</span>
            <span class="skill-tag">GoLang</span>
            <span class="skill-tag">Bash</span>
            <span class="skill-tag">SQL</span>
            <span class="skill-tag">Linux</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  padding: 2rem;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
  padding: 2rem 0;
}

.hero-title {
  margin-bottom: 1rem;
  line-height: 1.2;
}

.greeting {
  display: block;
  font-size: 1.5rem;
  font-weight: 400;
  margin-bottom: 0.5rem;
  color: var(--text-secondary);
}

.name {
  font-size: 3.5rem;
  font-weight: 700;
  background: linear-gradient(90deg, var(--dark-red) 0%, var(--dark-red-highlight) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  display: block;
  margin-bottom: 1rem;
}

.typing-container {
  height: 2rem;
  margin-bottom: 2rem;
  font-size: 1.5rem;
  font-weight: 500;
}

.typing-text {
  color: var(--accent-color);
}

.cursor {
  font-weight: 700;
  color: var(--accent-color);
}

.cursor.blink {
  animation: blink 1s infinite;
}

@keyframes blink {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}

.hero-description {
  font-size: 1.1rem;
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.8;
}

.hero-buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  margin-top: 3rem;
}

.button-group {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  border: 2px solid var(--accent-color);
  cursor: pointer;
  position: relative;
  overflow: hidden;
  min-width: 140px;
  justify-content: center;
  background: var(--accent-color);
  color: white;
}

.btn:hover {
  background: #dc0000;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 123, 255, 0.3);
}

.btn-icon {
  width: 18px;
  height: 18px;
  transition: transform 0.3s ease;
}

.btn:hover .btn-icon {
  transform: scale(1.05);
}

.about-section {
  padding-top: 2rem;
}

.section-title {
  text-align: center;
  margin-bottom: 2rem;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
  font-size: 1.75rem;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 3px;
  background-color: var(--accent-color);
}

.about-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  max-width: 1000px;
  margin: 0 auto;
}

.about-text p {
  margin-bottom: 1.5rem;
}

.skills h3 {
  margin-bottom: 1.5rem;
}

.skill-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.skill-tag {
  background-color: var(--background-elevated);
  color: var(--text-primary);
  padding: 0.3rem 0.6rem;
  border-radius: var(--border-radius-sm);
  font-size: 0.75rem;
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.skill-tag:hover {
  background-color: var(--accent-color);
  border-color: var(--accent-color);
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}

@media (max-width: 768px) {
  .name {
    font-size: 3rem;
  }

  .about-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .hero-buttons {
    gap: 1rem;
    margin-top: 2rem;
  }

  .button-group {
    flex-direction: column;
    gap: 0.75rem;
  }

  .btn {
    min-width: 120px;
    padding: 0.625rem 1.25rem;
    font-size: 0.9rem;
  }

  .btn-icon {
    width: 16px;
    height: 16px;
  }
}
</style>
