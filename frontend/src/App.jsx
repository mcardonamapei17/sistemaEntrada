import DocumentoInput from "./kiosk/components/DocumentoInput";
import { BuscarDocumentos } from "./api/attendanceApi";
import { useState } from "react";

function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleBuscar = async (documento) => {
    setLoading(true);
    setError(null);

    try {
      const data = await BuscarDocumentos(documento);
      console.log("Resultado:", data);
    } catch (err) {
      setError("Error consultando documento");
    } finally {
      setLoading(false);
    }
  };

  return (
    <DocumentoInput
      onBuscar={handleBuscar}
      loading={loading}
      error={error}
    />
  );
}

export default App;
