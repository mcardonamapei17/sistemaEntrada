import { useEffect, useState } from "react";
import {
  Stack,
  TextField,
  Button,
  Typography,
  MenuItem,
  Checkbox,
  FormControlLabel,
  Alert,
} from "@mui/material";

import { RegistrarEntrada } from "../../api/attendanceApi";
import { getSedes } from "../../api/managementApi";
import { useKioskStore } from "../store/kioskStore";

export default function RegistroEntradaForm() {
  const {
    usuario,
    tipo,
    setEntradaAbierta,
    setRegistroAbierto,
  } = useKioskStore();

  const [sedes, setSedes] = useState([]);
  const [sedeId, setSedeId] = useState("");
  const [placa, setPlaca] = useState("");
  const [epp, setEpp] = useState(false);
  const [info, setInfo] = useState(true);

  const [loading, setLoading] = useState(false);
  const [mensaje, setMensaje] = useState(null);
  const [error, setError] = useState(null);

  const esExterno = tipo === "EXTERNO";

  useEffect(() => {
    getSedes().then(setSedes).catch(() => {
      setError("No se pudieron cargar las sedes");
    });
  }, []);

  const handleSubmit = async () => {
    setError(null);
    setMensaje(null);

    if (!sedeId) {
      setError("Debe seleccionar una sede");
      return;
    }

    setLoading(true);

    try {
      const payload = {
        usuario_id: usuario.id,
        sede_id: sedeId,
      };

      if (esExterno) {
        payload.placa_vehiculo = placa || null;
        payload.EPP_entregados = epp;
        payload.Informacion_recibida = info;
      }

      const resp = await RegistrarEntrada(payload);

      setMensaje("Entrada registrada correctamente");
      setEntradaAbierta(true);
      setRegistroAbierto({
        id: resp.registro_id,
        hora_entrada: resp.hora_entrada,
      });
    } catch (err) {
      setError("Error registrando la entrada");
    } finally {
      setLoading(false);
    }
  };

  if (!usuario) return null;

  return (
    <Stack spacing={2} mt={3}>
      <Typography variant="h6">
        Registrar entrada
      </Typography>

      <TextField
        select
        label="Sede"
        value={sedeId}
        onChange={(e) => setSedeId(e.target.value)}
        fullWidth
      >
        {sedes.map((sede) => (
          <MenuItem key={sede.id} value={sede.id}>
            {sede.nombre_sede}
          </MenuItem>
        ))}
      </TextField>

      {esExterno && (
        <>
          <TextField
            label="Placa del vehículo (opcional)"
            value={placa}
            onChange={(e) => setPlaca(e.target.value)}
            fullWidth
          />

          <FormControlLabel
            control={
              <Checkbox
                checked={epp}
                onChange={(e) => setEpp(e.target.checked)}
              />
            }
            label="EPP entregados"
          />

          <FormControlLabel
            control={
              <Checkbox
                checked={info}
                onChange={(e) => setInfo(e.target.checked)}
              />
            }
            label="Información recibida"
          />
        </>
      )}

      {error && <Alert severity="error">{error}</Alert>}
      {mensaje && <Alert severity="success">{mensaje}</Alert>}

      <Button
        variant="contained"
        size="large"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Registrando..." : "Registrar entrada"}
      </Button>
    </Stack>
  );
}
