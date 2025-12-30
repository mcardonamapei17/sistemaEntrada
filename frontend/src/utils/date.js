const formatearHoraColombia = (isoString) => {
    if(!isoString) return '';

    const fecha = new Date(isoString);

    return fecha.toLocaleTimeString('es-CO',{
        timeZone: "America/Bogota",
        hour: '2-digit',
        minute: '2-digit',
        hour12: true,
    });
};

export default formatearHoraColombia