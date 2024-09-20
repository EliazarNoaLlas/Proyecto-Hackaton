from flask import Flask, jsonify
from flask_cors import CORS
from src.routes.routes import create_app

app = create_app()
CORS(app)  # Esto permite solicitudes de cualquier origen

@app.route('/fires/bolivia')
def get_fires_bolivia():
    # Tu lógica para obtener los datos del incendio en Bolivia
    data = {'message': 'Datos del incendio en Bolivia'}
    return jsonify(data)

@app.route('/fires/peru')
def get_fires_peru():
    # Tu lógica para obtener los datos del incendio en Perú
    data = {'message': 'Datos del incendio en Perú'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)