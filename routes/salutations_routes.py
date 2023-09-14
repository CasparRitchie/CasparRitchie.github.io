from flask import Blueprint, jsonify, request
import gestion_salutations
from flask_cors import CORS  # Ensure you import this if you're using CORS here

salutations_api = Blueprint('salutations_api', __name__)
CORS(salutations_api, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])


@salutations_api.route('/salutations', methods=['POST'])
def add_salutation():
    salutation = request.json.get('salutation')
    success = gestion_salutations.ajouter_salutation(salutation)  # Get the result of the insertion attempt
    
    if success:
        return jsonify(message=f"Salutation '{salutation}' ajoutée avec succès.")
    else:
        return jsonify(message=f"Salutation '{salutation}' already exists."), 409  # 409 is the HTTP status code for "Conflict"

@salutations_api.route('/salutations/<int:salutation_id>', methods=['GET'])
def get_specific_salutation(salutation_id):
    salutation = gestion_salutations.visualiser_salutation(salutation_id)
    if salutation:
        return jsonify(salutation=salutation)
    else:
        return jsonify(message="Salutation not found"), 404

@salutations_api.route('/salutations', methods=['GET'])
def get_salutations():
    salutations = gestion_salutations.afficher_salutations()
    print("Salutations from the endpoint:", salutations)  # Debugging line
    return jsonify(salutations=salutations)

@salutations_api.route('/salutations/<int:salutation_id>', methods=['PUT'])
def update_salutation(salutation_id):
    nouvelle_salutation = request.json.get('salutation')
    if not nouvelle_salutation:
        return jsonify(message="La nouvelle salutation n'est pas fournie."), 400

    try:
        gestion_salutations.modifier_salutation(salutation_id, nouvelle_salutation)
        return jsonify(message="Salutation modifiée avec succès.")
    except Exception as e:
        return jsonify(message=f"Erreur lors de la mise à jour: {str(e)}"), 500


@salutations_api.route('/salutations/<int:salutation_id>', methods=['DELETE'])
def delete_salutation(salutation_id):
    try:
        gestion_salutations.supprimer_salutation(salutation_id)
        return jsonify(message="Salutation supprimée avec succès.")
    except Exception as e:
        return jsonify(message=f"Erreur lors de la suppression: {str(e)}"), 500


