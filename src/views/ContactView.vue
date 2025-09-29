<script setup>
// Contact information component
</script>

<template>
  <div class="contact-content">
    <!-- Header -->
    <div class="content-header">
      <h1 class="main-title">Contact Information</h1>
    </div>

    <!-- Contact Cards -->
    <div class="contact-grid">
      <div class="contact-card">
        <div class="contact-header">
          <div class="contact-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
            </svg>
          </div>
          <h3 class="contact-title">Phone</h3>
        </div>
        <div class="contact-info">
          <a href="tel:+359877335187" class="contact-link">+359 87 733 5187</a>
          <p class="contact-description">Direct communication channel</p>
        </div>
      </div>

      <div class="contact-card">
        <div class="contact-header">
          <div class="contact-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
              <polyline points="22,6 12,13 2,6"/>
            </svg>
          </div>
          <h3 class="contact-title">Email</h3>
        </div>
        <div class="contact-info">
          <a href="mailto:ege.musa@icloud.com" class="contact-link">ege.musa@icloud.com</a>
          <p class="contact-description">Primary communication method</p>
        </div>
      </div>

      <div class="contact-card">
        <div class="contact-header">
          <div class="contact-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
              <circle cx="12" cy="10" r="3"/>
            </svg>
          </div>
          <h3 class="contact-title">Location</h3>
        </div>
        <div class="contact-info">
          <span class="contact-link">Krumovgrad, Bulgaria</span>
          <p class="contact-description">Physical presence coordinates</p>
        </div>
      </div>

      <div class="contact-card">
        <div class="contact-header">
          <div class="contact-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
            </svg>
          </div>
          <h3 class="contact-title">GitHub</h3>
        </div>
        <div class="contact-info">
          <a href="https://github.com/hope61" target="_blank" rel="noopener noreferrer" class="contact-link">
            github.com/hope61
          </a>
          <p class="contact-description">Code repository access</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.contact-content {
  padding: 2rem;
  max-width: 100%;
}

.content-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border);
  text-align: center;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 300;
  color: var(--text-primary);
  letter-spacing: 1px;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.contact-card {
  background: var(--bg-secondary);
  padding: 2rem;
  border-radius: 20px;
  border: 1px solid var(--border);
}

.contact-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.contact-icon {
  color: var(--accent);
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 102, 204, 0.1);
  border-radius: 15px;
}

.contact-title {
  font-size: 1.3rem;
  font-weight: 500;
  color: var(--text-primary);
}

.contact-info {
  margin-bottom: 1rem;
}

.contact-link {
  display: block;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--accent);
  text-decoration: none;
  margin-bottom: 0.5rem;
}

.contact-link:hover {
  color: var(--accent-dark);
}

.contact-description {
  color: var(--text-secondary);
  font-size: 0.9rem;
  line-height: 1.5;
}

/* Responsive Design */
@media (max-width: 768px) {
  .contact-content {
    padding: 1rem;
  }
  
  .main-title {
    font-size: 2rem;
  }
  
  .contact-grid {
    grid-template-columns: 1fr;
  }
  
  .contact-card {
    padding: 1.5rem;
  }
  
  .contact-header {
    flex-direction: column;
    text-align: center;
    gap: 0.5rem;
  }
  
  .contact-icon {
    width: 50px;
    height: 50px;
  }
}

@media (max-width: 480px) {
  .main-title {
    font-size: 1.8rem;
  }
  
  .contact-card {
    padding: 1rem;
  }
}
</style>