```markdown:README.md
# Proyecto de Monitoreo y Prevención de Incendios Forestales

Este proyecto tiene como objetivo monitorear y prevenir incendios forestales en las regiones amazónicas de Perú y Bolivia, mostrando un mapa interactivo en tiempo real y proporcionando información educativa para los estudiantes.

## Estructura del Proyecto

```bash
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
│   │   ├── EmergencyInfo.js   # Información de emergencia (mochila, números de bomberos)
│   │   ├── FireInfo.js        # Información detallada sobre incendios
│   │   ├── WaterPoints.js     # Puntos de agua útiles para bomberos
│   │   └── Navbar.js          # Barra de navegación
│   ├── styles/
│   │   ├── App.css            # Estilos globales
│   │   ├── MapView.css        # Estilos del mapa
│   │   └── EmergencyInfo.css  # Estilos de la información de emergencia
│   ├── utils/
│   │   └── api.js             # Conexión con el backend
│   ├── App.js                 # Componente principal de la aplicación
│   ├── index.js               # Punto de entrada de React
│   └── setupTests.js          # Configuración para pruebas (opcional)
```

## Instalación

Para comenzar a usar este proyecto, sigue los siguientes pasos:

### Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

### Instala las dependencias:

Desde la carpeta raíz del proyecto (`frontend/sistema-web/`), ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
npm install
```

### Instala las dependencias adicionales necesarias para el mapa interactivo:

```bash
npm install react-leaflet leaflet

```

### Ejecuta el proyecto:

Después de instalar las dependencias, puedes iniciar el servidor de desarrollo con el siguiente comando:

```bash
npm start
```

Esto lanzará la aplicación en el navegador en la dirección `http://localhost:3000/`.

## Descripción de Componentes

- **MapView.js**: Componente que muestra el mapa interactivo con los puntos de incendios en tiempo real.
- **EmergencyInfo.js**: Componente que muestra información sobre la mochila de emergencia y números de bomberos.
- **FireInfo.js**: Componente que proporciona información adicional sobre incendios.
- **WaterPoints.js**: Componente que muestra los puntos de agua útiles para los bomberos.
- **Navbar.js**: Barra de navegación superior para la aplicación.

## Próximos pasos

- Implementar la lógica para la visualización de flora y fauna afectada en los puntos de incendios.
- Añadir más sonidos y efectos visuales relacionados con los incendios forestales.

---

Este README te proporciona una estructura clara, un flujo de instalación y una descripción básica de los componentes del proyecto. Puedes adaptarlo según los detalles específicos a medida que desarrolles más funcionalidades.
```
