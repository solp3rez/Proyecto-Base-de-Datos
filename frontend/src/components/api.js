import axios from "axios";

// URL base de tu backend (ajustala si tu backend corre en otro puerto)
const BASE_URL = "http://localhost:5000";

// INGLES
export const getIngles = () => {
  return axios.get(`${BASE_URL}/ingles`);
};

export const postIngles = (apunte) => {
  return axios.post(`${BASE_URL}/ingles`, apunte);
};
