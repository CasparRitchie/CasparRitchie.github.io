from flask import Blueprint
from flask_cors import CORS
from gestion_create_audit import fetch_audit_structure


create_audit_bp = Blueprint('create_audit_bp', __name__)
CORS(create_audit_bp, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])


@create_audit_bp.route('/', methods=['GET', 'POST'])
def create_audit():
    # Placeholder function
    return "Audit creation endpoint"


@create_audit_bp.route('/audit_structure', methods=['GET'])
def get_audit_structure():
    structure = fetch_audit_structure()
    return {"audit_structure": structure}
