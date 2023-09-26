from flask import Blueprint, jsonify, request
from gestion_legendes import (
    ajouter_legende, visualiser_legende, afficher_legendes, modifier_legende, supprimer_legende
)
from flask_cors import CORS

legendes_api = Blueprint('legendes_api', __name__)
CORS(legendes_api, resources={r"/*": {"origins": "*"}})

@legendes_api.route('/', methods=['GET'])
def afficher_toutes_les_legendes():
    legendes = afficher_legendes()
    return jsonify(legendes), 200

@legendes_api.route('/<int:legende_id>', methods=['GET'])
def afficher_une_legende(legende_id):
    legende = visualiser_legende(legende_id)
    if legende:
        return jsonify(legende), 200
    return jsonify({"error": "Non trouvé"}), 404

@legendes_api.route('/', methods=['POST'])
def ajouter_une_legende():
    data = request.json
    legende_name = data.get("legende_name")
    chapitre = data.get("chapitre")
    legende_elements = data.get("legende_elements")
    result = ajouter_legende(legende_name, chapitre, legende_elements)
    return jsonify(result), 201 if result["status"] == "success" else 400

@legendes_api.route('/<int:legende_id>', methods=['PUT'])
def modifier_une_legende(legende_id):
    data = request.json
    updates = {
        "legende_name": data.get("legende_name"),
        "chapitre": data.get("chapitre"),
        "legende_elements": data.get("legende_elements")
    }
    result = modifier_legende(legende_id, updates)
    if result["status"] == "success":
        return jsonify(result), 200
    return jsonify({"error": "Non trouvé"}), 404

@legendes_api.route('/<int:legende_id>', methods=['DELETE'])
def supprimer_une_legende(legende_id):
    result = supprimer_legende(legende_id)
    if result["status"] == "success":
        return jsonify(result), 200
    return jsonify({"error": "Non trouvé"}), 404
