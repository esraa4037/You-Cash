<template>
  <app-layout>
    <router-view />
  </app-layout>
</template>

<script>
import AppLayout from "@/components/global/AppLayout.vue";
export default {
  components: {
    AppLayout,
  },
};
</script>

<style lang="scss">
#app {
  font-family: sans-serif;
  color: #333;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #333;

    &.router-link-exact-active {
      color: #20906c;
    }
  }
}

.main-btn {
  background-color: #20906c !important;
  font-family: inherit !important;
  letter-spacing: inherit !important;
  text-transform: none !important;
  font-size: inherit !important;

  border-radius: 3px !important;
  font-weight: bold !important;
  color: #fff !important;
}
h1,
h2,
h3,
.sub-heading {
  color: #333;
  font-weight: 700;
  letter-spacing: -0.05rem;
}

.sub-heading {
  font-size: 1.8rem;
  line-height: 1.2;
  margin-bottom: 1rem;
}

.border-bottom {
  width: 70px;
  border-bottom: solid 6px #20906c;
  margin-bottom: 2rem;
}
</style>
