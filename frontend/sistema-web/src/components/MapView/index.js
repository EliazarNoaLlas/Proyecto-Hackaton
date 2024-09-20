import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

// Configura el icono del marcador
const markerIcon = new L.Icon({
    iconUrl: '/images/marker-icon.png', // URL de la imagen del marcador
    iconSize: [25, 25], // Tamaño del icono [ancho, alto]
    iconAnchor: [12, 25], // Punto del icono que se ancla al mapa [x, y]
    popupAnchor: [0, -25], // Punto desde el cual se abre el popup [x, y]
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png', // URL de la sombra del marcador
    shadowSize: [41, 41], // Tamaño de la sombra [ancho, alto]
    shadowAnchor: [12, 41] // Punto de anclaje de la sombra [x, y]
  });

function FireMap() {
  const [fireData, setFireData] = useState([]);

  useEffect(() => {
    async function fetchFireData() {
      try {
        const [peruResponse, boliviaResponse] = await Promise.all([
          fetch('http://localhost:5000/fires/peru'),
          fetch('http://localhost:5000/fires/bolivia')
        ]);

        const peruData = await peruResponse.json();
        const boliviaData = await boliviaResponse.json();

        // Combina los datos de Perú y Bolivia
        const combinedData = [...parseCSV(peruData.data), ...parseCSV(boliviaData.data)];
        setFireData(combinedData);
      } catch (error) {
        console.error('Error fetching fire data:', error);
      }
    }

    fetchFireData();
  }, []);

  // Función para parsear los datos CSV
  function parseCSV(data) {
    const lines = data.split('\n');
    const result = [];
    const headers = lines[0].split(',');

    for (let i = 1; i < lines.length; i++) {
      const obj = {};
      const currentline = lines[i].split(',');

      for (let j = 0; j < headers.length; j++) {
        obj[headers[j]] = currentline[j];
      }
      result.push(obj);
    }
    return result;
  }

  return (
    <MapContainer center={[-10, -70]} zoom={5} style={{ height: '100vh', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {Array.isArray(fireData) && fireData.map((fire, index) => (
        <Marker key={index} position={[parseFloat(fire.latitude), parseFloat(fire.longitude)]} icon={markerIcon}>
          <Popup>
            {`Fire detected on ${fire.acq_date}`}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}

export default FireMap;