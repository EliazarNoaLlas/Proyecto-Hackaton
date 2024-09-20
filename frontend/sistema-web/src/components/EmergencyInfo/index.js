import React from 'react';

const EmergencyInfo = () => {
  return (
    <div>
      <h2>Información de Emergencia</h2>
      <p>Escucha el sonido de llamas para simular la emergencia.</p>
      <audio controls>
        <source src="../assets/sounds/fire-sound.mp3" type="audio/mpeg" />
        Tu navegador no soporta el elemento de audio.
      </audio>
      <h3>Mochila de Emergencia</h3>
      <p>Información sobre una mochila de emergencia para quemaduras.</p>
      <h3>Números de Bomberos</h3>
      <p>Incluye números de contacto de bomberos.</p>
    </div>
  );
};

export default EmergencyInfo;
