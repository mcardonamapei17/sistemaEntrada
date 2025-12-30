import {
  Card,
  CardContent,
  Typography,
  Stack,
  Chip,
  Box,
  Avatar,
} from "@mui/material";

// Iconos para igualar la imagen
import PersonOutlineIcon from '@mui/icons-material/PersonOutline';
import BusinessIcon from '@mui/icons-material/Business'; // Para Empresa
import BadgeIcon from '@mui/icons-material/Badge'; // Para Tipo de Usuario
import LoginIcon from '@mui/icons-material/Login'; // Para Última Entrada
import LogoutIcon from '@mui/icons-material/Logout';
import WareHouseIcon from '@mui/icons-material/Warehouse'

import { useKioskStore } from "../store/kioskStore";
import formatearHoraColombia from "../../utils/date";

export default function UsuarioResumen() {
  const {
    usuario,
    empresa,
    tipo,
    sede,
    entradaAbierta,
    registroAbierto,
  } = useKioskStore();

  if (!usuario) return null;

  // Reutilizamos la lógica de fila con icono para no repetir código
  const InfoRow = ({ icon: Icon, label, value }) => (
    <Stack direction="row" spacing={2} alignItems="flex-start" sx={{ mb: 2 }}>
      <Icon sx={{ color: 'text.secondary', mt: 0.5 }} />
      <Box>
        <Typography variant="caption" color="text.secondary" sx={{ display: 'block', lineHeight: 1 }}>
          {label}
        </Typography>
        <Typography variant="body1" sx={{ fontWeight: 500, color: 'text.primary' }}>
          {value}
        </Typography>
      </Box>
    </Stack>
  );

  return (
    <Card 
      elevation={0} 
      sx={{ 
        mt: 3, 
        borderRadius: 4, 
        border: '1px solid #e0e4e8',
        position: 'relative', // Para ubicar el chip arriba
        overflow: 'visible' 
      }}
    >
      <CardContent sx={{ p: 4 }}>
        {/* Chip de Estado (Esquina Superior Derecha) */}
        <Box sx={{ position: 'absolute', top: 20, right: 20 }}>
          <Chip
            icon={entradaAbierta ? <LogoutIcon fontSize="small" /> : <LoginIcon fontSize="small" />}
            label={entradaAbierta ? "Adentro" : "Afuera"}
            color={entradaAbierta ? "info" : "default"}
            sx={{ 
                fontWeight: 'bold', 
                backgroundColor: entradaAbierta ? '#f0f7ff' : '#f4f6f8',
                color: entradaAbierta ? '#007fff' : '#454f5b' 
            }}
          />
        </Box>

        {/* Encabezado: Avatar y Nombre */}
        <Stack direction="row" spacing={2} alignItems="center" sx={{ mb: 4 }}>
          <Avatar sx={{ bgcolor: '#f4f6f8', color: '#454f5b', width: 56, height: 56 }}>
            <PersonOutlineIcon fontSize="large" />
          </Avatar>
          <Box>
            <Typography variant="h5" sx={{ fontWeight: 700, color: '#1a1c1e' }}>
              {usuario.nombre} {usuario.apellido}
            </Typography>
            <Typography variant="body1" color="text.secondary">
              {usuario.documento}
            </Typography>
          </Box>
        </Stack>

        <Stack spacing={0.5}>
          {/* Fila: Tipo de Usuario */}
          <InfoRow 
            icon={BadgeIcon} 
            label="Tipo de Usuario" 
            value={tipo === 3 ? "Externo" : "Empleado"} 
          />

          {/* Fila: Empresa */}
          {empresa && (
            <InfoRow 
              icon={BusinessIcon} 
              label="Empresa / Entidad" 
              value={empresa.nombre} 
            />
          )}
          
          {entradaAbierta && registroAbierto && (
            <InfoRow 
              icon={WareHouseIcon}
              label="Sede / lugar"
              value={registroAbierto.sede.nombre}
            />
          )}

          {/* Fila: Registro Abierto */}
          {entradaAbierta && registroAbierto ? (
            <InfoRow 
              icon={LoginIcon} 
              label="Última Entrada" 
              value={`${registroAbierto.fecha} a las ${registroAbierto.hora_entrada ? formatearHoraColombia(registroAbierto.hora_entrada) : "---"}`} 
            />
          ) : (
            <InfoRow 
              icon={LogoutIcon} 
              label="Estado" 
              value="Sin registros activos hoy" 
            />
          )}
        </Stack>
      </CardContent>
    </Card>
  );
}