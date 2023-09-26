import mysql.connector
from db_utils import create_connection
from datetime import timedelta

def ajouter_audit(data):
    cnx, cursor = create_connection(dictionary=True)
    try:
        cursor.execute("""
            INSERT INTO audits (client_id, date_audit, client_contact_id, gestionnaire_id, auditeur_id, restaurant_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (data['client_id'], data['date_audit'], data['client_contact_id'], data['gestionnaire_id'], data['auditeur_id'], data['restaurant_id'], data['nombre_de_couverts'], "11:30:00", "14:00:00"))
        audit_id = cursor.lastrowid
        cnx.commit()
        return "Audit créé avec succès!"
    except mysql.connector.Error as err:
        cnx.rollback()
        return f"Erreur: {err}"
    finally:
        cursor.close()
        cnx.close()

def get_all_audits():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("""
        SELECT audits.audit_id, clients.client_nom, gestionnaires.gestionnaire_nom, auditeurs.auditeur_prenom, 
               auditeurs.auditeur_nom, elements.element_nom, restaurants.restaurant_nom, audits.date_audit,
               client_contacts.client_contact_prenom, client_contacts.client_contact_nom, audits.nombre_de_couverts,
               audits.horaires_du_self_debut, audits.horaires_du_self_fin
        FROM audits
        LEFT JOIN clients ON audits.client_id = clients.client_id
        LEFT JOIN gestionnaires ON audits.gestionnaire_id = gestionnaires.gestionnaire_id
        LEFT JOIN auditeurs ON audits.auditeur_id = auditeurs.auditeur_id
        LEFT JOIN elements ON audits.chapitre = elements.element_id
        LEFT JOIN restaurants ON audits.restaurant_id = restaurants.restaurant_id
        LEFT JOIN client_contacts ON audits.client_contact_id = client_contacts.client_contact_id
    """)
    audits = cursor.fetchall()
    cursor.close()
    cnx.close()
    return audits

def get_constats_for_audit(audit_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("""
        SELECT constats.constat, e.element_nom, rp.response_value AS score
        FROM constats
        LEFT JOIN elements e ON constats.element_id = e.element_id
        LEFT JOIN reponses_possibles rp ON constats.score = rp.response_id
        WHERE audit_id = %s
    """, (audit_id,))
    constats = cursor.fetchall()
    cursor.close()
    cnx.close()
    return constats


def afficher_audits():
    audits = get_all_audits()
    
    if not audits:
        return "Aucun audit trouvé!"
    
    audit_list = []
    for audit in audits:
        audit_data = {}
        for key, value in audit.items():
            # Convert timedelta objects to strings
            if isinstance(value, timedelta):
                audit_data[key] = str(value)
            else:
                audit_data[key] = value
        
        constats = get_constats_for_audit(audit['audit_id'])
        if constats:
            audit_data['constats'] = constats
        audit_list.append(audit_data)
    
    return audit_list


def visualiser_audit(audit_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("""
        SELECT audits.audit_id, clients.client_nom, gestionnaires.gestionnaire_nom, auditeurs.auditeur_prenom, 
               auditeurs.auditeur_nom, elements.element_nom, restaurants.restaurant_nom, audits.date_audit,
               client_contacts.client_contact_prenom, client_contacts.client_contact_nom, audits.nombre_de_couverts,
               audits.horaires_du_self_debut, audits.horaires_du_self_fin
        FROM audits
        LEFT JOIN clients ON audits.client_id = clients.client_id
        LEFT JOIN gestionnaires ON audits.gestionnaire_id = gestionnaires.gestionnaire_id
        LEFT JOIN auditeurs ON audits.auditeur_id = auditeurs.auditeur_id
        LEFT JOIN elements ON audits.chapitre = elements.element_id
        LEFT JOIN restaurants ON audits.restaurant_id = restaurants.restaurant_id
        LEFT JOIN client_contacts ON audits.client_contact_id = client_contacts.client_contact_id
        WHERE audits.audit_id = %s
    """, (audit_id,))
    audit = cursor.fetchone()
    if not audit:
        return "Audit non trouvé!"
    audit_details = {}
    for key, value in audit.items():
        audit_details[key] = value
    constats = get_constats_for_audit(audit_id)
    if constats:
        audit_details['constats'] = constats
    cursor.close()
    cnx.close()
    return audit_details

def modifier_audit(audit_id, updated_data):
    cnx, cursor = create_connection(dictionary=True)
    try:
        cursor.execute("""
            UPDATE audits
            SET client_id=%s, gestionnaire_id=%s, auditeur_id=%s, chapitre=%s,
                restaurant_id=%s, date_audit=%s, client_contact_id=%s, nombre_de_couverts=%s,
                horaires_du_self_debut=%s, horaires_du_self_fin=%s
            WHERE audit_id=%s
        """, (updated_data['client_id'], updated_data['gestionnaire_id'], updated_data['auditeur_id'], updated_data['chapitre'],
              updated_data['restaurant_id'], updated_data['date_audit'], updated_data['client_contact_id'], 
              updated_data['nombre_de_couverts'], updated_data['horaires_du_self_debut'], updated_data['horaires_du_self_fin'],
              audit_id))
        cnx.commit()
        return "Audit modifié avec succès!"
    except mysql.connector.Error as err:
        cnx.rollback()
        return f"Erreur: {err}"
    finally:
        cursor.close()
        cnx.close()

def supprimer_audit(audit_id):
    cnx, cursor = create_connection()
    try:
        cursor.execute("DELETE FROM audits WHERE audit_id = %s", (audit_id,))
        cnx.commit()
        return "Audit supprimé avec succès!"
    except mysql.connector.Error as err:
        return f"Erreur: {err}"
    finally:
        cursor.close()
        cnx.close()
