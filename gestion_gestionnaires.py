import mysql.connector
from db_utils import create_connection

def ajouter_gestionnaire(data):
    cnx, cursor = create_connection()
    
    nom = data.get('gestionnaire_nom')
    coords = data.get('gestionnaire_coords')

    if not nom or not coords:
        return {"message": "Nom et coordonnées du gestionnaire sont requis!"}

    cursor.execute("""
        INSERT INTO gestionnaires (gestionnaire_nom, gestionnaire_coords)
        VALUES (%s, %s)
    """, (nom, coords))
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Gestionnaire ajouté avec succès!"}


def afficher_gestionnaires():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM gestionnaires")
    gestionnaires = cursor.fetchall()
    cursor.close()
    cnx.close()
    return gestionnaires

def modifier_gestionnaire(gestionnaire_id, data):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute(f"SELECT * FROM gestionnaires WHERE gestionnaire_id = %s", (gestionnaire_id,))
    details = cursor.fetchone()

    if not details:
        return {"message": "Gestionnaire non trouvé!"}

    # If the user doesn't provide a value for 'gestionnaire_nom' or 'gestionnaire_coords',
    # it will use the existing values from the database.
    new_nom = data.get('gestionnaire_nom') or details['gestionnaire_nom']
    new_coords = data.get('gestionnaire_coords') or details['gestionnaire_coords']

    cursor.execute("""
        UPDATE gestionnaires 
        SET gestionnaire_nom = %s, gestionnaire_coords = %s
        WHERE gestionnaire_id = %s
    """, (new_nom, new_coords, gestionnaire_id))
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Gestionnaire modifié avec succès!"}


def supprimer_gestionnaire(gestionnaire_id):
    cnx, cursor = create_connection()
    cursor.execute(f"DELETE FROM gestionnaires WHERE gestionnaire_id = %s", (gestionnaire_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Gestionnaire supprimé avec succès!"}

def visualiser_gestionnaire(gestionnaire_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute(f"SELECT * FROM gestionnaires WHERE gestionnaire_id = %s", (gestionnaire_id,))
    details = cursor.fetchone()
    cursor.close()
    cnx.close()

    if not details:
        return {"message": "Gestionnaire non trouvé!"}

    return details
