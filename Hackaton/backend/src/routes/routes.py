# src/routes/routes.py

from flask import Flask
from src.controllers.controller import controller_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(controller_bp)
    return app
