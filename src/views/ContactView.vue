<script setup>
// Contact information component
</script>

<template>
  <div class="contact-container">
    <div class="contact-info">
      <div class="info-item">
        <div class="info-icon">
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
              d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
            ></path>
          </svg>
        </div>
        <div class="info-content">
          <h3>Phone</h3>
          <p><a href="tel:+359877335187">087 733 5187</a></p>
        </div>
      </div>

      <div class="info-item">
        <div class="info-icon">
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
              d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"
            ></path>
            <polyline points="22,6 12,13 2,6"></polyline>
          </svg>
        </div>
        <div class="info-content">
          <h3>Email</h3>
          <p><a href="mailto:ege.musa@icloud.com">ege.musa@icloud.com</a></p>
        </div>
      </div>

      <div class="info-item">
        <div class="info-icon">
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
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
            <circle cx="12" cy="10" r="3"></circle>
          </svg>
        </div>
        <div class="info-content">
          <h3>Location</h3>
          <p>Krumovgrad, Bulgaria</p>
        </div>
      </div>

      <div class="info-item">
        <div class="info-icon">
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
        </div>
        <div class="info-content">
          <h3>GitHub</h3>
          <p>
            <a href="https://github.com/hope61" target="_blank" rel="noopener noreferrer"
              >github.com/hope61</a
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.contact-container {
  max-width: var(--content-width);
  margin: 0 auto;
  padding: 0 2rem;
}

/* Removed contact card */

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

.contact-info {
  margin-top: 2rem;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.info-item {
  display: flex;
  align-items: center;
  margin-bottom: 1.5rem;
  padding: 0.75rem;
  border-radius: var(--border-radius-md);
  transition: all 0.3s ease;
  border: 1px solid transparent;
}

.info-item:hover {
  background-color: var(--background-elevated);
  border-color: var(--border-color);
  transform: translateX(5px);
}

.info-item:last-child {
  margin-bottom: 0;
}

.info-icon {
  margin-right: 1.25rem;
  background-color: var(--background-elevated);
  width: 42px;
  height: 42px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-color);
  flex-shrink: 0;
  transition: all 0.3s ease;
  border: 1px solid var(--border-color);
}

.info-item:hover .info-icon {
  background-color: var(--accent-color);
  color: white;
  border-color: var(--accent-color);
}

.info-content {
  flex-grow: 1;
}

.info-content h3 {
  margin-bottom: 0.25rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.info-content p {
  color: var(--text-secondary);
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.6;
}

.info-content a {
  color: var(--text-secondary);
  text-decoration: none;
  transition: color 0.2s ease;
}

.info-content a:hover {
  color: var(--accent-color);
}

@media (max-width: 768px) {
  .contact-container {
    padding: 0 1rem;
  }

  .info-item {
    flex-direction: row;
    align-items: center;
    padding: 0.5rem;
  }

  .info-icon {
    width: 38px;
    height: 38px;
    margin-right: 1rem;
  }

  .info-content h3 {
    font-size: 1rem;
  }
}
</style>
