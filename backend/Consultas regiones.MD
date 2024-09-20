# Consultas API FIRMS Ajustadas

Este documento proporciona las URLs y detalles para consultar datos de incendios en la región amazónica de Bolivia y Perú utilizando la API de FIRMS (Fire Information for Resource Management System) de la NASA.

## 1. Datos de Incendios en la Región Amazónica de Bolivia

Para obtener datos de incendios en la región amazónica de Bolivia, usa la siguiente URL:

https://firms.modaps.eosdis.nasa.gov/api/area/csv/a4af9f9db9f15fd4ceb35731121ce9fc/VIIRS_NOAA20_NRT/-70.0,-15.0,-60.0,-10.0/1


- **Método:** GET
- **Sensor:** VIIRS_NOAA20_NRT (puedes cambiar a otro sensor si es necesario)
- **Área:** Coordenadas para la región amazónica de Bolivia (-70.0,-15.0,-60.0,-10.0)
- **Días:** 1 (puedes ajustar el número de días según necesites)

## 2. Datos de Incendios en la Región Amazónica de Perú

Para obtener datos de incendios en la región amazónica de Perú, usa la siguiente URL:

https://firms.modaps.eosdis.nasa.gov/api/area/csv/a4af9f9db9f15fd4ceb35731121ce9fc/VIIRS_NOAA20_NRT/-80.0,-15.0,-70.0,-5.0/1


- **Método:** GET
- **Sensor:** VIIRS_NOAA20_NRT (puedes cambiar a otro sensor si es necesario)
- **Área:** Coordenadas para la región amazónica de Perú (-80.0,-15.0,-70.0,-5.0)
- **Días:** 1 (puedes ajustar el número de días según necesites)

## Cómo Usar en Postman

1. Abre Postman.
2. Crea una nueva solicitud (New > Request).
3. Selecciona el método GET.
4. Copia y pega la URL completa en el campo de URL de la solicitud.
5. Haz clic en **Send** para enviar la solicitud y ver la respuesta.