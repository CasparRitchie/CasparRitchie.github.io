from flask import Blueprint, request, jsonify
from db_utils import create_connection
import mysql.connector

client_contacts_bp = Blueprint('client_contacts', __name__)

@client_contacts_bp.route('/', methods=['POST'])
def ajouter_contact_client():
    cnx, cursor = create_connection()
    try:
        data = request.json
        cursor.execute("""
            INSERT INTO client_contacts (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, client_contact_adresse2, client_contact_adresse3, client_contact_cp, client_contact_ville, client_contact_coords, client_contact_email, client_contact_tel, client_contact_role, client_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (data['salutation_id'], data['prenom'], data['nom'], data['adresse1'], data['adresse2'], data['adresse3'], data['cp'], data['ville'], data['coords'], data['email'], data['tel'], data['role'], data['client_id']))
        cnx.commit()
        return jsonify({"message": "Contact client ajouté avec succès!"}), 200

    except mysql.connector.Error as err:
        return jsonify({"error": f"Erreur: {err}"}), 400
    finally:
        cursor.close()
        cnx.close()

@client_contacts_bp.route('/', methods=['GET'])
def afficher_contacts_clients():
    cnx, cursor = create_connection(dictionary=True)
    try:
        cursor.execute("SELECT * FROM client_contacts")
        contacts = cursor.fetchall()
        return jsonify(contacts), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Erreur: {err}"}), 400
    finally:
        cursor.close()
        cnx.close()

@client_contacts_bp.route('/<int:contact_id>', methods=['GET'])
def visualiser_contact_client(contact_id):
    cnx, cursor = create_connection(dictionary=True)
    try:
        cursor.execute("SELECT * FROM client_contacts WHERE client_contact_id = %s", (contact_id,))
        contact = cursor.fetchone()
        if not contact:
            return jsonify({"error": "Aucun contact trouvé avec cet ID."}), 404
        return jsonify(contact), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Erreur: {err}"}), 400
    finally:
        cursor.close()
        cnx.close()

@client_contacts_bp.route('/<int:contact_id>', methods=['PUT'])
def modifier_contact_client(contact_id):
    cnx, cursor = create_connection()
    try:
        data = request.json
        cursor.execute("""
            UPDATE client_contacts SET 
                client_contact_salutation_id = %s,
                client_contact_prenom = %s,
                client_contact_nom = %s,
                client_contact_adresse1 = %s,
                client_contact_adresse2 = %s,
                client_contact_adresse3 = %s,
                client_contact_cp = %s,
                client_contact_ville = %s,
                client_contact_coords = %s,
                client_contact_email = %s,
                client_contact_tel = %s,
                client_contact_role = %s
            WHERE client_contact_id = %s
        """, (data['salutation_id'], data['prenom'], data['nom'], data['adresse1'], data['adresse2'], data['adresse3'], data['cp'], data['ville'], data['coords'], data['email'], data['tel'], data['role'], contact_id))
        cnx.commit()
        return jsonify({"message": "Contact client modifié avec succès!"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Erreur: {err}"}), 400
    finally:
        cursor.close()
        cnx.close()

@client_contacts_bp.route('/<int:contact_id>', methods=['DELETE'])
def supprimer_contact_client(contact_id):
    cnx, cursor = create_connection()
    try:
        cursor.execute("DELETE FROM client_contacts WHERE client_contact_id = %s", (contact_id,))
        cnx.commit()
        return jsonify({"message": "Contact client supprimé avec succès!"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Erreur: {err}"}), 400
    finally:
        cursor.close()
        cnx.close()
