<script setup>
// A terminal pane, styled like a Ghostty split: `title` is the section heading
// (shown in the top border), and `dir` + `command` print the owner's p10k prompt
// as if that command produced the content below.
defineProps({
  title: { type: String, required: true },
  command: { type: String, required: true },
  dir: { type: String, default: '' },
})
</script>

<template>
  <section class="pane">
    <h2 class="title">{{ title }}</h2>
    <div class="prompt" aria-hidden="true">
      <p class="dir">
        <template v-if="dir">~/<span class="anchor">{{ dir }}</span></template>
        <span v-else class="anchor">~</span>
      </p>
      <p><span class="char">❯</span> {{ command }}</p>
    </div>
    <slot />
  </section>
</template>

<style scoped>
.pane {
  position: relative;
  padding: var(--space-2);
  border: 1px solid var(--rule);
  transition: border-color 0.15s;
}

/* Hovered pane gets the accent border, like the focused split. */
.pane:hover {
  border-color: var(--accent);
}

/* Sits on the top border, tmux pane-title style. */
.title {
  position: absolute;
  top: -0.65em;
  left: 1.5ch;
  padding: 0 0.5ch;
  background: var(--bg);
  font-size: var(--text-sm);
  color: var(--fg-muted);
  transition: color 0.15s;
}

.pane:hover .title {
  color: var(--accent);
}

.prompt {
  margin-bottom: var(--space-1);
  overflow-wrap: anywhere;
}

.dir {
  color: var(--amber);
}

.anchor {
  color: var(--link);
}

.char {
  color: var(--accent);
}
</style>
