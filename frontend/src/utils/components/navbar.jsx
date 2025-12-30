import { AppBar, Toolbar, Box } from '@mui/material';

const Navbar = () => {
  return (
    <AppBar 
      position="static" 
      elevation={1} // 0 para que sea plano, 1 para una sombra sutil
      sx={{ 
        backgroundColor: 'white', 
        borderBottom: '1px solid #b8b4b4ff',
        py: 1 // Padding vertical para darle aire al logo
      }}
    >
      <Toolbar sx={{ justifyContent: 'center' }}>
        {/* Contenedor del Logo */}
        <Box
          component="img"
          sx={{
            height: 40, // Ajusta el tamaño según tu logo
            width: 'auto',
          }}
          alt="Logo de la empresa"
          src="/vite.svg" // Asegúrate de que el logo esté en la carpeta public
        />
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;