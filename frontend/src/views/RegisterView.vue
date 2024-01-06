<template>
  <v-container class="my-10">
    <v-row align="center" justify="center">
      <v-col cols="12" lg="5" sm="7" md="6">
        <v-form
          @submit.prevent="register"
          class="pt-10 py-5 px-10"
          style="box-shadow: 0.1rem 0.1rem 0.6rem 0 #aaa; border-radius: 5px"
        >
          <h2 class="mb-5">Sign Up</h2>
          <v-text-field
            v-model="inputData.first_name"
            label="First Name"
            required
          >
          </v-text-field>
          <v-text-field
            v-model="inputData.last_name"
            label="Last Name"
            required
          ></v-text-field>
          <v-text-field
            v-model="inputData.phone_num"
            label="Phone Number"
            required
          ></v-text-field>
          <v-text-field
            v-model="inputData.username"
            label="Username"
            type="Username"
            required
          ></v-text-field>
          <v-text-field
            v-model="inputData.email"
            label="Email"
            type="email"
            required
          ></v-text-field>
          <v-text-field
            v-model="inputData.password"
            label="Password"
            type="password"
            required
          >
          </v-text-field>
          <v-btn class="main-btn" color="#20906c" type="submit">
            Sign Up
          </v-btn>
          <v-alert
            v-if="authStore.showAlertRegister"
            color="error"
            icon="$error"
            :text="authStore.alert"
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
import { useAuthStore } from "@/store/authStore";

const authStore = useAuthStore();

const inputData = ref({
  first_name: "",
  last_name: "",
  phone_num: "",
  username: "",
  email: "",
  password: "",
});

function register() {
  authStore.registerUser(inputData.value);
}
</script>
