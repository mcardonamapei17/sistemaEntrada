import {useState, useEffect, useRef} from 'react';
import {
    TextField,
    Button,
    Box,
    Typography,
    CircularProgress
} from '@mui/material';

const DocumentoInput = ({onBuscar, loading, error}) => {
    const [documento, setDocumento] = useState('');
    const inputRef = useRef(null);

    //auto focus permanente (para el modo kiosko)
    useEffect(() => {
        inputRef.current?.focus();
    },[]);

    const HandleBuscar = () => {
        if(!documento.trim())return;
        onBuscar(documento.trim());
    };

    const HandleKeyDown = (e) => {
        if (e.key === 'Enter'){
            HandleBuscar();
        }
    };

    //ahora si el codigo del boton
    return (
        <Box
        sx={{
            maxWidth: 400,
            mx: 'auto',
            mt: 8,
            textAlign: 'center'
        }}>
            <Typography variant="h5" gutterBottom>
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
            helperText={error ? 'Error al buscar el documento' : ''}
            sx={{mb:2}}
            inputProps={{
                style: {
                    fontSize: 24,
                    textAlign: "center"
                }
            }}>
            </TextField>
            <Button
            fullWidth
            size='large'
            variant='contained'
            onClick={HandleBuscar}
            disabled={loading}>
                {loading ? <CircularProgress size={24} />: "Continuar"}
            </Button>
        </Box>
    );
};

export default DocumentoInput;