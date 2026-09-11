<script setup>
import { ref, onUnmounted } from 'vue'
import LiveStats from './LiveStats.vue'
import { homelab } from '../data.js'
import topologyImage from '../assets/homelab-topology.webp'

const rows = [
  ['Hardware', homelab.specs],
  ['Hypervisor', homelab.hypervisor],
  ['Role', homelab.role],
  ['Router', homelab.router],
  ['Switch', homelab.switch],
]

const topologyAlt =
  'Network topology: router to switch to the Proxmox host, which runs four VMs ' +
  'and six LXC containers, with three Docker containers under Portainer'

const dialog = ref(null)
const zoomed = ref(false)

const open = () => {
  // Without <dialog> support there is no modal to show, so fall back to the
  // plain image rather than making the diagram unopenable.
  if (!dialog.value?.showModal) {
    window.open(topologyImage, '_blank', 'noopener')
    return
  }
  zoomed.value = false
  dialog.value.showModal()
  document.body.style.overflow = 'hidden'
}

const close = () => dialog.value?.close()

// Fires for both close() and the Escape key, so the scroll lock is released
// on either path.
const onClose = () => {
  document.body.style.overflow = ''
}

// The image stops its own clicks, so anything reaching the stage landed on the
// backdrop around it.
const onStageClick = () => close()

onUnmounted(() => {
  document.body.style.overflow = ''
})
</script>

<template>
  <section>
    <h2>Homelab</h2>

    <LiveStats />

    <figure class="topology">
      <button type="button" class="thumb" @click="open">
        <img
          :src="topologyImage"
          width="1400"
          height="1848"
          loading="lazy"
          decoding="async"
          :alt="topologyAlt"
        />
      </button>
      <figcaption>Network topology &mdash; click to enlarge</figcaption>
    </figure>

    <dialog
      ref="dialog"
      class="lightbox"
      aria-label="Network topology"
      @close="onClose"
      @click="onStageClick"
    >
      <div class="stage" :class="{ zoomed }">
        <img :src="topologyImage" :alt="topologyAlt" @click.stop="zoomed = !zoomed" />
      </div>
      <button type="button" class="close" @click.stop="close">Close</button>
    </dialog>

    <dl>
      <div v-for="[label, value] in rows" :key="label" class="row">
        <dt>{{ label }}</dt>
        <dd>{{ value }}</dd>
      </div>
      <div class="row">
        <dt>Services</dt>
        <dd>
          <ul class="services">
            <li v-for="service in homelab.services" :key="service" class="chip">{{ service }}</li>
          </ul>
        </dd>
      </div>
    </dl>
  </section>
</template>

<style scoped>
.topology {
  margin-bottom: var(--space-4);
}

/* The diagram is drawn on a dark canvas, so it sits in a matching panel
   rather than floating on the page background. */
.thumb {
  display: block;
  width: 100%;
  padding: var(--space-2);
  background: #141414;
  border: 1px solid var(--rule);
  cursor: zoom-in;
  font: inherit;
  color: inherit;
}

.topology figcaption {
  margin-top: var(--space-1);
  font-size: var(--text-sm);
  color: var(--fg-muted);
}

.lightbox {
  width: 100vw;
  max-width: 100vw;
  height: 100dvh;
  max-height: 100dvh;
  margin: 0;
  padding: 0;
  border: 0;
  background: transparent;
  overflow: hidden;
}

.lightbox::backdrop {
  /* Near-opaque: at 0.85 the page text behind stayed legible through it. */
  background: rgb(0 0 0 / 0.97);
  backdrop-filter: blur(2px);
}

.stage {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding: var(--space-2);
  overflow: auto;
  overscroll-behavior: contain;
}

.stage img {
  max-width: 100%;
  max-height: 100%;
  cursor: zoom-in;
}

/* Zoomed: drop the centring so the image can exceed the viewport and the
   stage scrolls it, which is the only way to read the node labels. */
.stage.zoomed {
  display: block;
}

.stage.zoomed img {
  width: 1400px;
  max-width: none;
  max-height: none;
  margin: 0 auto;
  cursor: zoom-out;
}

.close {
  position: fixed;
  top: var(--space-2);
  right: var(--space-2);
  padding: var(--space-1) var(--space-2);
  background: #141414;
  border: 1px solid #444;
  color: #e8e8e8;
  font: inherit;
  font-size: var(--text-sm);
  cursor: pointer;
}

.close:hover {
  background: #222;
}

.row {
  display: flex;
  gap: var(--space-2);
  padding: var(--space-1) 0;
  border-bottom: 1px solid var(--rule);
}

dt {
  flex: 0 0 7rem;
  color: var(--fg-muted);
}

dd {
  flex: 1;
  min-width: 0;
}

.services {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-1);
}

@media (max-width: 600px) {
  .row {
    flex-direction: column;
    gap: 0;
  }

  dt {
    flex: none;
  }
}
</style>
