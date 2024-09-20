# Consultas API FIRMS

## 1. Verificación del estado de las transacciones

- **Método:** GET
- **URL:** `https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=a4af9f9db9f15fd4ceb35731121ce9fc`

## 2. Disponibilidad de datos para todos los sensores

- **Método:** GET
- **URL:** `https://firms.modaps.eosdis.nasa.gov/api/data_availability/csv/a4af9f9db9f15fd4ceb35731121ce9fc/all`

## 3. Consulta de detecciones de incendios por área

- **Método:** GET
- **URL:** `https://firms.modaps.eosdis.nasa.gov/api/area/csv/a4af9f9db9f15fd4ceb35731121ce9fc/VIIRS_NOAA20_NRT/world/1`

### Parámetros ajustables:

- **Sensor:** VIIRS_NOAA20_NRT
- **Área:** world (modificable según la región deseada)
- **Días:** 1 (ajustable según necesidad)

## 4. Consulta de detecciones de incendios por país

- **Método:** GET
- **URL:** `https://firms.modaps.eosdis.nasa.gov/api/country/csv/a4af9f9db9f15fd4ceb35731121ce9fc/MODIS_NRT/PER/4`

### Parámetros ajustables:

- **Sensor:** MODIS_NRT
- **País:** PER (código del país, en este caso Perú)
- **Días:** 4 (ajustable según necesidad)

## Cómo usar en Postman

1. Abre Postman.
2. Crea una nueva solicitud (New > Request).
3. Elige el método GET.
4. Copia y pega la URL completa en el campo de URL de la solicitud.
5. Haz clic en Send para enviar la solicitud y ver la respuesta.

Estos ejemplos te permitirán probar diferentes funcionalidades de la API de FIRMS utilizando tu clave API.