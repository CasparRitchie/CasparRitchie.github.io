import mysql.connector
from db_utils import create_connection

def ajouter_constat(data):
    cnx, cursor = create_connection()

    # Extracting data with defaults or NULL
    constat = data.get('constat', None)  # NULL is acceptable for MySQL in Python
    elements_audites_details_prestation_id = data.get('elements_audites_details_prestation_id', None)
    element_id = data.get('element_id', None)
    heure_du_constat = data.get('heure_du_constat', None)  # assuming you're okay with NULL for datetime
    score = data.get('score', None)
    observations = data.get('observations', '')
    audit_id = data.get('audit_id', None)
    auditeur_id = data.get('auditeur_id', None)

    try:
        cursor.execute("""
            INSERT INTO constats (constat, elements_audites_details_prestation_id, element_id, heure_du_constat, score, 
                                 observations, audit_id, auditeur_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (constat, elements_audites_details_prestation_id, element_id, heure_du_constat, score, observations, audit_id, auditeur_id))
        cnx.commit()
        cursor.close()
        cnx.close()
        return {"message": "Constat ajouté avec succès!"}
    except mysql.connector.Error as err:
        print("MySQL error:", err)
        return {"message": f"Erreur lors de l'ajout du constat! Error: {err}"}


def afficher_constats():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM constats")
    constats = cursor.fetchall()
    cursor.close()
    cnx.close()
    return constats

def modifier_constat(constat_id, data):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM constats WHERE constat_id = %s", (constat_id,))
    details = cursor.fetchone()

    if not details:
        return {"message": "Constat non trouvé!"}

    # Extracting new data or using existing data
    new_constat = data.get('constat') or details['constat']
    new_elements_audites_details_prestation_id = data.get('elements_audites_details_prestation_id') or details['elements_audites_details_prestation_id']
    new_element_id = data.get('element_id') or details['element_id']
    new_heure_du_constat = data.get('heure_du_constat') or details['heure_du_constat']
    new_score = data.get('score') or details['score']
    new_observations = data.get('observations') or details['observations']
    new_piece_jointe = data.get('piece_jointe') or details['piece_jointe']
    new_audit_id = data.get('audit_id') or details['audit_id']
    new_auditeur_id = data.get('auditeur_id') or details['auditeur_id']

    cursor.execute("""
        UPDATE constats
        SET constat=%s, elements_audites_details_prestation_id=%s, element_id=%s, heure_du_constat=%s, score=%s, 
            observations=%s, piece_jointe=%s, audit_id=%s, auditeur_id=%s
        WHERE constat_id=%s
    """, (new_constat, new_elements_audites_details_prestation_id, new_element_id, new_heure_du_constat, new_score, 
          new_observations, new_piece_jointe, new_audit_id, new_auditeur_id, constat_id))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Constat modifié avec succès!"}

def supprimer_constat(constat_id):
    cnx, cursor = create_connection()
    cursor.execute("DELETE FROM constats WHERE constat_id = %s", (constat_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Constat supprimé avec succès!"}

def visualiser_constat(constat_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM constats WHERE constat_id = %s", (constat_id,))
    details = cursor.fetchone()
    cursor.close()
    cnx.close()

    if not details:
        return {"message": "Constat non trouvé!"}

    return details
