<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold">Client Management</h1>
    <button @click="showForm = true" class="bg-green-500 text-white p-2 mt-4">Add New Client</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const showForm = ref(false);
</script>
  