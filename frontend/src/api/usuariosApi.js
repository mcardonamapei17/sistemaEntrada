// src/api/usuarios.api.js
import apiClient from "./apiClient";

export const getUsuarios = async (params = {}) => {
  const response = await apiClient.get("/usuario/usuarios/", {
    params,
  });
  return response.data;
};

export const getUsuarioById = async (id) => {
  const response = await apiClient.get(`/usuario/usuarios/${id}/`);
  return response.data;
};

export const crearUsuario = async (payload) => {
  const response = await apiClient.post(
    "/usuario/usuarios/",
    payload
  );
  return response.data;
};

export const actualizarUsuario = async (id, payload) => {
  const response = await apiClient.put(
    `/usuario/usuarios/${id}/`,
    payload
  );
  return response.data;
};
