from flask import Blueprint, request, jsonify
from gestion_elements import ajouter_element, afficher_elements, visualiser_element, modifier_element, supprimer_element
from flask_cors import CORS

elements_bp = Blueprint('elements', __name__)
CORS(elements_bp, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])


@elements_bp.route('/', methods=['GET'])
def get_elements():
    return jsonify(afficher_elements()), 200

@elements_bp.route('/<int:element_id>', methods=['GET'])
def get_element(element_id):
    element = visualiser_element(element_id)
    if "message" in element:
        return jsonify(element), 404  # sending the message as an error
    return jsonify({'element': element}), 200  # wrapping element in a dictionary


@elements_bp.route('/', methods=['POST'])
def add_element():
    data = request.get_json()
    ajouter_element(data)  # Pass the entire dictionary to the function.
    return jsonify({'message': 'Element added successfully'}), 201


@elements_bp.route('/<int:element_id>', methods=['PUT'])
def update_element(element_id):
    data = request.get_json()
    modifier_element(element_id, data)  # Pass the element_id and the entire dictionary to the function.
    return jsonify({'message': 'Element updated successfully'}), 200


@elements_bp.route('/<int:element_id>', methods=['DELETE'])
def delete_element(element_id):
    supprimer_element(element_id)
    return jsonify({'message': 'Element deleted successfully'}), 200
