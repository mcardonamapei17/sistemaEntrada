import { useState, useEffect, useRef } from 'react';
import { TextField, Button, Box, Typography, CircularProgress } from '@mui/material';
import { useKioskStore } from '../store/kioskStore'; // Ajusta la ruta

const DocumentoInput = () => {
    const [documento, setDocumento] = useState('');
    const inputRef = useRef(null);

    // Extraemos todo de la tienda de Zustand
    const { buscarPorDocumento, loading, error, status } = useKioskStore();

    useEffect(() => {
        inputRef.current?.focus();
    }, []);

    // Limpiar el input si el status vuelve a idle o si hay éxito
    useEffect(() => {
        if (status === 'idle') setDocumento('');
    }, [status]);

    const HandleBuscar = () => {
        if (!documento.trim() || loading) return;
        buscarPorDocumento(documento.trim());
        console.log()
    };

    const HandleKeyDown = (e) => {
        if (e.key === 'Enter') HandleBuscar();
    };

    return (
        <Box sx={{ maxWidth: 600, mx: 'auto', mt: 8, textAlign: 'center' }}>
            <Typography variant="h4" gutterBottom>
                Ingrese su documento
            </Typography>

            <TextField
                inputRef={inputRef}
                fullWidth
                value={documento}
                onChange={(e) => setDocumento(e.target.value)}
                onKeyDown={HandleKeyDown}
                placeholder="Número de documento"
                disabled={loading}
                error={!!error}
                // Aquí usamos el error real que viene de Django/Store
                helperText={error || ''} 
                sx={{ mb: 2 }}
                inputProps={{
                    style: { fontSize: 24, textAlign: "center" }
                }}
                label="Número de documento"
                variant="outlined"
                color='primary'
                
            />
            
            <Button
                fullWidth
                size='large'
                variant='contained'
                onClick={HandleBuscar}
                disabled={loading || !documento.trim()}
            >
                {loading ? <CircularProgress size={24} color="inherit" /> : "Continuar"}
            </Button>
        </Box>
    );
};

export default DocumentoInput;