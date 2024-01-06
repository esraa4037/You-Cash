import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Pinia Config
import { createPinia } from "pinia";

// Emmiter Config
// import mitt from "mitt";
// const Emmiter = mitt();

// Axios
import "@/store/axios";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css";

const vuetify = createVuetify({
  components,
  directives,
});

createApp(App)
  .use(vuetify)
  .use(router)
  .use(createPinia())
  // .provide("Emmiter", Emmiter)
  .mount("#app");
