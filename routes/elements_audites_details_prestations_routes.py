from flask import Blueprint, request, jsonify
from gestion_elements_audites_details_prestations import (ajouter_element_audites_details_prestation, afficher_element_audites_details_prestations,
                                                          visualiser_element_audites_details_prestation, modifier_element_audites_details_prestation,
                                                          supprimer_element_audites_details_prestation)
from flask_cors import CORS


details_prestations_bp = Blueprint('elements_audites_details_prestations', __name__)
CORS(details_prestations_bp, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])


@details_prestations_bp.route('/', methods=['POST'])
def add_element():
    data = request.get_json()
    response = ajouter_element_audites_details_prestation(data)
    if "error" in response:
        return jsonify(response), 400
    return jsonify({'message': 'Element added successfully'}), 200

@details_prestations_bp.route('/', methods=['GET'])
def get_all_elements():
    elements = afficher_element_audites_details_prestations()
    return jsonify(elements), 200

@details_prestations_bp.route('/<int:element_id>', methods=['GET'])
def get_element(element_id):
    element = visualiser_element_audites_details_prestation(element_id)
    if "message" in element:
        return jsonify(element), 404
    return jsonify({'element': element}), 200

@details_prestations_bp.route('/<int:element_id>', methods=['PUT'])
def update_element(element_id):
    data = request.get_json()
    modifier_element_audites_details_prestation(element_id, data)
    return jsonify({'message': 'Element updated successfully'}), 200

@details_prestations_bp.route('/<int:element_id>', methods=['DELETE'])
def delete_element(element_id):
    supprimer_element_audites_details_prestation(element_id)
    return jsonify({'message': 'Element deleted successfully'}), 200
