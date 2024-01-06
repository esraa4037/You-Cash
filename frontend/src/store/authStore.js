import { defineStore } from "pinia";
import axiosInstance from "@/store/axios";
import { authenticatedInstance } from "@/store/axios";
import TokenService from "@/store/tokenService";

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    alertMessage: "",
    showLoginAlert: false,
    showRegisterAlert: false,
  }),
  getters: {
    alert: (state) => state.alertMessage,
    showAlertLogin: (state) => state.showLoginAlert,
    showAlertRegister: (state) => state.showRegisterAlert,
  },

  actions: {
    async registerUser(accountData) {
      if (
        accountData.first_name &&
        accountData.last_name &&
        accountData.phone_num &&
        accountData.username &&
        accountData.email &&
        accountData.password
      ) {
        try {
          const response = await axiosInstance.post(
            "accounts/register",
            accountData
          );

          // Login user if the account created successfully
          if (response.status == 200) {
            const credentials = {
              phone_num: accountData.phone_num,
              password: accountData.password,
            };
            try {
              this.loginUser(credentials);
            } catch {
              //
            }
          }
        } catch (error) {
          if (error.response.data.username?.[0]) {
            this.alertMessage = error.response.data.username?.[0];
          } else if (error.response.data.email?.[0]) {
            this.alertMessage = error.response.data.email?.[0];
          } else if (error.response?.data?.phone_num?.[0]) {
            this.alertMessage = error.response?.data?.phone_num?.[0];
          } else {
            console.log(error.response.data);
          }
          this.showRegisterAlert = true;
        }
      }
    },

    async loginUser(credentials) {
      // phone_num: 01111111111
      if (credentials.phone_num && credentials.password) {
        try {
          const response = await axiosInstance.post(
            "accounts/login",
            credentials
          );

          // Save token and id in the local storage
          TokenService.setToken(response.data.token);
          TokenService.setAccountId(response.data.account.id);
          TokenService.setIsLoggedIn(true);

          // Refresh the page
          window.location.reload();
        } catch (error) {
          if (error.response?.data?.detail) {
            this.alertMessage = error.response?.data?.detail;
          } else {
            this.alertMessage = "Something went wrong!";
          }
          this.showLoginAlert = true;
        }
      }
    },

    async logoutUser() {
      TokenService.removeToken();
      TokenService.removeAccountId();
      TokenService.setIsLoggedIn(false);

      // Refresh the page
      window.location.reload();
    },

    async logoutFromAllDevices() {
      try {
        const res = await authenticatedInstance.post("accounts/logout");
        console.log(res);

        TokenService.removeToken();
        TokenService.removeAccountId();
        TokenService.setIsLoggedIn(false);

        // Refresh the page
        window.location.reload();
      } catch {
        //
      }
    },
  },
});

// Using Options API
// export const authStore = defineStore("authStore", {
//   state: () => ({
//     first_name: "",
//     second_name: "",
//     phone_num: "",
//     email: "",
//     password: "",
//     token: "",
//     // is_authenticated: false,
//   }),

//   actions: {
//     async signUp(first_name, second_name, phone_num, email, password) {
//       await axios
//         .post("register", {
//           first_name,
//           second_name,
//           phone_num,
//           email,
//           password,
//         })
//         .then((response) => {
//           this.first_name = response.data.first_name;
//           this.second_name = response.data.second_name;
//           this.phone_num = response.data.hone_num;
//           this.password = response.data.ssword;
//         })
//         .catch((err) => console.log(err));
//     },

//     async login() {
//       // await axios
//       //   .get("api/user")
//       //   .then((response) => (this.token = response.data.token))
//       //   .catch((err) => console.log(err));
//     },
//   },
// });
