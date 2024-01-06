import { watch, ref, onMounted } from "vue";
import TokenService from "@/store/tokenService";

export default function (initialValue) {
  const isLoggedIn = ref(initialValue);

  onMounted(() => {
    const storageIsLoggedIn = TokenService.getIsLoggedIn() || false;
    if (storageIsLoggedIn) {
      isLoggedIn.value = storageIsLoggedIn;
    }

    watch(isLoggedIn, (newValue) => {
      TokenService.setIsLoggedIn(newValue);
    });
  });
  return isLoggedIn;
}
