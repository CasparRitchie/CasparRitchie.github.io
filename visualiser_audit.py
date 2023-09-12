import mysql.connector
from db_utils import create_connection


def visualiser_audit(audit_id):
    # Connect to the audit_responses_db
    cnx, cursor = create_connection(dictionary=True)  # Using dictionary to get column names with data
    try:
        # Construct the SQL query to gather audit details
        query = f"""
            SELECT 
    audits.audit_id,
    audits.date_audit,
    clients.client_nom,
    restaurants.restaurant_nom,
    gestionnaires.gestionnaire_nom,
    auditeurs.auditeur_prenom,
    auditeurs.auditeur_nom,
    client_contacts.client_contact_prenom,
    client_contacts.client_contact_nom,
    audits.nombre_de_couverts,
    audits.horaires_du_self_debut,
    audits.horaires_du_self_fin
FROM audits
JOIN clients ON audits.client_id = clients.client_id
JOIN restaurants ON audits.restaurant_id = restaurants.restaurant_id
JOIN gestionnaires ON audits.gestionnaire_id = gestionnaires.gestionnaire_id
JOIN auditeurs ON audits.auditeur_id = auditeurs.auditeur_id
JOIN client_contacts ON audits.client_contact_id = client_contacts.client_contact_id
WHERE audits.audit_id = {audit_id}
"""

        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            print("Here comes the result")
            print(result)
            return result
        else:
            print("Pas de donnees pour cet audit_id.")
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        cnx.close()
visualiser_audit(2)
