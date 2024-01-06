class TokenService {
  setToken = (token) => {
    localStorage.setItem("token", token);
  };

  getToken = () => {
    return localStorage.getItem("token");
  };

  removeToken = () => {
    localStorage.removeItem("token");
  };

  setAccountId = (accountId) => {
    localStorage.setItem("accountId", accountId);
  };

  getAccountId = () => {
    return localStorage.getItem("accountId");
  };

  removeAccountId = () => {
    localStorage.removeItem("accountId");
  };

  setIsLoggedIn = (isLogedIn) => {
    localStorage.setItem("isLogedIn", JSON.stringify(isLogedIn));
  };

  getIsLoggedIn = () => {
    const isLoggedIn = localStorage.getItem("isLogedIn");
    return JSON.parse(isLoggedIn);
  };
}

export default new TokenService();
