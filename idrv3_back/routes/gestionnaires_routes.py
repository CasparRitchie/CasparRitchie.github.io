from flask import Blueprint, jsonify, request
from gestion_gestionnaires import (  # You'll need to replace 'your_import_path' with the actual path to the file containing your gestionnaire functions.
    ajouter_gestionnaire, afficher_gestionnaires, modifier_gestionnaire, 
    visualiser_gestionnaire, supprimer_gestionnaire
)
from flask_cors import CORS

gestionnaires_api = Blueprint('gestionnaires_api', __name__)
CORS(gestionnaires_api, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])

@gestionnaires_api.route('/', methods=['POST'])
def add_gestionnaire():
    data = request.json
    result = ajouter_gestionnaire(data)  # You'll need to modify the function to accept parameters.
    return jsonify(result)

@gestionnaires_api.route('/', methods=['GET'])
def get_gestionnaires():
    gestionnaires = afficher_gestionnaires()
    return jsonify(gestionnaires=gestionnaires)

@gestionnaires_api.route('/<int:gestionnaire_id>', methods=['GET'])
def get_specific_gestionnaire(gestionnaire_id):
    gestionnaire = visualiser_gestionnaire(gestionnaire_id)
    if gestionnaire:
        return jsonify(gestionnaire=gestionnaire)
    else:
        return jsonify(message="Gestionnaire not found"), 404

@gestionnaires_api.route('/<int:gestionnaire_id>', methods=['PUT'])
def update_gestionnaire(gestionnaire_id):
    data = request.json
    result = modifier_gestionnaire(gestionnaire_id, data)  # Assuming you modify the function to accept parameters.
    return jsonify(result)

@gestionnaires_api.route('/<int:gestionnaire_id>', methods=['DELETE'])
def delete_gestionnaire(gestionnaire_id):
    result = supprimer_gestionnaire(gestionnaire_id)  # Assuming you modify the function to accept the gestionnaire_id parameter.
    return jsonify(result)
