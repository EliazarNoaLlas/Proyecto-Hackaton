# Proyecto de Monitoreo y Prevención de Incendios Forestales

Este proyecto tiene como objetivo monitorear y prevenir incendios forestales en las regiones amazónicas de Perú y Bolivia, mostrando un mapa interactivo en tiempo real y proporcionando información educativa para los estudiantes.

## Estructura del Proyecto
frontend/sistema-web/
├── .gitignore
├── README.md
├── package.json
├── public/
│   ├── index.html
│   ├── manifest.json
│   └── robots.txt
├── src/
│   ├── assets/
│   │   ├── images/
│   │   │   └── logo.png
│   │   └── sounds/
│   │       └── fire-sound.mp3
│   ├── components/
│   │   ├── MapView.js        # Componente para el mapa de incendios
│   │   ├── EmergencyInfo.js  # Información de emergencia (mochila, números de bomberos)
│   │   ├── FireInfo.js       # Información detallada sobre incendios
│   │   ├── WaterPoints.js    # Puntos de agua útiles para bomberos
│   │   └── Navbar.js         # Barra de navegación
│   ├── styles/
│   │   ├── App.css           # Estilos globales
│   │   ├── MapView.css       # Estilos del mapa
│   │   └── EmergencyInfo.css # Estilos de la información de emergencia
│   ├── utils/
│   │   └── api.js            # Conexión con el backend
│   ├── App.js                # Componente principal de la aplicación
│   ├── index.js              # Punto de entrada de React
│   └── setupTests.js         # Configuración para pruebas (opcional)


### Ejecuta el proyecto:

Después de instalar las dependencias, puedes iniciar el servidor de desarrollo con el siguiente comando:
npm start