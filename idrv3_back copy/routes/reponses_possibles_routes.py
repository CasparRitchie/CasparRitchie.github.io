from flask import Blueprint, jsonify, request
from gestion_reponses_possibles import ( 
    ajouter_reponse_possible, visualiser_reponse_possible, afficher_reponse_possibles, modifier_reponse_possible, supprimer_reponse_possible
)
from flask_cors import CORS

reponses_possibles_api = Blueprint('reponses_possibles_api', __name__)
CORS(reponses_possibles_api, resources={r"/*": {"origins": "*"}})


@reponses_possibles_api.route('/', methods=['GET'])
def afficher_toutes_les_reponses():
    responses = afficher_reponse_possibles()
    return jsonify(responses), 200


@reponses_possibles_api.route('/<int:response_id>', methods=['GET'])
def afficher_une_reponse(response_id):
    response = visualiser_reponse_possible(response_id)
    if response:
        return jsonify(response), 200
    return jsonify({"error": "Non trouvé"}), 404


@reponses_possibles_api.route('/', methods=['POST'])
def ajouter_une_reponse():
    data = request.json
    response_value = data.get("response_value")
    notes_structure_id = data.get("notes_structure_id")
    new_response = ajouter_reponse_possible(response_value, notes_structure_id)
    return jsonify(new_response), 201


@reponses_possibles_api.route('/<int:response_id>', methods=['PUT'])
def modifier_une_reponse(response_id):
    data = request.json
    new_response_value = data.get("response_value")
    new_notes_structure_id = data.get("notes_structure_id")
    updated_response = modifier_reponse_possible(response_id, new_response_value, new_notes_structure_id)
    if updated_response:
        return jsonify(updated_response), 200
    return jsonify({"error": "Non trouvé"}), 404


@reponses_possibles_api.route('/<int:response_id>', methods=['DELETE'])
def supprimer_une_reponse(response_id):
    success = supprimer_reponse_possible(response_id)
    if success:
        return jsonify({"message": "Supprimé avec succès"}), 200
    return jsonify({"error": "Non trouvé"}), 404
