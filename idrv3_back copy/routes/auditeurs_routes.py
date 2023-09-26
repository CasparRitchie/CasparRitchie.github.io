from flask import Blueprint, request, jsonify
from gestion_auditeurs import (
    ajouter_auditeur,
    afficher_auditeurs,
    visualiser_auditeur,
    modifier_auditeur,
    supprimer_auditeur
)
from flask_cors import CORS

auditeurs_bp = Blueprint('auditeurs', __name__)
CORS(auditeurs_bp, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])

@auditeurs_bp.route('/', methods=['POST'])
def add_auditeur():
    data = request.get_json()
    response = ajouter_auditeur(data)
    if "message" in response and "Erreur" in response["message"]:
        return jsonify(response), 400
    return jsonify(response), 200

@auditeurs_bp.route('/', methods=['GET'])
def get_all_auditeurs():
    auditeurs = afficher_auditeurs()
    return jsonify(auditeurs), 200

@auditeurs_bp.route('/<int:auditeur_id>', methods=['GET'])
def get_auditeur(auditeur_id):
    auditeur = visualiser_auditeur(auditeur_id)
    if not auditeur:
        return jsonify({"message": "Auditeur non trouvé!"}), 404
    return jsonify({'auditeur': auditeur}), 200

@auditeurs_bp.route('/<int:auditeur_id>', methods=['PUT'])
def update_auditeur(auditeur_id):
    data = request.get_json()
    response = modifier_auditeur(auditeur_id, data)
    return jsonify(response), 200

@auditeurs_bp.route('/<int:auditeur_id>', methods=['DELETE'])
def delete_auditeur(auditeur_id):
    response = supprimer_auditeur(auditeur_id)
    return jsonify(response), 200
