import { createRouter, createWebHistory } from "vue-router";
import TokenService from "@/store/tokenService";
import CreditView from "@/views/transactions/CreditView.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/HomeView"),
    meta: {
      title: "Home",
    },
  },
  {
    path: "/services",
    children: [
      {
        path: "",
        name: "Services",
        component: () => import("@/views/ServicesView"),
        meta: {
          title: "Services",
        },
      },
      {
        path: "credit",
        name: "Credit",
        component: CreditView,
        meta: {
          title: "Services | Credit",
        },
      },
      {
        path: "debit",
        name: "Debit",
        component: () => import("@/views/transactions/DebitView"),
        meta: {
          title: "Services | Debit",
        },
      },
      {
        path: "transfer",
        name: "Transfer",
        component: () => import("@/views/transactions/TransferView"),
        meta: {
          title: "Services | Transfer",
        },
      },
    ],
  },

  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/LoginView"),
    meta: {
      title: "Login",
    },
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("@/views/RegisterView"),
    meta: {
      title: "Register",
    },
  },
  {
    path: "/profile",
    name: "Profile",
    component: () => import("@/views/ProfileView"),
    meta: {
      title: "My Profile",
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: routes,
});

router.beforeEach((to, from, next) => {
  // Check if the user is navigating to the login or register page
  if (to.name === "Login" || to.name === "Register") {
    // Check if the user is already logged in
    if (TokenService.getToken()) {
      // If the user is already logged in, redirect to the home page
      next({ name: "Home" });
    } else {
      // If the user is not logged in, allow navigation to the login page
      next();
    }
  } else if (
    to.name === "Profile" ||
    to.name === "Credit" ||
    to.name === "Debit" ||
    to.name === "Transfer"
  ) {
    // Check if the user isn't logged in
    if (!TokenService.getToken()) {
      // If the user isn't logged in, remain the user in the same page
      next(false);
    } else {
      // If the user is logged in, allow navigation
      next();
    }
  } else {
    // For all other pages, allow navigation
    document.title = "YouCash | " + to.meta.title;
    next();
  }
});

export default router;
