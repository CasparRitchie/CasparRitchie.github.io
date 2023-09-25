from flask import Blueprint, jsonify, request
from gestion_constats import ajouter_constat, afficher_constats, visualiser_constat, modifier_constat, supprimer_constat

constats_api = Blueprint('constats_api', __name__)

@constats_api.route('/', methods=['POST'])
def create_constat():
    data = request.json
    ajouter_constat(data)
    return jsonify({"message": "Constat ajouté avec succès!"}), 201

@constats_api.route('/', methods=['GET'])
def list_constats():
    constats = afficher_constats()
    return jsonify(constats), 200

@constats_api.route('/<int:constat_id>/', methods=['GET'])
def view_constat(constat_id):
    constat = visualiser_constat(constat_id)
    if constat:
        return jsonify(constat), 200
    else:
        return jsonify({"message": "Constat non trouvé!"}), 404

@constats_api.route('/<int:constat_id>/', methods=['PUT'])
def update_constat(constat_id):
    data = request.json
    modifier_constat(constat_id, data)
    return jsonify({"message": "Constat modifié avec succès!"}), 200

@constats_api.route('/<int:constat_id>/', methods=['DELETE'])
def delete_constat(constat_id):
    supprimer_constat(constat_id)
    return jsonify({"message": "Constat supprimé avec succès!"}), 200
