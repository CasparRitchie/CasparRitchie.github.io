import mysql.connector
from db_utils import create_connection

def menu():
    print("\nGestion des éléments audités détails prestations:")
    print("1. Ajouter un élément audité détail prestation")
    print("2. Afficher les éléments audités détails prestations")
    print("3. Voir un élément audité détail prestation")
    print("4. Modifier un élément audité détail prestation")
    print("5. Supprimer un élément audité détail prestation")
    print("6. Quitter")
    choix = input("\nEntrez votre choix: ")
    return choix

def ajouter_element_detail_prestation():
    cnx, cursor = create_connection()

    nom = input("Entrez le nom de l'élément audité détail prestation: ")
    grammage = input("Entrez le grammage de l'élément: ")
    temperature = input("Entrez la température de l'élément: ")
    sous_titre = input("Entrez l'ID du sous-titre associé à l'élément: ")

    try:
        cursor.execute("""
            INSERT INTO elements_audites_details_prestations (elements_audites_details_prestation_nom, elements_audites_details_prestation_grammage, elements_audites_details_prestation_temperature, elements_audites_details_prestation_sous_titre)
            VALUES (%s, %s, %s, %s)
        """, (nom, grammage, temperature, sous_titre))
        cnx.commit()
        print("Élément ajouté avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()

    cursor.close()
    cnx.close()

def afficher_element_detail_prestations():
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("SELECT * FROM elements_audites_details_prestations")
    elements = cursor.fetchall()

    if not elements:
        print("Aucun élément trouvé!")
        return

    print("Liste des éléments audités détails prestations:")
    for element in elements:
        print("-" * 60)
        for key, value in element.items():
            print(f"{key}: {value}")

    cursor.close()
    cnx.close()

def voir_element_detail_prestation():
    cnx, cursor = create_connection(dictionary=True)
    
    element_id = input("Entrez l'ID de l'élément audité détail prestation que vous souhaitez voir: ")
    cursor.execute("SELECT * FROM elements_audites_details_prestations WHERE elements_audites_details_prestation_id = %s", (element_id,))
    element = cursor.fetchone()

    if not element:
        print("Élément non trouvé!")
        return

    print("Détails de l'élément audité détail prestation:")
    for key, value in element.items():
        print(f"{key}: {value}")

    cursor.close()
    cnx.close()

def modifier_element_detail_prestation():
    cnx, cursor = create_connection(dictionary=True)

    element_id = input("Entrez l'ID de l'élément audité détail prestation à modifier: ")

    cursor.execute("SELECT * FROM elements_audites_details_prestations WHERE elements_audites_details_prestation_id = %s", (element_id,))
    element = cursor.fetchone()

    if not element:
        print("Élément non trouvé!")
        return

    print("Laissez le champ vide pour conserver la valeur actuelle.")
    for key in element.keys():
        if key != "elements_audites_details_prestation_id":
            new_value = input(f"{key} (actuel: {element[key]}): ")
            if new_value:
                element[key] = new_value

    cursor.execute("""
        UPDATE elements_audites_details_prestations
        SET elements_audites_details_prestation_nom=%s, elements_audites_details_prestation_grammage=%s, elements_audites_details_prestation_temperature=%s, elements_audites_details_prestation_sous_titre=%s
        WHERE elements_audites_details_prestation_id=%s
    """, (element['elements_audites_details_prestation_nom'], element['elements_audites_details_prestation_grammage'], element['elements_audites_details_prestation_temperature'], element['elements_audites_details_prestation_sous_titre'], element_id))

    cnx.commit()
    print("Élément modifié avec succès!")
    cursor.close()
    cnx.close()

def supprimer_element_detail_prestation():
    cnx, cursor = create_connection()

    element_id = input("Entrez l'ID de l'élément audité détail prestation à supprimer: ")
    confirmation = input(f"Êtes-vous sûr de vouloir supprimer l'élément {element_id}? (oui/non): ")

    if confirmation.lower() == 'oui':
        cursor.execute("DELETE FROM elements_audites_details_prestations WHERE elements_audites_details_prestation_id = %s", (element_id,))
        cnx.commit()
        print("Élément supprimé avec succès!")
    else:
        print("Suppression annulée!")

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    while True:
        user_choice = menu()
        if user_choice == '1':
            ajouter_element_detail_prestation()
        elif user_choice == '2':
            afficher_element_detail_prestations()
        elif user_choice == '3':
            voir_element_detail_prestation()
        elif user_choice == '4':
            modifier_element_detail_prestation()
        elif user_choice == '5':
            supprimer_element_detail_prestation()
        elif user_choice == '6':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
