import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
    },
    {
      path: '/certifications',
      name: 'certifications',
      component: () => import('../views/CertificationsView.vue'),
    },
    {
      path: '/homelab',
      name: 'homelab',
      component: () => import('../views/HomelabView.vue'),
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/ContactView.vue'),
    },
  ],
})

export default router
