import mysql.connector
from db_utils import create_connection

def menu():
    print("\nGestion des légendes:")
    print("1. Ajouter une légende")
    print("2. Afficher les légendes")
    print("3. Voir une légende")
    print("4. Modifier une légende")
    print("5. Supprimer une légende")
    print("6. Quitter")
    choix = input("\nEntrez votre choix: ")
    return choix

def ajouter_legende():
    cnx, cursor = create_connection()
    
    legende_name = input("Entrez le nom de la légende: ")
    chapitre = input("Entrez le chapitre associé (ID de l'élément): ")
    legende_elements = input("Entrez les éléments de la légende: ")
    
    try:
        cursor.execute("""
            INSERT INTO legendes (legende_name, chapitre, legende_elements)
            VALUES (%s, %s, %s)
        """, (legende_name, chapitre, legende_elements))
        cnx.commit()
        print("Légende ajoutée avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()

    cursor.close()
    cnx.close()

def afficher_legendes():
    cnx, cursor = create_connection(dictionary=True)
    
    cursor.execute("SELECT * FROM legendes")
    legendes = cursor.fetchall()

    if not legendes:
        print("Aucune légende trouvée!")
        return

    print("Liste des légendes:")
    for legende in legendes:
        print("-" * 40)
        for key, value in legende.items():
            print(f"{key}: {value}")

    cursor.close()
    cnx.close()

def voir_legende():
    cnx, cursor = create_connection(dictionary=True)
    
    legende_id = input("Entrez l'ID de la légende que vous souhaitez voir: ")
    cursor.execute("SELECT * FROM legendes WHERE legende_id = %s", (legende_id,))
    legende = cursor.fetchone()

    if not legende:
        print("Légende non trouvée!")
        return

    print("Détails de la légende:")
    for key, value in legende.items():
        print(f"{key}: {value}")

    cursor.close()
    cnx.close()

def modifier_legende():
    cnx, cursor = create_connection(dictionary=True)

    legende_id = input("Entrez l'ID de la légende à modifier: ")

    cursor.execute("SELECT * FROM legendes WHERE legende_id = %s", (legende_id,))
    legende = cursor.fetchone()

    if not legende:
        print("Légende non trouvée!")
        return

    print("Laissez le champ vide pour conserver la valeur actuelle.")
    for key in legende.keys():
        if key != "legende_id":
            new_value = input(f"{key} (actuel: {legende[key]}): ")
            if new_value:
                legende[key] = new_value

    cursor.execute("""
        UPDATE legendes
        SET legende_name=%s, chapitre=%s, legende_elements=%s
        WHERE legende_id=%s
    """, (legende['legende_name'], legende['chapitre'], legende['legende_elements'], legende_id))

    cnx.commit()
    print("Légende modifiée avec succès!")
    cursor.close()
    cnx.close()

def supprimer_legende():
    cnx, cursor = create_connection()

    legende_id = input("Entrez l'ID de la légende à supprimer: ")
    confirmation = input(f"Êtes-vous sûr de vouloir supprimer la légende {legende_id}? (oui/non): ")

    if confirmation.lower() == 'oui':
        cursor.execute("DELETE FROM legendes WHERE legende_id = %s", (legende_id,))
        cnx.commit()
        print("Légende supprimée avec succès!")
    else:
        print("Suppression annulée!")

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    while True:
        user_choice = menu()
        if user_choice == '1':
            ajouter_legende()
        elif user_choice == '2':
            afficher_legendes()
        elif user_choice == '3':
            legende_id = input("Entrez l'ID de la légende que vous souhaitez voir: ")
            voir_legende(legende_id)
        elif user_choice == '4':
            modifier_legende()
        elif user_choice == '5':
            supprimer_legende()
        elif user_choice == '6':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
