<script setup>
// Timeline component for software engineering journey
</script>

<template>
  <div class="timeline">
    <!-- Timeline Item 1 -->
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="timeline-date">2020</div>
        <h3>Introduction to Programming</h3>
        <p class="timeline-company">Tech Innovations Inc.</p>
        <p>
          I started learning programming with Python. In 2020, my IT teacher gave me a book about
          Python, and from there I spiraled into programming. I began with basic Discord bots and
          automations. Before that, I had basic knowledge about computers because of games and the
          interest I had in cheats.
        </p>
      </div>
    </div>

    <!-- Timeline Item 2 -->
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="timeline-date">2023</div>
        <h3>First Softuni Certificate</h3>
        <p>In May of 2023, I finished my Python basics course at SoftUni with a score of 5.84/6.</p>
      </div>
    </div>

    <!-- Timeline Item 3 -->
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="timeline-date">2024</div>
        <h3>Setting up my first homelab</h3>
        <p>
          I got my first homelab in January of 2024. I bought a Dell Mini Optiplex which I installed
          Proxmox on and set up basically a de-Googled infrastructure. Before that, I had experience
          with Linux but I wasn't really into it, with Oracle VPS since I provided hosting services
          for Minecraft servers. I took interest in Linux because of YouTubers like NetworkChuck and
          TechnoTim.
        </p>
      </div>
    </div>

    <!-- Timeline Item 4 -->
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="timeline-date">2025</div>
        <h3>Getting back into programming</h3>
        <p>
          Since I got my first VPS and started providing hosting services for Minecraft servers, I
          stopped programming for a while. I only made small scripts to automate weekly checks of my
          servers. For a whole year, I only did DevOps and messed around with Linux, but this year I
          got back into coding because of the YouTuber ThePrimeTime. I started learning GoLang and
          built a novel reading website with a GoLang backend and a Python API scraper to get the
          novels.
        </p>
      </div>
    </div>

    <!-- Timeline Item 5 -->
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="timeline-date">2025 - Beginning of summer</div>
        <h3>Coding telegram bots</h3>
        <p>
          I started coding trading Telegram bots for my cousin, which I got paid for since the bots
          had subscription plans and were mostly for signaling good trades. They were made using
          Python, and the bot that managed the subscriptions was made in C#. Since I was studying it
          in school, I thought I could give it a try.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.timeline-company {
  color: var(--text-secondary);
  font-style: italic;
  margin-bottom: 1rem;
}
</style>
