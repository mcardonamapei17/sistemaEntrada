import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App'

import {ThemeProvider, CssBaseline} from '@mui/material';
import {createTheme} from '@mui/material/styles';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2'
    },
  }
})

ReactDOM.createRoot(document.getElementById('root')).render(
  <ThemeProvider theme={theme}>
    <CssBaseline />
    <App />
  </ThemeProvider>
)