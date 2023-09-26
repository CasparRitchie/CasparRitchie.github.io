from flask import Blueprint, jsonify, request
from flask_cors import CORS
from gestion_audits import ajouter_audit, afficher_audits, visualiser_audit, modifier_audit, supprimer_audit, get_constats_for_audit

audits_api = Blueprint('audits_api', __name__)
CORS(audits_api, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])


@audits_api.route('/', methods=['POST'])
def create_audit():
    data = request.json
    ajouter_audit(data)
    return jsonify({"message": "Audit ajouté avec succès!"}), 201

@audits_api.route('/', methods=['GET'])
def list_audits():
    audits = afficher_audits()
    return jsonify(audits), 200

@audits_api.route('/<int:audit_id>/', methods=['GET'])
def view_audit(audit_id):
    audit = visualiser_audit(audit_id)
    if audit:
        return jsonify(audit), 200
    else:
        return jsonify({"message": "Audit non trouvé!"}), 404

@audits_api.route('/<int:audit_id>/', methods=['PUT'])
def update_audit(audit_id):
    data = request.json
    modifier_audit(audit_id, data)
    return jsonify({"message": "Audit modifié avec succès!"}), 200

@audits_api.route('/<int:audit_id>/', methods=['DELETE'])
def delete_audit(audit_id):
    supprimer_audit(audit_id)
    return jsonify({"message": "Audit supprimé avec succès!"}), 200

@audits_api.route('/<int:audit_id>/constats/', methods=['GET'])
def get_constats_for_specific_audit(audit_id):
    constats = get_constats_for_audit(audit_id)
    if constats:
        return jsonify(constats), 200
    else:
        return jsonify({"message": "Aucun constat trouvé pour cet audit!"}), 404
