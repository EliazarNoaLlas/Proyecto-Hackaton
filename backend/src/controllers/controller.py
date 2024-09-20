# File: controller.py
# Author: eliazar
# Copyright: 2024, Hackathon Peru.
# License: MIT
#
# Purpose:
# Define endpoints for user CRUD operations and fire data retrieval.
#
# Last Modified: 2024-09-17
# src/controllers/controller.py

import requests
from flask import Blueprint, jsonify, request
from ..config import API_BASE_URL
from ..extensions import db
from ..models.model import User

controller_bp = Blueprint('controller', __name__)


# FIRE DATA FUNCTIONS
def fetch_fire_data(bounds, days):
    url = f"{API_BASE_URL}/{bounds}/{days}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        response.raise_for_status()


@controller_bp.route('/fires/bolivia', methods=['GET'])
def get_fires_bolivia():
    bounds = "-70.0,-15.0,-60.0,-10.0"
    days = 1
    try:
        data = fetch_fire_data(bounds, days)
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@controller_bp.route('/fires/peru', methods=['GET'])
def get_fires_peru():
    bounds = "-80.0,-15.0,-70.0,-5.0"
    days = 1
    try:
        data = fetch_fire_data(bounds, days)
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# USER CRUD OPERATIONS
# CREATE: Crear un nuevo usuario
@controller_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


# READ: Obtener todos los usuarios
@controller_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


# READ: Obtener un usuario por ID
@controller_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())


# UPDATE: Actualizar un usuario
@controller_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    username = data.get('username')

    user = User.query.get(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    if username:
        user.username = username

    db.session.commit()
    return jsonify(user.to_dict())


# DELETE: Eliminar un usuario
@controller_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
