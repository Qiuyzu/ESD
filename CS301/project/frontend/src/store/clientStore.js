import { defineStore } from 'pinia';
import api from '@/utils/api';

export const useClientStore = defineStore('clients', {
  state: () => ({
    clients: []
  }),
  actions: {
    async fetchClients() {
      try {
        const response = await api.get('/clients');
        this.clients = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addClient(clientData) {
      try {
        await api.post('/clients', clientData);
        this.fetchClients();
      } catch (error) {
        console.error(error);
      }
    },
    async deleteClient(clientId) {
      try {
        await api.delete(`/clients/${clientId}`);
        this.fetchClients();
      } catch (error) {
        console.error(error);
      }
    }
  }
});