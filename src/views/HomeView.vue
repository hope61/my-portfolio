<script setup>
// Animation library for text effects
import { onMounted, ref } from 'vue'

const titles = ref(['System Administrator', 'DevOps Engineer'])
const currentTitleIndex = ref(0)
const displayedTitle = ref('')
const isTyping = ref(true)
const typingSpeed = 100
const erasingSpeed = 50
const pauseTime = 1500

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
        <a
          href="#projects"
          @click.prevent="
            document
              .getElementById('projects')
              .scrollIntoView({ behavior: 'smooth', block: 'start' })
          "
          class="btn"
          >View My Work</a
        >
        <a
          href="#contact"
          @click.prevent="
            document
              .getElementById('contact')
              .scrollIntoView({ behavior: 'smooth', block: 'start' })
          "
          class="btn btn-outline"
          >Contact Me</a
        >
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
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
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
    flex-direction: column;
    align-items: center;
  }

  .btn {
    width: 100%;
    max-width: 200px;
    text-align: center;
  }
}
</style>
