import { defineStore } from "pinia";
import { authenticatedInstance } from "@/store/axios";
import tokenService from "./tokenService";
import { ref } from "vue";

export const useAccountStore = defineStore("accountStore", {
  state: () => ({
    transactionHistory: ref([]),
    accountData: ref({}),
  }),
  actions: {
    async getTransactionHistory() {
      const accountId = tokenService.getAccountId();
      try {
        const response = await authenticatedInstance.get(
          `accounts/${accountId}/transaction-history`
        );
        this.transactionHistory = response.data.list;
      } catch (error) {
        this.console.log(error.response);
      }
    },

    async getAccoutDetails() {
      const accountId = tokenService.getAccountId();
      try {
        const response = await authenticatedInstance.get(
          `accounts/${accountId}/`
        );
        this.accountData = response.data.account;
      } catch (error) {
        this.console.log(error.response);
      }
    },
  },
});
