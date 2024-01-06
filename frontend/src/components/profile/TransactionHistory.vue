<template>
  <!-- Transaction History -->
  <v-container>
    <v-row class="overflow">
      <table class="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Amount</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="transaction in props.transactionHistory"
            :key="transaction.id"
          >
            <td>{{ transaction.id }}</td>
            <td>{{ transaction.transaction_type }}</td>
            <td>{{ transaction.amount }}</td>
            <td>{{ formatDateString(transaction.transaction_date) }}</td>
          </tr>
        </tbody>
      </table>
    </v-row>
  </v-container>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  transactionHistory: {
    type: Array,
    required: true,
  },
});

// Function to format the date string
const formatDateString = (dateString) => {
  const date = new Date(dateString);
  const formattedDate = date.toLocaleString("en-US", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });

  return formattedDate;
};

// Using Options API
// export default {
//   props: {
//     transactionHistory: {
//       type: Array,
//     },
//   },
//   mounted() {
//     console.log(this.transactionHistory);
//   },
// };
</script>

<style scoped>
.overflow {
  overflow-x: scroll;
}

.table {
  width: 100%;
  font-size: 1rem;
  background-color: #f9f9f9;

  border-spacing: 0;
  border-radius: 9px;
}

.table th:first-child {
  border-top-left-radius: 9px;
}

.table th:last-child {
  border-top-right-radius: 9px;
}

.table th,
.table td {
  padding: 1rem;
  text-align: left;
}

.table thead th {
  font-size: 1.2rem;
  font-weight: bold;
  background-color: #20906c;
  color: #ffffff;
}

.table tbody tr:nth-child(even) {
  background-color: #f2f2f2;
}

.table tbody tr:hover {
  background-color: #d4e9e2;
}
</style>
