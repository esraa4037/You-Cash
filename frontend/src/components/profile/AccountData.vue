<template>
  <v-container>
    <v-row>
      <v-col lg="8" sm="12" class="mx-2 account-card">
        <v-row>
          <v-col sm="4">
            <h4 class="title">First Name</h4>
          </v-col>
          <v-col sm="8">
            <p>{{ props.accountData.first_name }}</p>
          </v-col>
        </v-row>
        <hr color="#eee" size="1px" />

        <v-row>
          <v-col sm="4">
            <h4 class="title">Last Name</h4>
          </v-col>
          <v-col sm="8">
            <p>{{ props.accountData.last_name }}</p>
          </v-col>
        </v-row>
        <hr color="#eee" size="1px" />

        <v-row>
          <v-col sm="4">
            <h4 class="title">Username</h4>
          </v-col>
          <v-col sm="8">
            <p>{{ props.accountData.username }}</p>
          </v-col>
        </v-row>
        <hr color="#eee" size="1px" />

        <v-row>
          <v-col sm="4">
            <h4 class="title">Email</h4>
          </v-col>
          <v-col sm="8">
            <p>{{ props.accountData.email }}</p>
          </v-col>
        </v-row>
        <hr color="#eee" size="1px" />

        <v-row>
          <v-col sm="4">
            <h4 class="title">Phone Number</h4>
          </v-col>
          <v-col sm="8">
            <p>{{ props.accountData.phone_num }}</p>
          </v-col>
        </v-row>
        <hr color="#eee" size="1px" />

        <v-row>
          <v-col sm="4">
            <h4 class="title">Balance</h4>
          </v-col>
          <v-col sm="8">
            <p>{{ props.accountData.balance }}</p>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  accountData: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
.account-card {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
  padding: 1.5rem 2.7rem;
  border: solid 1px #ccc;
  border-radius: 4px;
  box-shadow: 0 0.2rem 0.5rem rgba(0, 0, 0, 0.1);
}

.title {
  color: #20906c;
}
</style>
