import mysql.connector
from db_utils import create_connection

def ajouter_element_audites_details_prestation(data):
    cnx, cursor = create_connection()

    nom = data.get('elements_audites_details_prestation_nom')
    grammage = data.get('elements_audites_details_prestation_grammage')
    temperature = data.get('elements_audites_details_prestation_temperature')
    sous_titre = data.get('elements_audites_details_prestation_sous_titre')



    if not nom or not grammage or not temperature or not sous_titre:
        return {"message": "All element details are required!"}

    try:
        cursor.execute("""
            INSERT INTO elements_audites_details_prestations (elements_audites_details_prestation_nom, elements_audites_details_prestation_grammage, elements_audites_details_prestation_temperature, elements_audites_details_prestation_sous_titre)
            VALUES (%s, %s, %s, %s)
        """, (nom, grammage, temperature, sous_titre))
        cnx.commit()
        cursor.close()
        cnx.close()
        return {"message": "Élément ajouté avec succès!"}
    except mysql.connector.Error as err:
        print("MySQL error:", err)
        return {"message": f"Erreur lors de l'ajout de l'élément! Error: {err}"}


def afficher_element_audites_details_prestations():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM elements_audites_details_prestations")
    elements = cursor.fetchall()
    cursor.close()
    cnx.close()
    return elements

def modifier_element_audites_details_prestation(element_id, data):
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("SELECT * FROM elements_audites_details_prestations WHERE elements_audites_details_prestation_id = %s", (element_id,))
    details = cursor.fetchone()

    if not details:
        return {"message": "Élément non trouvé!"}

    new_nom = data.get('elements_audites_details_prestation_nom')
    new_grammage = data.get('elements_audites_details_prestation_grammage')
    new_temperature = data.get('elements_audites_details_prestation_temperature')
    new_sous_titre = data.get('elements_audites_details_prestation_sous_titre')


    cursor.execute("""
        UPDATE elements_audites_details_prestations
        SET elements_audites_details_prestation_nom=%s, elements_audites_details_prestation_grammage=%s, elements_audites_details_prestation_temperature=%s, elements_audites_details_prestation_sous_titre=%s
        WHERE elements_audites_details_prestation_id=%s
    """, (new_nom, new_grammage, new_temperature, new_sous_titre, element_id))

    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Élément modifié avec succès!"}

def supprimer_element_audites_details_prestation(element_id):
    cnx, cursor = create_connection()
    cursor.execute("DELETE FROM elements_audites_details_prestations WHERE elements_audites_details_prestation_id = %s", (element_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Élément supprimé avec succès!"}

def visualiser_element_audites_details_prestation(element_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM elements_audites_details_prestations WHERE elements_audites_details_prestation_id = %s", (element_id,))
    details = cursor.fetchone()
    cursor.close()
    cnx.close()

    if not details:
        return {"message": "Élément non trouvé!"}

    return details
