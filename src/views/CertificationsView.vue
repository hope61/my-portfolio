<script setup>
import { ref } from 'vue'

// Certifications data
const certifications = ref([
  {
    id: 1,
    title: 'Python programming basics',
    issuer: 'SoftUni',
    date: '2023',
    credentialUrl: 'https://softuni.bg/certificates/details/175017/f5f36f92',
    description: 'Successfully completed Python programming basics course.',
  },
  {
    id: 2,
    title: 'Programming Fundamentals with Python',
    issuer: 'SoftUni',
    date: '2023',
    credentialUrl: 'https://softuni.bg/certificates/details/194844/10b10e3d',
    description: 'Successfully completed Programming Fundamentals with Python course.',
  },
  {
    id: 3,
    title: 'Linux System Administrator',
    issuer: 'SoftUni',
    date: '2024',
    credentialUrl: 'https://softuni.bg/certificates/details/220749/812761c8',
    description: 'Successfully completed Linux System Administrator course.',
  },
  {
    id: 4,
    title: 'JavaScript Basics',
    issuer: 'SoftUni',
    date: '2025',
    credentialUrl: 'https://softuni.bg/certificates/details/244145/b107218d',
    description: 'Successfully completed JavaScript Basics course.',
  },
])

const openCredential = (url) => {
  window.open(url, '_blank', 'noopener,noreferrer')
}
</script>

<template>
  <div class="certifications-content">
    <!-- Header -->
    <div class="content-header">
      <h1 class="main-title">Certifications</h1>
    </div>

    <!-- Certifications Grid -->
    <div class="certifications-grid">
      <div v-for="cert in certifications" :key="cert.id" class="certification-card">
        <div class="cert-header">
          <div class="cert-icon">
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
        </div>

        <div class="cert-content">
          <h3 class="cert-title">{{ cert.title }}</h3>
          <div class="cert-meta">
            <span class="cert-issuer">{{ cert.issuer }}</span>
            <span class="cert-date">{{ cert.date }}</span>
          </div>
          <p class="cert-description">{{ cert.description }}</p>
        </div>

        <div class="cert-actions">
          <button
            @click="openCredential(cert.credentialUrl)"
            class="verify-button"
            :aria-label="`Verify ${cert.title} credential`"
          >
            <div class="button-icon">
              <svg
                width="16"
                height="16"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                <polyline points="15,3 21,3 21,9" />
                <line x1="10" y1="14" x2="21" y2="3" />
              </svg>
            </div>
            <span class="button-text">VIEW CREDENTIAL</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.certifications-content {
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

.certifications-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.certification-card {
  background: var(--bg-secondary);
  border-radius: 20px;
  border: 1px solid var(--border);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.cert-header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1.5rem 2rem;
  background: rgba(0, 102, 204, 0.05);
  border-bottom: 1px solid var(--border);
}

.cert-icon {
  color: var(--accent);
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 102, 204, 0.1);
  border-radius: 12px;
}

.cert-content {
  padding: 2rem;
  flex: 1;
}

.cert-title {
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: 1rem;
  line-height: 1.4;
}

.cert-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.cert-issuer {
  color: var(--accent);
  font-weight: 600;
  font-size: 0.9rem;
}

.cert-date {
  color: var(--text-muted);
  font-size: 0.9rem;
  font-weight: 500;
}

.cert-description {
  color: var(--text-secondary);
  line-height: 1.6;
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
}

.cert-actions {
  padding: 0 2rem 2rem;
  margin-top: auto;
}

.verify-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.8rem 1.2rem;
  background: var(--accent);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.verify-button:hover {
  background: var(--accent-dark);
}

.button-icon {
  color: white;
}

/* Responsive Design */
@media (max-width: 768px) {
  .certifications-content {
    padding: 1rem;
  }

  .main-title {
    font-size: 2rem;
  }

  .certifications-grid {
    grid-template-columns: 1fr;
  }

  .cert-header {
    padding: 1rem 1.5rem;
  }

  .cert-content {
    padding: 1.5rem;
  }

  .cert-actions {
    padding: 0 1.5rem 1.5rem;
  }

  .cert-meta {
    flex-direction: column;
    gap: 0.5rem;
    align-items: flex-start;
  }
}

@media (max-width: 480px) {
  .main-title {
    font-size: 1.8rem;
  }

  .cert-header {
    padding: 0.75rem 1rem;
  }

  .cert-content {
    padding: 1rem;
  }

  .cert-actions {
    padding: 0 1rem 1rem;
  }

  .cert-icon {
    width: 50px;
    height: 50px;
  }
}
</style>
