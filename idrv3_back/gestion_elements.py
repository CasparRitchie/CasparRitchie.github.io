import mysql.connector
from db_utils import create_connection


def ajouter_element(data):
    cnx, cursor = create_connection()
    
    chapitre = data.get('chapitre')
    titre = data.get('titre')
    sous_titre = data.get('sous_titre')
    element_nom = data.get('element_nom')
    notes_structure_id = data.get('notes_structure_id') # This assumes you're passing the related ID directly.

    if not chapitre or not titre or not sous_titre or not element_nom:
        return {"message": "All element details are required!"}

    cursor.execute("""
        INSERT INTO elements (chapitre, titre, sous_titre, element_nom, notes_structure_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (chapitre, titre, sous_titre, element_nom, notes_structure_id))
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Element ajouté avec succès!"}

def afficher_elements():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM elements")
    elements = cursor.fetchall()
    cursor.close()
    cnx.close()
    print(elements)
    return elements

def modifier_element(element_id, data):
    cnx, cursor = create_connection(dictionary=True)
    
    cursor.execute(f"SELECT * FROM elements WHERE element_id = %s", (element_id,))
    details = cursor.fetchone()

    if not details:
        return {"message": "Element non trouvé!"}

    # Using the provided data or existing values from the database.
    new_chapitre = data.get('chapitre') or details['chapitre']
    new_titre = data.get('titre') or details['titre']
    new_sous_titre = data.get('sous_titre') or details['sous_titre']
    new_element_nom = data.get('element_nom') or details['element_nom']
    new_notes_structure_id = data.get('notes_structure_id') or details['notes_structure_id']

    cursor.execute("""
        UPDATE elements
        SET chapitre = %s, titre = %s, sous_titre = %s, element_nom = %s, notes_structure_id = %s
        WHERE element_id = %s
    """, (new_chapitre, new_titre, new_sous_titre, new_element_nom, new_notes_structure_id, element_id))
    
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Element modifié avec succès!"}

def supprimer_element(element_id):
    cnx, cursor = create_connection()
    cursor.execute(f"DELETE FROM elements WHERE element_id = %s", (element_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Element supprimé avec succès!"}

def visualiser_element(element_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute(f"SELECT * FROM elements WHERE element_id = %s", (element_id,))
    details = cursor.fetchone()
    cursor.close()
    cnx.close()

    if not details:
        return {"message": "Element non trouvé!"}

    return details
