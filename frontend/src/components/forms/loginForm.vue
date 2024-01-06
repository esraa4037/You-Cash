<template>
  <v-form @submit.prevent="login" class="login-form pt-10 py-5 px-10">
    <h2 class="mb-5">Login</h2>
    <v-text-field
      v-model="credentials.phone_num"
      label="Phone Number"
      required
    ></v-text-field>
    <v-text-field
      v-model="credentials.password"
      label="Password"
      type="password"
      required
    ></v-text-field>
    <v-btn class="main-btn" color="#20906c" type="submit">Login</v-btn>
    <v-alert
      v-if="authStore.showAlertLogin"
      color="error"
      icon="$error"
      :text="authStore.alert"
      closable
      class="py-2 mt-5"
    ></v-alert>
  </v-form>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/store/authStore";

const authStore = useAuthStore();

const credentials = ref({
  phone_num: "",
  password: "",
});

async function login() {
  await authStore.loginUser(credentials.value);
}
</script>

<style scoped>
.login-form {
  background-color: #fff;
  border: 1px solid #ccc;
  box-shadow: 0.1rem 0.1rem 0.6rem 0 #aaa;
  border-radius: 5px;
}
</style>
