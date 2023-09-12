import mysql.connector
from db_utils import create_connection


def ajouter_gestionnaire():
    cnx, cursor = create_connection()
    
    nom = input("Entrez le nom du gestionnaire: ")
    coords = input("Entrez les coordonnées du gestionnaire: ")

    cursor.execute("""
        INSERT INTO gestionnaires (gestionnaire_nom, gestionnaire_coords)
        VALUES (%s, %s)
    """, (nom, coords))
    
    cnx.commit()
    print("Gestionnaire ajouté avec succès!")
    cursor.close()
    cnx.close()


def afficher_gestionnaires():
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("SELECT * FROM gestionnaires")
    gestionnaires = cursor.fetchall()

    for g in gestionnaires:
        print(g)

    cursor.close()
    cnx.close()


def modifier_gestionnaire():
    cnx, cursor = create_connection(dictionary=True)

    gestionnaire_id = input("Entrez l'ID du gestionnaire à modifier: ")
    cursor.execute(f"SELECT * FROM gestionnaires WHERE gestionnaire_id = {gestionnaire_id}")
    details = cursor.fetchone()

    if not details:
        print("Gestionnaire non trouvé!")
        return

    print("Détails actuels:")
    for key, value in details.items():
        print(f"{key}: {value}")

    print("\nEntrez les nouvelles informations (laissez vide pour ne pas changer):")
    nom = input("Nom: ") or details['gestionnaire_nom']
    coords = input("Coordonnées: ") or details['gestionnaire_coords']

    cursor.execute("""
        UPDATE gestionnaires 
        SET gestionnaire_nom = %s, gestionnaire_coords = %s
        WHERE gestionnaire_id = %s
    """, (nom, coords, gestionnaire_id))
    
    cnx.commit()
    print("Gestionnaire modifié avec succès!")
    cursor.close()
    cnx.close()


def supprimer_gestionnaire():
    cnx, cursor = create_connection()

    gestionnaire_id = input("Entrez l'ID du gestionnaire à supprimer: ")
    sure = input("Êtes-vous sûr de vouloir supprimer ce gestionnaire? (Oui/Non): ").lower()

    if sure == 'oui':
        cursor.execute(f"DELETE FROM gestionnaires WHERE gestionnaire_id = {gestionnaire_id}")
        cnx.commit()
        print("Gestionnaire supprimé avec succès!")
    else:
        print("Opération annulée.")

    cursor.close()
    cnx.close()


def voir_gestionnaire():
    cnx, cursor = create_connection(dictionary=True)

    gestionnaire_id = input("Entrez l'ID du gestionnaire que vous souhaitez voir: ")
    cursor.execute(f"SELECT * FROM gestionnaires WHERE gestionnaire_id = {gestionnaire_id}")
    details = cursor.fetchone()

    if not details:
        print("Gestionnaire non trouvé!")
        return

    print("Détails du gestionnaire:")
    for key, value in details.items():
        print(f"{key}: {value}")

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    while True:
        print("\nGestion des gestionnaires:")
        print("1. Ajouter un gestionnaire")
        print("2. Afficher les gestionnaires")
        print("3. Modifier un gestionnaire")
        print("4. Voir un gestionnaire")
        print("5. Supprimer un gestionnaire")
        print("6. Quitter")
        
        choix = input("\nEntrez votre choix: ")

        if choix == '1':
            ajouter_gestionnaire()
        elif choix == '2':
            afficher_gestionnaires()
        elif choix == '3':
            modifier_gestionnaire()
        elif choix == '4':
            voir_gestionnaire()
        elif choix == '5':
            supprimer_gestionnaire()
        elif choix == '6':
            break
        else:
            print("Choix non valide!")
