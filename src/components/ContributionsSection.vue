<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import TermWindow from './TermWindow.vue'
import { profile } from '../data.js'

const user = profile.github.split('/').pop()

const contributions = ref([])
const total = ref(null)
const failed = ref(false)
const scroller = ref(null)

// Each column is a Sunday-to-Saturday week, so a day's column counts weeks from
// the Sunday on or before the first day.
const cells = computed(() => {
  if (!contributions.value.length) return []
  const lead = new Date(contributions.value[0].date).getUTCDay()
  return contributions.value.map((day, i) => ({
    ...day,
    week: Math.floor((i + lead) / 7),
    weekday: (i + lead) % 7,
  }))
})

const weeks = computed(() => (cells.value.length ? cells.value.at(-1).week + 1 : 53))

// A month label sits over the first week that starts in that month.
const months = computed(() => {
  const labels = []
  let last = null
  for (const cell of cells.value) {
    if (cell.weekday !== 0) continue
    const month = new Date(cell.date).toLocaleString('en', { month: 'short', timeZone: 'UTC' })
    // A label closer than 3 weeks to the previous one would overlap it, so it
    // replaces it (the partial first month loses its label, as on GitHub).
    if (month !== last) {
      if (labels.length && cell.week - labels.at(-1).week < 3) labels.pop()
      labels.push({ week: cell.week, month })
    }
    last = month
  }
  return labels
})

onMounted(async () => {
  try {
    // shortcut: third-party scraper of the public profile calendar (no token needed);
    // move behind the backend with a GitHub GraphQL token if it goes away.
    const response = await fetch(`https://github-contributions-api.jogruber.de/v4/${user}?y=last`)
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    const result = await response.json()
    contributions.value = result.contributions
    total.value = result.total.lastYear
    // When the pane is too narrow and the graph scrolls, start at today like GitHub.
    await nextTick()
    if (scroller.value) scroller.value.scrollLeft = scroller.value.scrollWidth
  } catch (error) {
    console.error('Failed to fetch contributions:', error)
    failed.value = true
  }
})
</script>

<template>
  <TermWindow title="contributions" dir="code" command="git log --since='1 year' | wc -l">
    <div>
      <p v-if="failed" class="meta">
        Couldn't load the calendar.
        <a :href="profile.github" target="_blank" rel="noopener noreferrer">See it on GitHub</a>
      </p>
      <template v-else>
        <p class="total"><span class="count">{{ total ?? '…' }}</span> contributions in the last year</p>
        <div ref="scroller" class="scroll">
          <div
            class="calendar"
            :style="{ '--weeks': weeks }"
            role="img"
            :aria-label="`${total ?? 0} contributions in the last year`"
          >
            <span v-for="(day, i) in ['Mon', 'Wed', 'Fri']" :key="day" class="weekday" :style="{ gridRow: i * 2 + 3 }">{{
              day
            }}</span>
            <span
              v-for="label in months"
              :key="label.week"
              class="month"
              :style="{ gridColumn: label.week + 2 }"
              >{{ label.month }}</span
            >
            <span
              v-for="cell in cells"
              :key="cell.date"
              class="cell"
              :class="`l${cell.level}`"
              :style="{ gridColumn: cell.week + 2, gridRow: cell.weekday + 2 }"
              :title="`${cell.count} contributions on ${cell.date}`"
            ></span>
          </div>
        </div>
        <p class="legend meta" aria-hidden="true">
          Less
          <span v-for="level in 5" :key="level" class="cell" :class="`l${level - 1}`"></span>
          More
        </p>
      </template>
    </div>
  </TermWindow>
</template>

<style scoped>
.total {
  margin-bottom: var(--space-1);
}

.count {
  color: var(--link);
}

.scroll {
  overflow-x: auto;
}

/* GitHub's look (square days, even 3px gaps), stretched to fill the pane.
   Columns never go below 10px; past that the graph scrolls instead. */
.calendar {
  display: grid;
  grid-template-columns: auto repeat(var(--weeks), minmax(10px, 1fr));
  gap: 3px;
  min-width: calc(var(--weeks) * 13px + 3rem);
}

.weekday {
  grid-column: 1;
  padding-right: 1ch;
  font-size: var(--text-sm);
  /* Zero height so the label never makes its row taller than a square, which
     left uneven gaps under the Mon/Wed/Fri rows. */
  line-height: 0;
  color: var(--fg-muted);
  align-self: center;
}

.month {
  grid-row: 1;
  /* Labels are wider than one week column; let them run into the next. */
  white-space: nowrap;
  overflow: visible;
  width: 0;
  font-size: var(--text-sm);
  color: var(--fg-muted);
}

.cell {
  aspect-ratio: 1;
  border-radius: 2px;
}

.legend .cell {
  width: 10px;
}

.legend .cell:first-of-type {
  margin-left: 0.5ch;
}

.legend .cell:last-of-type {
  margin-right: 0.5ch;
}

/* One hue, rising lightness, from the ember palette: l1 is its selection colour,
   l3 its red, l4 its bright red. A hue jump at the top read as a different category. */
.l0 {
  background: #241211;
}
.l1 {
  background: #401d1c;
}
.l2 {
  background: #7a3132;
}
.l3 {
  background: #ce5456;
}
.l4 {
  background: #f07a74;
}

.meta {
  font-size: var(--text-sm);
  color: var(--fg-muted);
}

.legend {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 3px;
  margin-top: var(--space-1);
  font-size: var(--text-sm);
}
</style>
