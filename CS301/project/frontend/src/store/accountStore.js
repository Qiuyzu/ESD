import { defineStore } from 'pinia';
import api from '@/utils/api';

export const useAccountStore = defineStore('accounts', {
  state: () => ({
    accounts: []
  }),
  actions: {
    async fetchAccounts() {
      try {
        const response = await api.get('/accounts');
        this.accounts = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async createAccount(accountData) {
      try {
        await api.post('/accounts', accountData);
        this.fetchAccounts();
      } catch (error) {
        console.error(error);
      }
    },
    async deleteAccount(accountId) {
      try {
        await api.delete(`/accounts/${accountId}`);
        this.fetchAccounts();
      } catch (error) {
        console.error(error);
      }
    }
  }
});
