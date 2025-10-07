import axios from "axios";

// URL base de tu backend
const BASE_URL = "http://localhost:5000";

// --- Funciones para Inglés ---
export const getIngles = () => {
  return axios.get(`${BASE_URL}/ingles`);
};

export const postIngles = (apunte) => {
  return axios.post(`${BASE_URL}/ingles`, apunte);
};

// --- Función genérica para cualquier materia (opcional) ---
export const getApuntes = (materia) => {
  return axios.get(`${BASE_URL}/${materia}`);
};

export const postApunte = (materia, apunte) => {
  return axios.post(`${BASE_URL}/${materia}`, apunte);
};
