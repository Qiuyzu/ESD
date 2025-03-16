<template>
    <div>
      <label :for="id" class="block font-medium text-gray-700">{{ label }}</label>
      <input :id="id" v-model="model" :type="type" class="w-full p-2 border rounded-md" />
    </div>
  </template>
  
  <script setup>
  import { defineProps, ref } from 'vue';
  
  const props = defineProps({
    label: String,
    id: String,
    type: { type: String, default: 'text' }
  });
  
  const model = ref('');
  </script>