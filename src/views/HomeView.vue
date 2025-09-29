<script setup>
// Home page content
</script>

<template>
  <div class="home-content">
    <!-- Hero Section -->
    <div class="hero-section">
      <h1 class="name">Ege Musa</h1>
      <h2 class="title">Software Developer & System Administrator</h2>
      <p class="description">
        I specialize in Python, Golang development and Linux system administration.
      </p>

      <!-- GitHub Button -->
      <a
        href="https://github.com/egemusa"
        target="_blank"
        rel="noopener noreferrer"
        class="github-button"
      >
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <path
            d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
          />
        </svg>
      </a>
    </div>

    <!-- Quick Links -->
    <div class="quick-links">
      <router-link to="/homelab" class="quick-link">
        <div class="link-icon">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
            <line x1="8" y1="21" x2="16" y2="21" />
            <line x1="12" y1="17" x2="12" y2="21" />
          </svg>
        </div>
        <span>Homelab</span>
      </router-link>

      <router-link to="/certifications" class="quick-link">
        <div class="link-icon">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
            <polyline points="14,2 14,8 20,8" />
            <line x1="16" y1="13" x2="8" y2="13" />
            <line x1="16" y1="17" x2="8" y2="17" />
          </svg>
        </div>
        <span>Certifications</span>
      </router-link>

      <router-link to="/contact" class="quick-link">
        <div class="link-icon">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
            />
          </svg>
        </div>
        <span>Contact</span>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.home-content {
  padding: 3rem 2rem;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.hero-section {
  margin-bottom: 4rem;
  position: relative;
}

.name {
  font-size: 3.5rem;
  font-weight: 300;
  color: var(--text-primary);
  margin-bottom: 1rem;
  letter-spacing: 2px;
}

.title {
  font-size: 1.5rem;
  font-weight: 400;
  color: var(--text-secondary);
  margin-bottom: 2rem;
  letter-spacing: 1px;
}

.description {
  font-size: 1.1rem;
  line-height: 1.8;
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto;
}

.github-button {
  position: absolute;
  top: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid var(--border);
  border-radius: 50%;
  text-decoration: none;
  color: var(--text-secondary);
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.github-button:hover {
  color: var(--accent);
  background: rgba(255, 255, 255, 0.95);
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.quick-links {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.quick-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  padding: 1.5rem;
  background: var(--bg-secondary);
  border-radius: 15px;
  border: 1px solid var(--border);
  text-decoration: none;
  color: var(--text-primary);
  transition: all 0.3s ease;
  min-width: 120px;
}

.quick-link:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-light);
  border-color: var(--accent);
}

.link-icon {
  color: var(--accent);
}

.quick-link span {
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 1px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .home-content {
    padding: 2rem 1rem;
  }

  .name {
    font-size: 2.5rem;
  }

  .title {
    font-size: 1.3rem;
  }

  .description {
    font-size: 1rem;
  }

  .github-button {
    width: 36px;
    height: 36px;
  }

  .quick-links {
    gap: 1rem;
  }

  .quick-link {
    padding: 1rem;
    min-width: 100px;
  }
}

@media (max-width: 480px) {
  .name {
    font-size: 2rem;
  }

  .title {
    font-size: 1.1rem;
  }

  .github-button {
    width: 32px;
    height: 32px;
  }

  .quick-links {
    flex-direction: column;
    align-items: center;
  }

  .quick-link {
    width: 200px;
  }
}
</style>
