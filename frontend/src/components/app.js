import axios from "axios";

// Cambiá el host si Flask está en otra máquina o puerto
const API_URL = "http://localhost:5000";

export const getIngles = () => axios.get(`${API_URL}/ingles`);
export const postIngles = (data) => axios.post(`${API_URL}/ingles`, data);
export const putIngles = (id, data) => axios.put(`${API_URL}/ingles/${id}`, data);
export const deleteIngles = (id) => axios.delete(`${API_URL}/ingles/${id}`);
