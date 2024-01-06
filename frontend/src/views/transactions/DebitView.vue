<template>
  <v-container class="mt-16">
    <v-row align="center" justify="center">
      <v-col cols="12" lg="5" sm="7" md="6">
        <v-form
          @submit.prevent="submit"
          class="pt-10 py-5 px-10"
          style="box-shadow: 0.1rem 0.1rem 0.5rem #aaa; border-radius: 5px"
        >
          <h2 class="mb-5">Debit</h2>
          <v-text-field
            v-model="debitData.amount"
            label="Amount"
            required
          ></v-text-field>
          <v-text-field
            v-model="debitData.password"
            label="Password"
            type="password"
            required
          ></v-text-field>
          <v-btn class="main-btn" color="#20906c" type="submit">Debit</v-btn>
          <v-alert
            v-if="transactionStore.showAlertDebit"
            :color="transactionStore.alertType"
            :icon="`$${transactionStore.alertType}`"
            :text="transactionStore.alert"
            closable
            class="py-2 mt-5"
          ></v-alert>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useTransactionStore } from "@/store/transactionStore";

const transactionStore = useTransactionStore();
const debitData = ref({
  amount: "",
  password: "",
});

function submit() {
  transactionStore.debit(debitData.value);
  // Clear input fields
  debitData.value.amount = "";
  debitData.value.password = "";
}
</script>
