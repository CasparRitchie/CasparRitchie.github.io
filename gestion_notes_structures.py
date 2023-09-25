import mysql.connector
from db_utils import create_connection

def ajouter_note_structure(notes_structure_nom, element_audite=None, est_actif=False):
    cnx, cursor = create_connection()
    try:
        cursor.execute("""
            INSERT INTO notes_structures (notes_structure_nom, element_audite, est_actif)
            VALUES (%s, %s, %s)
        """, (notes_structure_nom, element_audite or None, est_actif))
        cnx.commit()
        return {"message": "Structure de note ajoutée avec succès!"}
    except mysql.connector.Error as err:
        return {"error": f"Erreur: {err}"}
    finally:
        cursor.close()
        cnx.close()

def afficher_note_structures():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM notes_structures")
    all_structures = cursor.fetchall()
    cursor.close()
    cnx.close()
    return all_structures

def visualiser_note_structure(notes_structure_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM notes_structures WHERE notes_structure_id = %s", (notes_structure_id,))
    details = cursor.fetchone()
    cursor.close()
    cnx.close()
    return details or {}

def modifier_note_structure(notes_structure_id, notes_structure_nom=None, element_audite=None, est_actif=None):
    cnx, cursor = create_connection()

    cursor.execute("SELECT * FROM notes_structures WHERE notes_structure_id = %s", (notes_structure_id,))
    details = cursor.fetchone()
    
    if not details:
        return {"error": "Structure de note non trouvée!"}
    
    try:
        cursor.execute("""
            UPDATE notes_structures 
            SET notes_structure_nom = %s, element_audite = %s, est_actif = %s
            WHERE notes_structure_id = %s
        """, (notes_structure_nom or details['notes_structure_nom'], element_audite or details['element_audite'], est_actif or details['est_actif'], notes_structure_id))
        
        cnx.commit()
        return {"message": "Structure de note modifiée avec succès!"}
    except mysql.connector.Error as err:
        return {"error": f"Erreur: {err}"}
    finally:
        cursor.close()
        cnx.close()

def supprimer_note_structure(notes_structure_id):
    cnx, cursor = create_connection()
    try:
        cursor.execute("DELETE FROM notes_structures WHERE notes_structure_id = %s", (notes_structure_id,))
        cnx.commit()
        return {"message": "Structure de note supprimée avec succès!"}
    except mysql.connector.Error as err:
        return {"error": f"Erreur: {err}"}
    finally:
        cursor.close()
        cnx.close()
