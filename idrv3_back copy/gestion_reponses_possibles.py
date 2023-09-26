import mysql.connector
from db_utils import create_connection


def ajouter_reponse_possible(response_value, notes_structure_id):
    cnx, cursor = create_connection()
    try:
        cursor.execute("""
            INSERT INTO reponses_possibles (response_value, notes_structure_id)
            VALUES (%s, %s)
        """, (response_value, notes_structure_id))
        cnx.commit()

        return {"message": "Réponse possible ajoutée avec succès!"}
    except mysql.connector.Error as err:
        return {"error": str(err)}
    finally:
        cursor.close()
        cnx.close()


def afficher_reponse_possibles():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("""
        SELECT response_id, response_value, notes_structure_nom 
        FROM reponses_possibles 
        LEFT JOIN notes_structures ON reponses_possibles.notes_structure_id = notes_structures.notes_structure_id
    """)
    responses = cursor.fetchall()
    cursor.close()
    cnx.close()
    return responses


def modifier_reponse_possible(response_id, new_response_value, new_notes_structure_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM reponses_possibles WHERE response_id = %s", (response_id,))
    response = cursor.fetchone()

    if not response:
        return {"error": "Réponse non trouvée!"}

    try:
        cursor.execute("""
            UPDATE reponses_possibles
            SET response_value = %s, notes_structure_id = %s
            WHERE response_id = %s
        """, (new_response_value, new_notes_structure_id, response_id))
        cnx.commit()
        return {"message": "Réponse modifiée avec succès!"}
    except mysql.connector.Error as err:
        return {"error": str(err)}
    finally:
        cursor.close()
        cnx.close()


def visualiser_reponse_possible(response_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("""
        SELECT reponses_possibles.*, notes_structures.notes_structure_nom
        FROM reponses_possibles
        LEFT JOIN notes_structures ON reponses_possibles.notes_structure_id = notes_structures.notes_structure_id
        WHERE response_id = %s
    """, (response_id,))

    response = cursor.fetchone()
    cursor.close()
    cnx.close()
    if not response:
        return {"error": "Réponse non trouvée!"}
    return response


def supprimer_reponse_possible(response_id):
    cnx, cursor = create_connection()
    try:
        cursor.execute("DELETE FROM reponses_possibles WHERE response_id = %s", (response_id,))
        cnx.commit()
        return {"message": "Réponse supprimée avec succès!"}
    except mysql.connector.Error as err:
        return {"error": str(err)}
    finally:
        cursor.close()
        cnx.close()