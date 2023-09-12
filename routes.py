from flask import Blueprint, jsonify, request
from flask_cors import CORS
import gestion_auditeurs
import gestion_audits
import gestion_salutations

salutations_api = Blueprint('salutations_api', __name__)
CORS(salutations_api, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])

main = Blueprint('main', __name__)
CORS(main, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])


@main.route('/')
def home():
    return "Welcome to the Flask API!"

@main.route('/test', methods=['GET'])
def test_route():
    return jsonify(message="Test successful!")


@main.route('/admin', methods=['GET'])
def hello_admin():
    response = jsonify(message="Hello from FCasparrrrrrask!")
    return response

@main.route('/hello', methods=['GET'])
def hello():
    response = jsonify(message="Hello from Flask!")
    return response

@main.route('/auditeurs', methods=['GET'])
def get_all_auditeurs():
    auditeurs = gestion_auditeurs.afficher_auditeurs()
    response = jsonify(auditeurs=auditeurs)
    return response

@main.route('/auditeurs', methods=['POST'])
def add_auditeur():
    data = request.json
    prenom = data['prenom']
    nom = data['nom']
    email = data['email']
    telephone = data['telephone']

    gestion_auditeurs.ajouter_auditeur(prenom, nom, email, telephone)
    response = jsonify(message="Auditeur added successfully!")
    return response

@main.route('/ajouter_audit', methods=['POST'])
def ajouter_audit_endpoint():
    data = request.json
    gestion_audits.ajouter_audit(data)
    response = jsonify(message="Audit added successfully!")
    return response

@main.route('/afficher_audits', methods=['GET'])
def afficher_audits_endpoint():
    audits = gestion_audits.afficher_audits()
    response = jsonify(audits=audits)
    return response

@main.route('/visualiser_audit/<int:audit_id>', methods=['GET'])
def visualiser_audit_endpoint(audit_id):
    audit = gestion_audits.visualiser_audit(audit_id)
    if audit:
        response = jsonify(audit=audit)
    else:
        response = jsonify(message="Audit not found"), 404
    return response

# @main.route('/changer_audit', methods=['PUT'])
# def changer_audit_endpoint():
#     # Extract data and call the changer_audit function
#     # Return an appropriate response
#     # ...

@main.route('/supprimer_audit/<int:audit_id>', methods=['DELETE'])
def supprimer_audit_endpoint(audit_id):
    gestion_audits.supprimer_audit(audit_id)
    response = jsonify(message="Audit deleted successfully!")
    return response





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


