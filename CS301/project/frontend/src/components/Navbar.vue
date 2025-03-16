<template>
    <nav class="bg-gray-800 p-4 text-white flex justify-between">
      <router-link to="/dashboard" class="hover:text-gray-300">Dashboard</router-link>
      <router-link to="/clients" class="hover:text-gray-300">Clients</router-link>
      <router-link to="/accounts" class="hover:text-gray-300">Accounts</router-link>
      <router-link to="/transactions" class="hover:text-gray-300">Transactions</router-link>
      <button @click="logout" class="bg-red-500 px-4 py-2 rounded">Logout</button>
    </nav>
  </template>
  
  <script setup>
  import { useAuthStore } from '@/store/authStore';
  import { useRouter } from 'vue-router';
  
  const authStore = useAuthStore();
  const router = useRouter();
  
  const logout = () => {
    authStore.logout();
    router.push('/');
  };
  </script>