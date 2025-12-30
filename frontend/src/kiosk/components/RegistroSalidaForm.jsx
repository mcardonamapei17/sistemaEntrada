import { useState } from "react";
import { Button, Stack, Typography, Alert } from "@mui/material";

import { RegistrarSalida } from "../../api/attendanceApi";
import { useKioskStore } from "../store/kioskStore";

export default function RegistroSalidaForm() {
  const {
    usuario,
    registroAbierto,
    reset,
  } = useKioskStore();

  const [loading, setLoading] = useState(false);
  const [mensaje, setMensaje] = useState(null);
  const [error, setError] = useState(null);

  if (!usuario || !registroAbierto) return null;

  const handleSalida = async () => {
    setLoading(true);
    setError(null);

    try {
      const resp = await RegistrarSalida({
        usuario_id: usuario.id,
      });

      setMensaje(`Salida registrada a las ${resp.hora_salida}`);

      // Reset automático después de unos segundos
      setTimeout(() => {
        reset();
      }, 3000);
    } catch (err) {
      setError("Error registrando la salida");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Stack spacing={3} mt={4} alignItems="center">
      <Typography variant="h6">
        ¿Desea registrar su salida?
      </Typography>

      {mensaje && <Alert severity="success">{mensaje}</Alert>}
      {error && <Alert severity="error">{error}</Alert>}

      <Button
        variant="contained"
        color="error"
        size="large"
        onClick={handleSalida}
        disabled={loading}
        sx={{ minWidth: 220, minHeight: 60 }}
      >
        {loading ? "Registrando..." : "Registrar salida"}
      </Button>
    </Stack>
  );
}
