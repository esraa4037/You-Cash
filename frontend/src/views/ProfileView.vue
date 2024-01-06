<template>
  <!-- User Profile Data -->
  <v-container class="mt-10">
    <h1 class="heading-tertiary mb-4">Personal Info</h1>
    <AccountData :accountData="accountData" />
  </v-container>

  <!-- <button @click="logoutAllDevices">Logout From All Devices</button> -->

  <!-- Transaction History -->
  <v-container v-if="transactionHistory.length" class="mt-7">
    <h1 class="heading-tertiary mb-4">Transaction History</h1>
    <TransactionHistory :transactionHistory="transactionHistory" />
  </v-container>

  <!-- If there is no transactions -->
  <v-container v-else class="mt-16">
    <h1 class="heading-tertiary mb-4">Transaction History</h1>
    <div class="img-container">
      <h1 class="empty-title">No Transactions</h1>
      <img class="empty-img" src="@/assets/empty_result.png" />
    </div>
  </v-container>
</template>

<script setup>
import AccountData from "@/components/profile/AccountData.vue";
import TransactionHistory from "@/components/profile/TransactionHistory.vue";
import { useAccountStore } from "@/store/accountStore";
// import { useAuthStore } from "@/store/authStore";
import { ref, onMounted } from "vue";

const accountStore = useAccountStore();
// const authStore = useAuthStore();

const accountData = ref({});
const transactionHistory = ref([]);

// function logoutAllDevices() {
//   authStore.logoutFromAllDevices();
// }

// Get account details and transaction history on mounted
onMounted(async () => {
  // Account Details
  await accountStore.getAccoutDetails();
  accountData.value = accountStore.accountData;

  // Transaction History
  await accountStore.getTransactionHistory();
  transactionHistory.value = accountStore.transactionHistory;
});

// Using Options API
// import { transactionsModule } from "@/store/transactions";
// import { mapActions } from "pinia";
// import { mapState } from "pinia";

// export default {
//   components: {
//     TransactionHistory,
//   },
//   computed: {
//     ...mapState(transactionsModule, ["transactionHistory"]),
//   },
//   methods: {
//     ...mapActions(transactionsModule, ["getTransactionHistory"]),
//   },
//   async mounted() {
//     await this.getTransactionHistory();
//   },
// };
</script>

<style scoped>
.profile-details {
  display: flex;
  justify-content: start;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.profile-details h2 {
  font-size: 1.2rem;
  color: #444;
}

.profile-details p {
  font-size: 1rem;
  color: #666666;
}

.img-container {
  text-align: center;
}

.empty-title {
  color: #aaa;
}

.empty-img {
  width: 40%;
}
</style>
