import { Box } from "@mui/material";
import KioskPage from "./kiosk/pages/kioskPage"; // Quita las llaves {}
import Navbar from "./utils/components/navbar";

function App() {
  return (
    <Box sx={{minHeight: '100vh', backgroundColor: '#f5f5f5'}}>
      <Navbar />
      <KioskPage />
    </Box>
  );
}

export default App;