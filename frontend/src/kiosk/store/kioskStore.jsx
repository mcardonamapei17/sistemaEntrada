//manejo de estados y el flujo de la aplicacion, que va a que, donde va a donde y que paso se va a seguir

import {create} from 'zustand';
import { BuscarDocumentos } from '../../api/attendanceApi';

export const useKioskStore = create((set,get)=>({
    //base
    satus: 'idle',

    loading: false,
    error: null,
    mensaje: null,

    //data
    usuario: null,
    empresa: null,
    tipo: null, //empleado o externo
    entradaAbierta: false,
    registroAbierto: null,

    //acciones
    reset: () =>
        set({
            status: "idle",
            loading:false,
            error: null,
            mensaje: null,
            usuario:null,
            empresa:null,
            tipo:null,
            entradaAbierta:false,
            registroAbierto:null
        }),
    
    buscarPorDocumento: async (documento) => {
    console.log("🔍 Iniciando búsqueda para:", documento);
    set({ loading: true, error: null, mensaje: null });

    try {
        const response = await BuscarDocumentos(documento);
        console.log("✅ Respuesta de Django:", response); // <--- LOG CLAVE

        if (!response.existe) {
            console.warn("⚠️ El usuario no existe en la base de datos");
            set({
                status: 'not_found',
                loading: false,
                // ... resto de nulos
            });
            return;
        }

        const { usuario, entrada_abierta, registro } = response;
        
        // Log para ver el tipo de dato de entrada_abierta
        console.log("🤔 ¿Tiene entrada abierta?:", entrada_abierta, " Tipo:", typeof entrada_abierta);

        const nextStatus = entrada_abierta ? 'salida' : 'entrada';
        console.log("🚀 Próximo paso:", nextStatus);

        set({
            status: nextStatus,
            loading: false,
            usuario,
            empresa: response.empresa,
            tipo: response.tipo,
            entradaAbierta: entrada_abierta, // Asegúrate de que el nombre coincida con tu estado
            registroAbierto: registro,
        });
    } catch (err) {
        console.error("❌ Error en la petición:", err);
        set({
            loading: false,
            error: 'Error al obtener el documento',
        });
    }
},

    // En useKioskStore
    marcarCompletado: async (mensaje = "Operación realizada correctamente") => {
        // 1. Mostramos el mensaje de éxito
        set({ 
            status: 'done', 
            mensaje,
            loading: false 
        });

        // 2. Esperamos 3 segundos (tiempo ideal para lectura en Kiosko)
        await new Promise(resolve => setTimeout(resolve, 3000));

        // 3. Limpiamos todo usando la acción reset que ya tienes
        get().reset();
    },
}));