<template>
  <div class="flex justify-center items-center h-screen">
    <form @submit.prevent="handleLogin" class="bg-white p-6 rounded shadow-md w-96">
      <h2 class="text-xl font-bold mb-4">Login</h2>
      <input v-model="email" type="email" placeholder="Email" class="w-full p-2 mb-3 border rounded" required />
      <input v-model="password" type="password" placeholder="Password" class="w-full p-2 mb-3 border rounded" required />
      <button type="submit" class="bg-blue-500 text-white w-full p-2 rounded">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/store/authStore';

const email = ref('');
const password = ref('');
const authStore = useAuthStore();

const handleLogin = async () => {
  await authStore.login({ email: email.value, password: password.value });
};
</script>