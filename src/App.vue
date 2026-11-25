<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import TermWindow from './components/TermWindow.vue'
import HomelabSection from './components/HomelabSection.vue'
import ProjectsSection from './components/ProjectsSection.vue'
import CertsSection from './components/CertsSection.vue'
import ContributionsSection from './components/ContributionsSection.vue'
import ActivitySection from './components/ActivitySection.vue'
import { profile, layout } from './data.js'

const handle = profile.github.split('/').pop()

// Names used by `layout` in data.js.
const sections = {
  projects: ProjectsSection,
  contributions: ContributionsSection,
  activity: ActivitySection,
  homelab: HomelabSection,
  certifications: CertsSection,
}

// Taskbar clock, minute precision.
const clock = () => new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
const time = ref(clock())
let timer = null
onMounted(() => {
  timer = setInterval(() => (time.value = clock()), 15000)
})
onUnmounted(() => clearInterval(timer))
</script>

<template>
  <div class="page">
    <aside>
      <TermWindow title="about" command="neofetch">
        <header>
          <h1>{{ profile.name }}</h1>
          <p class="handle">{{ handle }}@github</p>
          <p class="divider" aria-hidden="true">----------------</p>
          <dl class="info">
            <div>
              <dt>Location</dt>
              <dd>{{ profile.location }}</dd>
            </div>
            <div>
              <dt>Email</dt>
              <dd>
                <a :href="`mailto:${profile.email}`">{{ profile.email }}</a>
              </dd>
            </div>
            <div>
              <dt>GitHub</dt>
              <dd>
                <a :href="profile.github" target="_blank" rel="noopener noreferrer">{{
                  profile.github.replace('https://', '')
                }}</a>
              </dd>
            </div>
          </dl>
          <p class="bio">{{ profile.bio }}</p>
          <p class="swatches" aria-hidden="true">
            <span v-for="n in 8" :key="n" :class="`c${n}`"></span>
          </p>
          <p class="prompt" aria-hidden="true"><span class="char">❯</span> <span class="cursor"></span></p>
        </header>
      </TermWindow>

      <component :is="sections[name]" v-for="name in layout.sidebar" :key="name" />
    </aside>

    <main>
      <component :is="sections[name]" v-for="name in layout.main" :key="name" />
    </main>

    <!-- tmux-style status line. -->
    <footer class="status">
      <span class="session">{{ handle }}</span>
      <span class="window">0:portfolio*</span>
      <a :href="`mailto:${profile.email}`">{{ profile.email }}</a>
      <a :href="profile.github" target="_blank" rel="noopener noreferrer">github</a>
      <span class="clock">{{ time }}</span>
    </footer>
  </div>
</template>

<style scoped>
.page {
  display: grid;
  grid-template-columns: 20rem minmax(0, 1fr);
  gap: var(--space-3);
  max-width: 82rem;
  margin: 0 auto;
  padding: var(--space-4) var(--space-3);
}

aside,
main {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  min-width: 0;
}

.handle {
  color: var(--amber);
}

.divider {
  color: var(--fg-muted);
}

.info div {
  display: flex;
  gap: 0.5ch;
}

.info dt {
  color: var(--accent);
}

.info dt::after {
  content: ':';
  color: var(--fg);
}

.info dd {
  min-width: 0;
  overflow-wrap: anywhere;
}

.bio {
  margin-top: var(--space-1);
  color: var(--fg-muted);
}

/* The neofetch colour blocks: ember's 8 normal ANSI colours. */
.swatches {
  display: flex;
  margin-top: var(--space-1);
}

.swatches span {
  width: 1.5ch;
  height: 1em;
}

.c1 { background: #412d2b; }
.c2 { background: #ce5456; }
.c3 { background: #758764; }
.c4 { background: #c18154; }
.c5 { background: #6d7c9a; }
.c6 { background: #965165; }
.c7 { background: #659193; }
.c8 { background: #cbbab2; }

.prompt {
  margin-top: var(--space-1);
}

.char {
  color: var(--accent);
}

.cursor {
  display: inline-block;
  width: 1ch;
  height: 1em;
  vertical-align: text-bottom;
  background: #e66e68;
  animation: blink 1s steps(1) infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cursor {
    animation: none;
  }
}

.status {
  grid-column: 1 / -1;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0 2ch;
  background: var(--rule);
  font-size: var(--text-sm);
}

.session {
  padding: 0 1ch;
  background: var(--accent);
  color: var(--bg);
}

.window {
  color: var(--fg-bright);
}

.status a {
  color: var(--fg);
}

.clock {
  margin-left: auto;
  padding-right: 1ch;
  color: var(--fg-muted);
}

@media (max-width: 768px) {
  .page {
    grid-template-columns: minmax(0, 1fr);
    padding: var(--space-2) var(--space-2);
  }
}
</style>
