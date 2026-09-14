export const profile = {
  name: 'Ege Musa',
  bio: 'First-year Software Engineering student at Plovdiv University. Python, Java, and Linux system administration.',
  email: 'ege.musa@icloud.com',
  github: 'https://github.com/hope61',
}

export const projects = [
  {
    id: 1,
    name: 'Refurbished hardware storefront',
    description:
      'Online shop for prebuilt PCs and second-hand components: faceted catalogue, user accounts and order history, admin panel with product CRUD and image uploads, cash-on-delivery checkout. Sessions and PBKDF2-SHA256 hashing are hand-written, and the data layer is plain sqlite3 with no ORM.',
    tech: ['Vue 3', 'FastAPI', 'SQLite', 'Docker', 'nginx'],
    url: 'https://github.com/hope61/rebootpc',
  },
  {
    id: 2,
    name: 'Internet situational-awareness console',
    description:
      'Dashboard pulling 23 live OSINT feeds — BGP hijacks, CVEs, ransomware leak sites, Tor activity, submarine cables — into one keyboard-driven console that ranks what changed since you last looked. Zero npm dependencies: the HTTP server, RSS parser, DER decoder and map renderer are all written against the standard library.',
    tech: ['Node.js', 'Vanilla JS'],
    url: 'https://github.com/hope61/blackwall',
  },
  {
    id: 3,
    name: 'Solana dip-alert Telegram bot',
    description:
      'Self-hosted bot watching Solana token prices across four time windows and alerting on sharp drops. Prices come from on-chain state via accountSubscribe and are cross-checked against DexScreener before anything fires. 528 offline unit tests.',
    tech: ['Python 3.12', 'SQLite'],
    url: 'https://github.com/hope61/dipbot',
  },
  {
    id: 4,
    name: 'Web novel reader',
    description:
      'Reading app with a Python API serving chapter content and a Vue frontend handling pagination, progress tracking and reading state. Includes the scraper that collects the chapters. Runs in Docker behind nginx.',
    tech: ['FastAPI', 'Vue 3', 'SQLite', 'Docker'],
    url: 'https://github.com/hope61/TbateReader',
  },
  {
    id: 5,
    name: 'FSMP core plugin',
    description:
      "The FSMP Minecraft server's core plugin, handling custom gameplay mechanics on the Folia multithreaded server platform. Built to a paying client's requirements.",
    tech: ['Java', 'Folia/Paper API'],
    url: 'https://github.com/hope61/FSMP-folia-core',
  },
  {
    id: 6,
    name: 'GriefPrevention Easy GUI',
    description:
      'Plugin wrapping a widely-used Minecraft land-protection plugin, replacing its command-line interaction with an in-game menu system.',
    tech: ['Java', 'Bukkit API'],
    url: 'https://github.com/hope61/GriefPreventionEasyGUI',
  },
  {
    id: 7,
    name: 'SpearControl',
    description:
      'Server plugin letting administrators selectively disable individual behaviours of a game mechanic, with granular per-function configuration.',
    tech: ['Java', 'Bukkit API'],
    url: 'https://github.com/hope61/SpearControl',
  },
  {
    id: 8,
    name: 'This site',
    description:
      'Personal portfolio with the live server panel below. A FastAPI backend queries the Proxmox API with a read-only token, caches and whitelists the fields, and nginx proxies it same-origin to the Vue frontend.',
    tech: ['Vue 3', 'FastAPI', 'Docker', 'nginx'],
    url: 'https://github.com/hope61/my-portfolio',
  },
]

export const certifications = [
  {
    id: 1,
    title: 'Linux System Administrator',
    issuer: 'SoftUni',
    date: '2024',
    url: 'https://softuni.bg/certificates/details/220749/812761c8',
  },
  {
    id: 2,
    title: 'Programming Fundamentals with Python',
    issuer: 'SoftUni',
    date: '2023',
    url: 'https://softuni.bg/certificates/details/194844/10b10e3d',
  },
  {
    id: 3,
    title: 'Python programming basics',
    issuer: 'SoftUni',
    date: '2023',
    url: 'https://softuni.bg/certificates/details/175017/f5f36f92',
  },
]

export const homelab = {
  specs: '6 × Intel Core i5-8500T @ 2.10GHz · 32 GB RAM · 224GB M.2 SSD + 1TB SSD',
  hypervisor: 'Proxmox VE',
  role: 'Self-hosted services and file sharing',
  router: 'TP-Link Archer AX50',
  switch: 'Ubiquiti Flex Mini',
  services: [
    'Pi-hole',
    'AMP Game Server',
    'Twingate',
    'Cloudflare Tunnels',
    'Immich',
    'Portainer',
    'CasaOS',
    'Pterodactyl',
    'Vaultwarden',
    'Homelable',
    'Speed Tracker',
    'Portfolio',
    'Windows VM',
  ],
}
