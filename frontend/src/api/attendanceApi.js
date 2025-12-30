//registro de asistencia
import apiClient from "./apiClient";

//buscar el usuario por documentos

export const BuscarDocumentos = async(documento) => {
    const response = await apiClient.get(
        "/registro-horas/buscar-documento/",{
        params: {documento},
    }
    );
    return response.data;
};

//registrar entrada
export const RegistrarEntrada = async(payload) => {
    const response = await apiClient.post(
        "/registro-horas/entrada/",
        payload

    );
    return response.data;
};

//registrar salida
export const RegistrarSalida = async(payload) => {
    const response = await apiClient.post(
        "/registro-horas/salida/",
        payload
    );
    return response.data;
};

