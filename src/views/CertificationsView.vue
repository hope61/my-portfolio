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
  <div class="certifications-grid">
    <div v-for="cert in certifications" :key="cert.id" class="certification-card">
      <div class="certification-header">
        <div class="certification-icon">
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
            <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
            <polyline points="14,2 14,8 20,8" />
            <line x1="16" y1="13" x2="8" y2="13" />
            <line x1="16" y1="17" x2="8" y2="17" />
            <polyline points="10,9 9,9 8,9" />
          </svg>
        </div>
        <div class="certification-badge">
          <span class="badge-text">Verified</span>
        </div>
      </div>

      <div class="certification-info">
        <h3 class="certification-title">{{ cert.title }}</h3>
        <p class="certification-issuer">{{ cert.issuer }}</p>
        <p class="certification-description">{{ cert.description }}</p>

        <div class="certification-details">
          <div class="detail-item">
            <span class="detail-label">Issued:</span>
            <span class="detail-value">{{ cert.date }}</span>
          </div>
        </div>

        <div class="certification-actions">
          <button
            @click="openCredential(cert.credentialUrl)"
            class="verify-button"
            :aria-label="`Verify ${cert.title} credential`"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
              <polyline points="15,3 21,3 21,9" />
              <line x1="10" y1="14" x2="21" y2="3" />
            </svg>
            Verify Credential
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.certifications-disclaimer {
  max-width: 600px;
  margin: 0 auto 2rem;
  padding: 1rem 1.5rem;
  background-color: var(--background-elevated);
  border-radius: var(--border-radius-md);
  border-left: 4px solid var(--accent-color);
}

.certifications-disclaimer p {
  margin: 0;
  color: var(--text-secondary);
  font-size: 0.9rem;
  line-height: 1.6;
  font-style: italic;
}

.certifications-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}

.certification-card {
  background-color: var(--background-secondary);
  border-radius: var(--border-radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
  border: 1px solid var(--border-color);
}

.certification-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.certification-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background-color: var(--background-elevated);
  border-bottom: 1px solid var(--border-color);
}

.certification-icon {
  color: var(--accent-color);
  display: flex;
  align-items: center;
}

.certification-badge {
  background-color: var(--accent-color);
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: var(--border-radius-sm);
  font-size: 0.75rem;
  font-weight: 600;
}

.certification-info {
  padding: 1.5rem;
}

.certification-title {
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
  color: var(--text-primary);
  font-weight: 600;
}

.certification-issuer {
  color: var(--accent-color);
  font-weight: 500;
  margin-bottom: 0.75rem;
  font-size: 0.9rem;
}

.certification-description {
  color: var(--text-secondary);
  margin-bottom: 1rem;
  line-height: 1.5;
  font-size: 0.9rem;
}

.certification-details {
  margin-bottom: 1rem;
}

.detail-item {
  display: flex;
  justify-content: center;
  margin-bottom: 0.5rem;
  font-size: 0.85rem;
  gap: 0.5rem;
}

.detail-label {
  color: var(--text-secondary);
  font-weight: 500;
}

.detail-value {
  color: var(--text-primary);
  font-weight: 600;
}

.certification-actions {
  display: flex;
  gap: 0.75rem;
}

.verify-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: var(--accent-color);
  color: white;
  border: none;
  border-radius: var(--border-radius-sm);
  font-weight: 500;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.verify-button:hover {
  background-color: var(--accent-color-hover);
  transform: translateY(-2px);
}

@media (max-width: 480px) {
  .certifications-disclaimer {
    margin: 0 1rem 2rem;
    padding: 0.75rem 1rem;
  }

  .certifications-disclaimer p {
    font-size: 0.85rem;
  }

  .certifications-grid {
    grid-template-columns: 1fr;
  }

  .certification-header {
    padding: 0.75rem 1rem;
  }

  .certification-info {
    padding: 1rem;
  }

  .certification-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .verify-button {
    justify-content: center;
  }
}
</style>
