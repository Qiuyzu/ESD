<template>
  <div class="flex">
    <Sidebar />
    <div class="flex-1 p-6">
      <Navbar />
      <slot />
    </div>
  </div>
</template>

<script setup>
import Sidebar from '@/components/Sidebar.vue';
import Navbar from '@/components/Navbar.vue';
</script>
