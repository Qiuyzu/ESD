import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router'; // Import the router
import App from './App.vue';
import './assets/main.css';

const app = createApp(App);
app.use(createPinia());
app.use(router); // Add Vue Router
app.mount('#app');

