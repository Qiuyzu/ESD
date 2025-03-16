<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold">Dashboard</h1>
    <p v-if="user.role === 'admin'">Welcome, Admin! Manage users and clients.</p>
    <p v-if="user.role === 'agent'">Welcome, Agent! Manage your clients and transactions.</p>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/store/authStore';
const authStore = useAuthStore();
const user = authStore.user;
</script>