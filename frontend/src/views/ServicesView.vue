<template>
  <v-container class="w-75 mt-7">
    <!-- Title -->
    <v-container>
      <h3 class="sub-heading">Services</h3>
      <div class="border-bottom"></div>
    </v-container>

    <!-- Services Cards -->
    <v-row justify="center">
      <v-col cols="12" lg="3" sm="7" md="3" class="mx-2">
        <router-link
          @click.prevent="showLoginModal"
          :to="{ name: 'Credit' }"
          class="transaction-card"
        >
          <img src="@/assets/credit.png" alt="add-money" />
          <p>Credit</p>
        </router-link>
      </v-col>

      <v-col cols="12" lg="3" sm="7" md="3" class="mx-2">
        <router-link
          @click.prevent="showLoginModal"
          :to="{ name: 'Debit' }"
          class="transaction-card"
        >
          <img src="@/assets/debit.png" alt="request-money" />
          <p>Debit</p>
        </router-link>
      </v-col>

      <v-col cols="12" lg="3" sm="7" md="3" class="mx-2">
        <router-link
          @click.prevent="showLoginModal"
          :to="{ name: 'Transfer' }"
          class="transaction-card"
        >
          <img src="@/assets/transfer_money.png" alt="transfer-money" />
          <p>Transfer</p>
        </router-link>
      </v-col>
    </v-row>

    <!-- Login Modal -->
    <v-row v-if="showModal" align="center" justify="center">
      <v-col class="modal" cols="12" lg="4" sm="7" md="6">
        <LoginForm class="modal" />
      </v-col>
    </v-row>
    <div v-if="showModal" class="overlay" @click="closeModal"></div>
  </v-container>
</template>

<script setup>
import LoginForm from "@/components/forms/loginForm.vue";
import { ref } from "vue";

const isLoggedIn = ref(false);
const showModal = ref(false);

function showLoginModal() {
  if (!isLoggedIn.value) {
    showModal.value = true;
  }
}

function closeModal() {
  showModal.value = false;
}
</script>

<style scoped>
.transaction-card:link,
.transaction-card:visited {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1.8rem;

  text-decoration: none;
  font-size: 1.2rem;
  font-weight: 500;
  color: #20906c;

  padding: 2rem 3.5rem;
  border: solid 1px #eee;
  border-radius: 4px;
  box-shadow: 0 0.5rem 0.7rem rgba(0, 0, 0, 0.2);
  transition: all 0.3s;
}

.transaction-card:hover,
.transaction-card:active {
  transform: translateY(-3px);
  box-shadow: 0 0.9rem 2.5rem rgba(0, 0, 0, 0.17);
}

/* MODAL */
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;

  z-index: 10;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(3px);
  z-index: 5;
}

.close-modal {
  position: absolute;
  top: 1.2rem;
  right: 2rem;
  font-size: 2rem;
  color: #333;
  cursor: pointer;
  border: none;
  background: none;
}
</style>
