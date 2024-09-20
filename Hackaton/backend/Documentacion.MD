# Documentación del Proyecto Backend

## Descripción del Proyecto

Este proyecto es una API que proporciona datos sobre incendios en Bolivia y Perú utilizando la API de FIRMS (Fire Information for Resource Management System) de la NASA. La API está construida con Flask, un framework de Python para aplicaciones web.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:
backend/
├── .gitignore
├── README.MD
├── env/
│   ├── Lib/
│   │   └── site-packages/
│   │       ├── pip-24.2.dist-info/
│   │       ├── pip/
│   │       ├── pip/internal/
│   │       ├── pip/vendor/
│   │       └── ...
│   ├── Scripts/
│   │   ├── activate
│   │   ├── activate.bat
│   │   └── Activate.ps1
│   └── pyvenv.cfg
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── controller.py
│   ├── extensions.py
│   ├── models/
│   │   └── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services/
│   │   └── __init__.py
│   └── utils/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── main.py
└── wsgi.py

## Archivos Principales

### `main.py`
Este archivo es el punto de entrada de la aplicación. Configura la aplicación Flask y define algunas rutas básicas.

### `wsgi.py`
Este archivo se utiliza para desplegar la aplicación en un servidor WSGI.

### `Consultas.MD` y `Consultas regiones.MD`
Estos archivos contienen ejemplos de consultas a la API de FIRMS para obtener datos de incendios en diferentes regiones.

## Requisitos

Los requisitos del proyecto están listados en el archivo `requirements.txt`. Asegúrate de instalar estos paquetes antes de ejecutar la aplicación.

## Cómo Ejecutar el Proyecto

1. Clona el repositorio.
2. Crea un entorno virtual y actívalo.
3. Instala los requisitos con `pip install -r requirements.txt`.
4. Ejecuta la aplicación con `python main.py`.

## Rutas Disponibles

- `/fires/bolivia`: Devuelve datos de incendios en Bolivia.
- `/fires/peru`: Devuelve datos de incendios en Perú.

Estas rutas están definidas en el archivo `main.py`.

## Uso de la API

Para probar la API, puedes usar herramientas como Postman. Los detalles de las consultas están en los archivos `Consultas.MD` y `Consultas regiones.MD`.

Espero que esta documentación te sea útil para entender y trabajar con el proyecto.