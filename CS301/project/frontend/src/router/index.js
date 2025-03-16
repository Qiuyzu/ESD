import { createRouter, createWebHistory } from 'vue-router';

// Import all pages
import Login from '@/pages/Login.vue';
import Dashboard from '@/pages/Dashboard.vue';
import ClientManagement from '@/pages/ClientManagement.vue';
import AccountManagement from '@/pages/AccountManagement.vue';
import TransactionLogs from '@/pages/TransactionLogs.vue';

const routes = [
  { path: '/', redirect: '/login' }, // Redirect root to /login
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/clients', component: ClientManagement },
  { path: '/accounts', component: AccountManagement },
  { path: '/transactions', component: TransactionLogs },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
