<template>
  <v-container class="mt-16">
    <v-row align="center" justify="center">
      <v-col cols="12" lg="5" sm="7" md="6">
        <LoginForm />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import LoginForm from "@/components/forms/loginForm.vue";
</script>
