<script setup>
import { ref, onMounted } from 'vue'
import TermWindow from './TermWindow.vue'
import { profile } from '../data.js'

const user = profile.github.split('/').pop()
const MAX_ROWS = 5

const rows = ref([])
const failed = ref(false)

const ago = (iso) => {
  const minutes = Math.floor((Date.now() - new Date(iso)) / 60000)
  if (minutes < 60) return `${Math.max(minutes, 1)}m`
  if (minutes < 60 * 24) return `${Math.floor(minutes / 60)}h`
  return `${Math.floor(minutes / (60 * 24))}d`
}

onMounted(async () => {
  try {
    // Repos by last push, not the /events feed: that feed lagged days behind real pushes.
    // Unauthenticated: 60 requests/hour per visitor IP, plenty for one load per visit.
    const response = await fetch(
      `https://api.github.com/users/${user}/repos?sort=pushed&per_page=${MAX_ROWS}`,
    )
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    rows.value = await response.json()
  } catch (error) {
    console.error('Failed to fetch GitHub activity:', error)
    failed.value = true
  }
})
</script>

<template>
  <TermWindow title="activity" dir="code" command="ls -t | head -5">
    <p v-if="failed" class="meta">
      Couldn't load activity.
      <a :href="profile.github" target="_blank" rel="noopener noreferrer">See it on GitHub</a>
    </p>
    <ul v-else>
      <li v-for="repo in rows" :key="repo.id">
        <time class="ago" :datetime="repo.pushed_at" :title="new Date(repo.pushed_at).toLocaleString()">{{
          ago(repo.pushed_at)
        }}</time>
        <span class="what">
          pushed to
          <a :href="repo.html_url" target="_blank" rel="noopener noreferrer">{{ repo.full_name }}</a>
        </span>
      </li>
    </ul>
  </TermWindow>
</template>

<style scoped>
li {
  display: flex;
  align-items: baseline;
  gap: 1ch;
}

/* Fixed width so the repo names line up like a git log column. */
.ago {
  flex: none;
  width: 4ch;
  text-align: right;
  color: var(--amber);
}

.what {
  min-width: 0;
  overflow-wrap: anywhere;
}

.meta {
  color: var(--fg-muted);
}
</style>
