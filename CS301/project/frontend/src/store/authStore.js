import { defineStore } from 'pinia';
import api from '@/utils/api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || ''
  }),
  actions: {
    async login(credentials) {
      try {
        const response = await api.post('/auth/login', credentials);
        this.token = response.data.token;
        localStorage.setItem('token', this.token);
      } catch (error) {
        console.error(error);
      }
    },
    logout() {
      this.token = '';
      localStorage.removeItem('token');
    }
  }
});