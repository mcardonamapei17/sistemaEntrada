//no endpoints solo headers errores y manejo de jwt a futuro
import axios from 'axios';

const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    timeout: 3000,
    headers: {
        'Content-Type': 'application/json',
    },
});

//futuro api key y jwt para admin (acuerdeme de poner esta monda)
apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token){
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

//respuesta del interceptor
apiClient.interceptors.response.use(
    (response) => response,
    (error) => {
        const message = error.response?.data?.detail || error.response?.data?.message || "Error de conexion con el servidor";

        return Promise.reject({
            status: error.response?.status,
            message,
            raw: error,
        });
    }
);

export default apiClient;