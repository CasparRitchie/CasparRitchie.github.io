import mysql.connector
from db_utils import create_connection


def ajouter_reponse_possible():
    cnx, cursor = create_connection()

    # Gather data for the new response_possible
    response_value = input("Entrez la valeur de la réponse: ")
    notes_structure_id = input("Entrez l'ID de la structure de note associée: ")

    try:
        # Insert the new response_possible into the database
        cursor.execute("""
            INSERT INTO reponses_possibles (response_value, notes_structure_id)
            VALUES (%s, %s)
        """, (response_value, notes_structure_id))
        cnx.commit()
        print("Réponse possible ajoutée avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()


def afficher_reponses_possibles():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("""
        SELECT response_id, response_value, notes_structure_nom 
        FROM reponses_possibles 
        LEFT JOIN notes_structures ON reponses_possibles.notes_structure_id = notes_structures.notes_structure_id
    """)
    responses = cursor.fetchall()
    for response in responses:
        print(response)
    cursor.close()
    cnx.close()


def modifier_reponse_possible():
    cnx, cursor = create_connection(dictionary=True)
    
    response_id = input("Entrez l'ID de la réponse à modifier: ")
    cursor.execute("SELECT * FROM reponses_possibles WHERE response_id = %s", (response_id,))
    response = cursor.fetchone()

    if not response:
        print("Réponse non trouvée!")
        return

    print("Détails actuels de la réponse:")
    for key, value in response.items():
        print(f"{key}: {value}")

    # Ask user for new values
    new_response_value = input(f"Entrez la nouvelle valeur de la réponse (laissez vide pour garder '{response['response_value']}'): ")
    new_notes_structure_id = input(f"Entrez le nouvel ID de la structure de note associée (laissez vide pour garder '{response['notes_structure_id']}'): ")

    try:
        cursor.execute("""
            UPDATE reponses_possibles
            SET response_value = %s, notes_structure_id = %s
            WHERE response_id = %s
        """, (new_response_value or response['response_value'], new_notes_structure_id or response['notes_structure_id'], response_id))
        cnx.commit()
        print("Réponse modifiée avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()


def voir_reponse_possible():
    cnx, cursor = create_connection(dictionary=True)

    response_id = input("Entrez l'ID de la réponse que vous souhaitez voir: ")

    cursor.execute("""
        SELECT reponses_possibles.*, notes_structures.notes_structure_nom
        FROM reponses_possibles
        LEFT JOIN notes_structures ON reponses_possibles.notes_structure_id = notes_structures.notes_structure_id
        WHERE response_id = %s
    """, (response_id,))
    
    response = cursor.fetchone()

    if not response:
        print("Réponse non trouvée!")
        return

    print("Détails de la réponse:")
    for key, value in response.items():
        print(f"{key}: {value}")

    cursor.close()
    cnx.close()



def supprimer_reponse_possible():
    cnx, cursor = create_connection()
    
    response_id = input("Entrez l'ID de la réponse à supprimer: ")
    
    sure = input(f"Êtes-vous sûr de vouloir supprimer la réponse avec l'ID {response_id}? (oui/non): ").lower()
    if sure != 'oui':
        print("Suppression annulée.")
        return

    try:
        cursor.execute("DELETE FROM reponses_possibles WHERE response_id = %s", (response_id,))
        cnx.commit()
        print("Réponse supprimée avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()



if __name__ == '__main__':
    while True:
        print("\nGestion des réponses possibles:")
        print("1. Ajouter une nouvelle possible réponse")
        print("2. Afficher les réponses actuellement dispos")
        print("3. Modifier une réponse possible existant")
        print("4. Voir une réponse possible existant")
        print("5. Supprimer une réponse possible existant")
        print("6. Quitter")

        choix = input("Entrez votre choix: ")

        if choix == "1":
            ajouter_reponse_possible()
        elif choix == "2":
            afficher_reponses_possibles()
        elif choix == "3":
            modifier_reponse_possible()
        elif choix == "4":
            voir_reponse_possible()
        elif choix == "5":
            supprimer_reponse_possible()
        elif choix == "6":
            break