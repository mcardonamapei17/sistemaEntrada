// src/api/management.api.js
import apiClient from "./apiClient";

/* ===================== EMPRESAS ===================== */

export const getEmpresas = async () => {
  const response = await apiClient.get("/management/empresas/");
  return response.data;
};

export const crearEmpresa = async (payload) => {
  const response = await apiClient.post(
    "/management/empresas/",
    payload
  );
  return response.data;
};

/* ===================== SEDES ===================== */

export const getSedes = async () => {
  const response = await apiClient.get("/management/sedes/");
  return response.data;
};

/* ===================== ROLES ===================== */

export const getRoles = async () => {
  const response = await apiClient.get("/management/roles/");
  return response.data;
};
