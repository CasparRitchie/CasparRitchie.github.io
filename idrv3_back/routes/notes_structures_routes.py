from flask import Blueprint, jsonify, request
from gestion_notes_structures import (  # You'll need to ensure the necessary functions are imported from the correct module
    ajouter_note_structure, visualiser_note_structure, afficher_note_structures, modifier_note_structure, supprimer_note_structure
)
from flask_cors import CORS

notes_structures_api = Blueprint('notes_structures_api', __name__)
CORS(notes_structures_api, resources={r"/*": {"origins": "*"}})

@notes_structures_api.route('/', methods=['GET'])
def afficher_toutes_les_structures():
    structures = afficher_note_structures()
    return jsonify(structures), 200

@notes_structures_api.route('/<int:structure_id>', methods=['GET'])
def afficher_une_structure(structure_id):
    structure = visualiser_note_structure(structure_id)
    if structure:
        return jsonify(structure), 200
    return jsonify({"error": "Non trouvé"}), 404

@notes_structures_api.route('/', methods=['POST'])
def ajouter_une_structure():
    data = request.json
    notes_structure_nom = data.get("notes_structure_nom")
    element_audite = data.get("element_audite")
    est_actif = data.get("est_actif")
    new_structure = ajouter_note_structure(notes_structure_nom, element_audite, est_actif)
    return jsonify(new_structure), 201

@notes_structures_api.route('/<int:structure_id>', methods=['PUT'])
def modifier_une_structure(structure_id):
    data = request.json
    new_notes_structure_nom = data.get("notes_structure_nom")
    new_element_audite = data.get("element_audite")
    new_est_actif = data.get("est_actif")
    updated_structure = modifier_note_structure(structure_id, new_notes_structure_nom, new_element_audite, new_est_actif)
    if updated_structure:
        return jsonify(updated_structure), 200
    return jsonify({"error": "Non trouvé"}), 404

@notes_structures_api.route('/<int:structure_id>', methods=['DELETE'])
def supprimer_une_structure(structure_id):
    success = supprimer_note_structure(structure_id)
    if success:
        return jsonify({"message": "Supprimé avec succès"}), 200
    return jsonify({"error": "Non trouvé"}), 404
