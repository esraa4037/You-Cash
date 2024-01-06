import { defineStore } from "pinia";
import { authenticatedInstance } from "@/store/axios";

export const useTransactionStore = defineStore("transactionStore", {
  state: () => ({
    showCreditAlert: false,
    showDebitAlert: false,
    showTransAlert: false,
    alertColor: "",
    alertMessage: "",
  }),
  getters: {
    alert: (state) => state.alertMessage,
    showAlertCrdit: (state) => state.showCreditAlert,
    showAlertDebit: (state) => state.showDebitAlert,
    showAlertTrans: (state) => state.showTransAlert,
    alertType: (state) => state.alertColor,
  },
  actions: {
    async credit(creditData) {
      if (creditData.amount && creditData.password) {
        try {
          const response = await authenticatedInstance.post(
            "transactions/credit",
            creditData
          );
          this.setAlertMessage(response);
          this.alertColor = "success";
        } catch (error) {
          this.setAlertMessage(error.response);
          this.alertColor = "error";
        }
        this.showCreditAlert = true;
      }
    },

    async debit(debitData) {
      if (debitData.amount && debitData.password) {
        try {
          const response = await authenticatedInstance.post(
            "transactions/debit",
            debitData
          );
          this.setAlertMessage(response);
          this.alertColor = "success";
        } catch (error) {
          this.setAlertMessage(error.response);
          this.alertColor = "error";
        }
        this.showDebitAlert = true;
      }
    },

    async transfer(transferData) {
      if (transferData.to && transferData.amount && transferData.password) {
        try {
          const response = await authenticatedInstance.post(
            "transactions/transfer",
            transferData
          );
          this.setAlertMessage(response);
          this.alertColor = "success";
        } catch (error) {
          this.setAlertMessage(error.response);
          this.alertColor = "error";
        }
        this.showTransAlert = true;
      }
    },

    setAlertMessage(response) {
      if (response.status === 201) {
        this.alertMessage = "Success Transaction";
      } else if (response.status === 400) {
        this.alertMessage = response.data.detail;
      } else {
        this.alertMessage = "Something went wrong";
      }
    },
  },
});
