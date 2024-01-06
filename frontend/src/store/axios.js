import axios from "axios";
import TokenService from "@/store/tokenService";

const BASE_URL = "http://localhost:8000/";
// const BASE_URL = "https://youcash.internship2023.et3.co/";
const axiosInstance = axios.create({
  baseURL: BASE_URL,
  headers: {},
});

const authenticatedInstance = axios.create({
  baseURL: BASE_URL,
  headers: {
    Authorization: `Token ${TokenService.getToken()}`,
  },
});

authenticatedInstance.interceptors.request.use((config) => {
  const token = TokenService.getToken();
  config.headers.Authorization = `Token ${token}`;
  return config;
});

export default axiosInstance;
export { authenticatedInstance };
