<script setup>
// Futuristic background animations
</script>

<template>
  <div class="lain-container">
    <!-- Minimal Futuristic Background -->
    <div class="minimal-background">
      <!-- Subtle Grid -->
      <div class="subtle-grid"></div>

      <!-- Floating Elements -->
      <div class="floating-elements">
        <div class="element element-1"></div>
        <div class="element element-2"></div>
        <div class="element element-3"></div>
        <div class="element element-4"></div>
        <div class="element element-5"></div>
      </div>

      <!-- Gentle Particles -->
      <div class="gentle-particles">
        <div
          class="particle"
          v-for="i in 12"
          :key="i"
          :style="{
            left: `${Math.random() * 100}%`,
            animationDelay: `${Math.random() * 6}s`,
            animationDuration: `${5 + Math.random() * 4}s`,
          }"
        ></div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Navigation -->
      <nav class="main-nav">
        <router-link to="/" class="nav-item">
          <span class="nav-text">HOME</span>
          <div class="nav-line"></div>
        </router-link>
        <router-link to="/homelab" class="nav-item">
          <span class="nav-text">HOMELAB</span>
          <div class="nav-line"></div>
        </router-link>
        <router-link to="/certifications" class="nav-item">
          <span class="nav-text">CERTIFICATIONS</span>
          <div class="nav-line"></div>
        </router-link>
        <router-link to="/contact" class="nav-item">
          <span class="nav-text">CONTACT</span>
          <div class="nav-line"></div>
        </router-link>
      </nav>

      <!-- Content Area -->
      <main class="content-area">
        <router-view />
      </main>
    </div>
  </div>
</template>

<style>
/* Global Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Root Variables */
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-tertiary: #f1f3f4;
  --text-primary: #1a1a1a;
  --text-secondary: #666666;
  --text-muted: #999999;
  --accent: #0066cc;
  --accent-light: #4d94ff;
  --accent-dark: #004499;
  --border: #e0e0e0;
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  --shadow-light: 0 2px 10px rgba(0, 0, 0, 0.05);
}

/* Base Styles */
body {
  font-family:
    'Inter',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  overflow-x: hidden;
  line-height: 1.6;
}

/* Lain Container */
.lain-container {
  min-height: 100vh;
  position: relative;
  background: var(--bg-primary);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Minimal Background */
.minimal-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 50%, #e9ecef 100%);
  overflow: hidden;
}

/* Subtle Grid */
.subtle-grid {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image:
    linear-gradient(rgba(0, 102, 204, 0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 102, 204, 0.08) 1px, transparent 1px);
  background-size: 80px 80px;
  z-index: 1;
}

/* Floating Elements */
.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 2;
}

.element {
  position: absolute;
  border: 1px solid rgba(0, 102, 204, 0.15);
  animation: element-float 20s ease-in-out infinite;
}

.element-1 {
  width: 40px;
  height: 40px;
  top: 20%;
  left: 15%;
  border-radius: 50%;
  animation-delay: 0s;
}

.element-2 {
  width: 30px;
  height: 30px;
  top: 70%;
  left: 80%;
  transform: rotate(45deg);
  animation-delay: 5s;
}

.element-3 {
  width: 50px;
  height: 50px;
  top: 80%;
  left: 20%;
  border-radius: 15px;
  animation-delay: 10s;
}

.element-4 {
  width: 35px;
  height: 35px;
  top: 30%;
  left: 75%;
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
  animation-delay: 15s;
}

.element-5 {
  width: 45px;
  height: 45px;
  top: 60%;
  left: 10%;
  border-radius: 50%;
  animation-delay: 20s;
}

/* Gentle Particles */
.gentle-particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 3;
}

.particle {
  position: absolute;
  width: 2px;
  height: 2px;
  background: rgba(0, 102, 204, 0.2);
  border-radius: 50%;
  animation: particle-float linear infinite;
}

/* Animations */

@keyframes element-float {
  0%,
  100% {
    transform: translateY(0px) rotate(0deg);
    opacity: 0.1;
  }
  50% {
    transform: translateY(-15px) rotate(180deg);
    opacity: 0.2;
  }
}

@keyframes particle-float {
  0% {
    transform: translateY(100vh) translateX(0px);
    opacity: 0;
  }
  10% {
    opacity: 0.15;
  }
  90% {
    opacity: 0.15;
  }
  100% {
    transform: translateY(-100px) translateX(30px);
    opacity: 0;
  }
}

/* Main Content */
.main-content {
  position: relative;
  z-index: 10;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Navigation */
.main-nav {
  display: flex;
  gap: 3rem;
  margin-bottom: 3rem;
  padding: 1rem 0;
}

.nav-item {
  position: relative;
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 500;
  font-size: 14px;
  letter-spacing: 2px;
  transition: all 0.3s ease;
  padding: 0.5rem 0;
}

.nav-item.router-link-active {
  color: var(--accent);
}

.nav-line {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--accent);
  transition: width 0.3s ease;
}

.nav-item.router-link-active .nav-line {
  width: 100%;
}

/* Content Area */
.content-area {
  width: 100%;
  max-width: 800px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(0, 102, 204, 0.1);
  overflow: hidden;
  position: relative;
  z-index: 10;
}

/* Responsive Design */
@media (max-width: 768px) {
  .main-content {
    padding: 1rem;
  }

  .main-nav {
    flex-direction: column;
    gap: 1rem;
    align-items: center;
  }

  .nav-item {
    font-size: 12px;
  }

  .content-area {
    border-radius: 15px;
  }

  .shape {
    opacity: 0.5;
  }
}

@media (max-width: 480px) {
  .main-nav {
    gap: 0.5rem;
  }

  .nav-item {
    font-size: 11px;
    letter-spacing: 1px;
  }

  .content-area {
    border-radius: 10px;
  }
}
</style>
