<template>
    <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-md shadow-lg">
        <slot />
        <button @click="closeModal" class="mt-4 bg-red-500 text-white px-4 py-2 rounded">Close</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue';
  
  const props = defineProps({ isOpen: Boolean });
  const emit = defineEmits(['close']);
  
  const closeModal = () => {
    emit('close');
  };
  </script>