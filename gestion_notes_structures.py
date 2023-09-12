import mysql.connector
from db_utils import create_connection


def ajouter_notes_structure():
    cnx, cursor = create_connection()

    notes_structure_nom = input("Entrez le nom de la structure de note: ")
    element_audite = input("Entrez l'élément audité (laisser vide si non déterminé): ")
    est_actif_input = input("Est-ce actif? (oui/non): ")
    est_actif = True if est_actif_input.lower() == 'oui' else False

    try:
        cursor.execute("""
            INSERT INTO notes_structures (notes_structure_nom, element_audite, est_actif)
            VALUES (%s, %s, %s)
        """, (notes_structure_nom, element_audite or None, est_actif))
        cnx.commit()
        print("Structure de note ajoutée avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()

def afficher_notes_structures():
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("""
        SELECT * FROM notes_structures
    """)
    all_structures = cursor.fetchall()

    print("Liste de toutes les structures de notes:")
    for structure in all_structures:
        for key, value in structure.items():
            print(f"{key}: {value}")

        # Fetch associated responses for each structure
        cursor.execute("""
            SELECT response_value FROM reponses_possibles
            WHERE notes_structure_id = %s
        """, (structure['notes_structure_id'],))
        responses = cursor.fetchall()

        print("Réponses possibles:")
        for response in responses:
            print(f"  - {response['response_value']}")
        print("-" * 50)  # Separator

    cursor.close()
    cnx.close()



def modifier_notes_structure():
    cnx, cursor = create_connection()

    notes_structure_id = input("Entrez l'ID de la structure de note à modifier: ")

    cursor.execute("SELECT * FROM notes_structures WHERE notes_structure_id = %s", (notes_structure_id,))
    details = cursor.fetchone()

    if not details:
        print("Structure de note non trouvée!")
        return

    print("Détails actuels de la structure de note:")
    for key, value in details.items():
        print(f"{key}: {value}")

    notes_structure_nom = input(f"Entrez le nouveau nom de la structure de note ({details['notes_structure_nom']}): ")
    element_audite = input(f"Entrez le nouvel élément audité ({details['element_audite']}): ")
    est_actif_input = input(f"Est-ce actif? (actuel: {details['est_actif']}) (oui/non): ")
    est_actif = True if est_actif_input.lower() == 'oui' else False

    try:
        cursor.execute("""
            UPDATE notes_structures 
            SET notes_structure_nom = %s, element_audite = %s, est_actif = %s
            WHERE notes_structure_id = %s
        """, (notes_structure_nom or details['notes_structure_nom'], element_audite or details['element_audite'], est_actif, notes_structure_id))
        
        cnx.commit()
        print("Structure de note modifiée avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()


def voir_notes_structure():
    cnx, cursor = create_connection(dictionary=True)

    notes_structure_id = input("Entrez l'ID de la structure de note que vous souhaitez voir: ")
    cursor.execute("""
        SELECT * FROM notes_structures 
        WHERE notes_structure_id = %s
    """, (notes_structure_id,))
    details = cursor.fetchone()

    if not details:
        print("Structure de note non trouvée!")
        return

    print("Détails de la structure de note:")
    for key, value in details.items():
        print(f"{key}: {value}")

    # Fetch associated responses
    cursor.execute("""
        SELECT response_value FROM reponses_possibles
        WHERE notes_structure_id = %s
    """, (notes_structure_id,))
    responses = cursor.fetchall()

    print("\nRéponses possibles:")
    for response in responses:
        print(response['response_value'])

    cursor.close()
    cnx.close()




def supprimer_notes_structure():
    cnx, cursor = create_connection()

    notes_structure_id = input("Entrez l'ID de la structure de note à supprimer: ")

    sure = input(f"Êtes-vous sûr de vouloir supprimer la structure de note avec l'ID {notes_structure_id}? (oui/non): ")

    if sure.lower() == 'oui':
        try:
            cursor.execute("DELETE FROM notes_structures WHERE notes_structure_id = %s", (notes_structure_id,))
            cnx.commit()
            print("Structure de note supprimée avec succès!")
        except mysql.connector.Error as err:
            print(f"Erreur: {err}")
            cnx.rollback()
    else:
        print("Suppression annulée.")
    
    cursor.close()
    cnx.close()










if __name__ == '__main__':
    while True:
        print("\nGestion des Structures des notes:")
        print("1. Ajouter une structure de notes")
        print("2. Afficher les structures")
        print("3. Modifier un structure")
        print("4. Voir un structure")
        print("5. Supprimer un structure")
        print("6. Quitter")

        choix = input("Entrez votre choix: ")

        if choix == "1":
            ajouter_notes_structure()
        elif choix == "2":
            afficher_notes_structures()
        elif choix == "3":
            modifier_notes_structure()
        elif choix == "4":
            voir_notes_structure()
        elif choix == "5":
            supprimer_notes_structure()
        elif choix == "6":
            break