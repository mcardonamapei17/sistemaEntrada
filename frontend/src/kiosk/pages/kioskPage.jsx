import { Container, Stack, Typography, Alert, Box } from "@mui/material";
import DocumentoInput from "../components/DocumentoInput";
import { useKioskStore } from "../store/kioskStore";
import UsuarioResumen from "../components/UsuarioResumen";
import RegistroEntradaForm from "../components/RegistroEntradaForm"; // Importa el nuevo componente
import RegistroSalidaForm from "../components/RegistroSalidaForm";

export default function KioskPage() {
  const { status, error, mensaje, entradaAbierta } = useKioskStore();

  return (
    <Container maxWidth="sm" sx={{ mt: 6, mb: 6 }}>
      <Stack spacing={3}>
        <Typography variant="h5" align="center" fontWeight="bold">
          Registro de Entrada / Salida
        </Typography>

        {/* 1. Buscador: Siempre visible a menos que ya se haya completado la operación */}
        {status !== "done" && <DocumentoInput />}

        {/* 2. Alertas de Error o No Encontrado */}
        {error && <Alert severity="warning">{error}</Alert>}
        {status === "not_found" && (
          <Alert severity="info">
            Usuario no registrado. Debe crear el registro en la oficina.
          </Alert>
        )}

        {/* 3. Resumen del Usuario: Aparece cuando se encuentra (entrada o salida) */}
        {(status === "entrada" || status === "salida") && (
          <Box>
            <UsuarioResumen />
            
            {/* 4. Formulario de Entrada: Solo si el status es 'entrada' (es decir, está afuera) */}
            {status === "entrada" && !entradaAbierta && (
              <RegistroEntradaForm />
            )}

            {/* Aquí podrías poner el componente de Salida si status === 'salida' */}
            {status === "salida" && entradaAbierta && (
                <RegistroSalidaForm />
            )}
          </Box>
        )}

        {/* 5. Mensaje de Éxito Final */}
        {status === "done" && (
          <Stack spacing={2} alignItems="center">
            <Alert severity="success" sx={{ width: '100%' }}>{mensaje}</Alert>
            <Button variant="outlined" onClick={() => window.location.reload()}>
              Finalizar
            </Button>
          </Stack>
        )}

        <Typography variant="body2" align="center" color="text.secondary">
          Siga las instrucciones en pantalla
        </Typography>
      </Stack>
    </Container>
  );
}