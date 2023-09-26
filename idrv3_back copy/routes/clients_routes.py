from flask import Blueprint, request, jsonify
from gestion_clients import (ajouter_client, afficher_clients, visualiser_client, 
                             modifier_client, supprimer_client)
from flask_cors import CORS

clients_bp = Blueprint('clients', __name__)
CORS(clients_bp, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])

@clients_bp.route('/', methods=['POST'])
def add_client():
    data = request.get_json()
    response = ajouter_client(data)
    if "error" in response:
        return jsonify(response), 400
    return jsonify({'message': 'Client added successfully'}), 200

@clients_bp.route('/', methods=['GET'])
def get_all_clients():
    clients = afficher_clients()
    return jsonify(clients), 200

@clients_bp.route('/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = visualiser_client(client_id)
    if "error" in client:
        return jsonify(client), 404
    return jsonify({'client': client}), 200

@clients_bp.route('/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    response = modifier_client(client_id, data)
    return jsonify(response), 200

@clients_bp.route('/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    response = supprimer_client(client_id)
    return jsonify(response), 200
