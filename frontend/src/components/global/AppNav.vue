<template>
  <div class="nav-bar">
    <v-app-bar :class="{ 'nav-open': navOpen }">
      <v-container>
        <v-row class="d-flex align-center">
          <v-col cols="3">
            <div class="logo">
              <span style="color: #20906c">You</span>
              <span>Cash</span>
            </div>
          </v-col>

          <v-col cols="9" class="main-nav">
            <v-col cols="4" class="d-flex align-center">
              <ul
                class="links d-flex align-center"
                style="list-style: none; gap: 2rem"
              >
                <li>
                  <router-link class="main-nav-link" :to="{ name: 'Home' }">
                    Home
                  </router-link>
                </li>
                <li>
                  <router-link class="main-nav-link" :to="{ name: 'Services' }">
                    Services
                  </router-link>
                </li>
              </ul>
            </v-col>
            <v-col
              v-if="isLoggedIn"
              class="d-flex justify-end align-center"
              style="gap: 2rem"
            >
              <!-- Logout -->
              <div
                class="d-flex align-center nav-link"
                style="gap: 4px; text-decoration: none"
              >
                <v-icon class="color">mdi-logout</v-icon>
                <div class="color main-nav-link" @click="logout">Logout</div>
              </div>

              <!-- My Profile -->
              <router-link
                class="d-flex align-center nav-link"
                style="gap: 4px; text-decoration: none"
                :to="{ name: 'Profile' }"
              >
                <v-icon class="color">mdi-account</v-icon>
                <div class="color main-nav-link">My Profile</div>
              </router-link>
            </v-col>
            <v-col
              v-else
              class="d-flex justify-end align-center"
              style="gap: 2rem"
            >
              <router-link
                :to="{ name: 'Login' }"
                class="d-flex align-center"
                style="gap: 4px; text-decoration: none"
              >
                <v-icon class="color">mdi-login</v-icon>
                <router-link class="color" :to="{ name: 'Login' }">
                  Login
                </router-link>
              </router-link>
              <v-btn class="main-btn">
                <router-link class="text-btn" :to="{ name: 'Register' }">
                  Register
                </router-link>
              </v-btn>
            </v-col>
          </v-col>
        </v-row>
      </v-container>

      <!-- Btn Mobile Nav -->
      <button class="btn-mobile-nav" @click="toggleMobileNav">
        <img src="@/assets/menu-icon.png" class="img-mobile-nav" name="menu" />
        <img
          src="@/assets/close-icon.png"
          class="img-mobile-nav"
          name="close"
        />
      </button>
    </v-app-bar>
    <!-- Mobile Nav -->
    <div :class="{ 'show-mobile-nav': navOpen }" class="mobile-navigation">
      <ul class="links mobile-nav-list">
        <li>
          <router-link
            class="main-nav-link"
            :to="{ name: 'Home' }"
            @click="toggleMobileNav"
          >
            Home
          </router-link>
        </li>
        <li>
          <router-link
            class="main-nav-link"
            :to="{ name: 'Services' }"
            @click="toggleMobileNav"
          >
            Services
          </router-link>
        </li>
        <v-col v-if="isLoggedIn" class="mobile-nav-list">
          <!-- Logout -->
          <div
            class="d-flex align-center nav-link"
            style="gap: 4px; text-decoration: none"
            @click="toggleMobileNav"
          >
            <v-icon class="color">mdi-logout</v-icon>
            <div class="color main-nav-link" @click="logout">Logout</div>
          </div>

          <!-- My Profile -->
          <router-link
            class="d-flex align-center nav-link"
            style="gap: 4px; text-decoration: none"
            :to="{ name: 'Profile' }"
            @click="toggleMobileNav"
          >
            <v-icon class="color">mdi-account</v-icon>
            <div class="color main-nav-link">My Profile</div>
          </router-link>
        </v-col>
        <v-col v-else class="mobile-nav-list">
          <router-link
            :to="{ name: 'Login' }"
            class="d-flex align-center"
            style="gap: 4px; text-decoration: none"
          >
            <v-icon class="color">mdi-login</v-icon>
            <router-link
              class="color"
              :to="{ name: 'Login' }"
              @click="toggleMobileNav"
            >
              Login
            </router-link>
          </router-link>
          <v-btn class="main-btn">
            <router-link
              class="text-btn"
              :to="{ name: 'Register' }"
              @click="toggleMobileNav"
            >
              Register
            </router-link>
          </v-btn>
        </v-col>
      </ul>
    </div>
  </div>
</template>

<script setup>
import useStorageIsLoggedIn from "@/composable/useStorageIsLoggedIn";
import { useAuthStore } from "@/store/authStore";
import { ref } from "vue";

const authStore = useAuthStore();
const isLoggedIn = useStorageIsLoggedIn(false);
const navOpen = ref(false);

function logout() {
  authStore.logoutUser();
}

function toggleMobileNav() {
  navOpen.value = !navOpen.value;
}
</script>

<style scoped>
.nav-bar {
  overflow-x: hidden;
}

.logo {
  font-size: 2rem;
  font-weight: bold;
}

.main-nav {
  display: flex;
  align-items: center;
}

.main-nav-link:link,
.main-nav-link:visited {
  display: inline-block;
  text-decoration: none;
  color: #333;
  font-weight: 500;
  font-size: 1.2rem;
  transition: all 0.3s;
}

.main-nav-link:hover,
.main-nav-link:active {
  color: #20906c;
  text-decoration: underline;
  cursor: pointer;
}

.color {
  color: #20906c;
}

.color:hover {
  color: #16684e;
}

.text-btn {
  color: #fff;
  text-decoration: none;
}

.btn-mobile-nav {
  cursor: pointer;
  border: none;
  background: none;
  margin-right: 1.2rem;

  display: none;
}

.img-mobile-nav[name="close"] {
  display: none;
}

.img-mobile-nav[name="menu"] {
  display: inline-block;
}

.img-mobile-nav {
  width: 24px;
}

.mobile-navigation {
  background-color: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;

  /* 1) Hide it visually */
  opacity: 0;

  /* 2) Make it unaccessible to mouse and keyboard */
  pointer-events: none;

  /* 3) Hide it from screen readers */
  visibility: hidden;

  transform: translateX(100%);

  transition: all 0.5s ease-in;
}

.mobile-nav-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  list-style: none;
  gap: 2rem;
}

/*************************/
/* BELOW 900px (Tablets) */
/*************************/
@media (max-width: 700px) {
  /* MOBILE NAVIGATION */
  .main-nav {
    display: none;
  }

  .btn-mobile-nav {
    display: block;
    z-index: 100;
  }

  .mobile-navigation .main-nav-link {
    font-size: 1.4rem;
  }

  .mobile-navigation.show-mobile-nav {
    z-index: 20;
    transform: translatex(0);

    opacity: 1;
    pointer-events: auto;
    visibility: visible;
  }
  .nav-open .img-mobile-nav[name="close"] {
    display: inline-block;
  }

  .nav-open .img-mobile-nav[name="menu"] {
    display: none;
  }
}
</style>
