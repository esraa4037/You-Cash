<template>
  <div class="layout">
    <v-layout>
      <AppNav />
      <v-main>
        <slot></slot>
      </v-main>
      <!-- <AppFooter /> -->
    </v-layout>
  </div>
</template>

<script>
import AppNav from "@/components/global/AppNav.vue";
// import AppFooter from "@/components/global/AppFooter.vue";

export default {
  components: {
    AppNav,
    // AppFooter,
  },
};
</script>
