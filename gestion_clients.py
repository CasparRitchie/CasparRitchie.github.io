import mysql.connector
from db_utils import create_connection

def ajouter_client():
    cnx, cursor = create_connection()
    
    client_nom = input("Entrez le nom du client: ")
    client_adresse1 = input("Entrez l'adresse du client (ligne 1): ")
    client_adresse2 = input("Entrez l'adresse du client (ligne 2): ")
    client_adresse3 = input("Entrez l'adresse du client (ligne 3): ")
    client_cp = input("Entrez le code postal du client: ")
    client_ville = input("Entrez la ville du client: ")
    client_coords = input("Entrez les coordonnées du client: ")
    client_siret = input("Entrez le SIRET du client: ")
    
    # Skipping client_logo for simplicity.
    cursor.execute("""
        INSERT INTO clients (client_nom, client_adresse1, client_adresse2, client_adresse3, client_cp, client_ville, client_coords, client_siret)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (client_nom, client_adresse1, client_adresse2, client_adresse3, client_cp, client_ville, client_coords, client_siret))
    
    cnx.commit()
    
    print(f"Client '{client_nom}' ajouté avec succès.")
    
    cursor.close()
    cnx.close()

def afficher_clients():
    cnx, cursor = create_connection(dictionary=True)
    
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()

    print("\nListe des clients:")
    for c in clients:
        print(f"ID: {c['client_id']}, Nom: {c['client_nom']}, Adresse: {c['client_adresse1']}, Ville: {c['client_ville']}, SIRET: {c['client_siret']}")

    cursor.close()
    cnx.close()

def voir_client():
    cnx, cursor = create_connection(dictionary=True)

    client_id = input("\nEntrez l'ID du client que vous souhaitez voir: ")

    cursor.execute("""
        SELECT * 
        FROM clients 
        WHERE client_id = %s
    """, (client_id,))

    client_details = cursor.fetchone()

    if client_details:
        for key, value in client_details.items():
            print(f"{key}: {value}")
    else:
        print(f"Aucun client trouvé avec l'ID {client_id}.")

    cursor.close()
    cnx.close()



def modifier_client():
    cnx, cursor = create_connection()

    afficher_clients()
    client_id = input("\nEntrez l'ID du client à modifier: ")

    print("Entrez les nouvelles valeurs pour le client ou laissez vide pour ne pas modifier:")

    nouveau_nom = input("Entrez le nouveau nom du client: ")
    nouvelle_adresse1 = input("Entrez la nouvelle adresse du client (ligne 1): ")
    nouvelle_adresse2 = input("Entrez la nouvelle adresse du client (ligne 2): ")
    nouvelle_adresse3 = input("Entrez la nouvelle adresse du client (ligne 3): ")
    nouveau_cp = input("Entrez le nouveau code postal du client: ")
    nouvelle_ville = input("Entrez la nouvelle ville du client: ")
    nouvelles_coords = input("Entrez les nouvelles coordonnées du client: ")
    nouveau_siret = input("Entrez le nouveau SIRET du client: ")

    cursor.execute("""
        UPDATE clients 
        SET client_nom = %s, 
            client_adresse1 = %s, 
            client_adresse2 = %s, 
            client_adresse3 = %s, 
            client_cp = %s, 
            client_ville = %s, 
            client_coords = %s, 
            client_siret = %s
        WHERE client_id = %s
    """, (nouveau_nom, nouvelle_adresse1, nouvelle_adresse2, nouvelle_adresse3, nouveau_cp, nouvelle_ville, nouvelles_coords, nouveau_siret, client_id))
    
    cnx.commit()

    print(f"Client modifié avec succès.")
    
    cursor.close()
    cnx.close()


def supprimer_client():
    cnx, cursor = create_connection()

    afficher_clients()
    client_id = input("\nEntrez l'ID du client à supprimer: ")

    confirmation = input(f"Etes-vous sûr de vouloir supprimer le client avec l'ID {client_id}? (Oui/Non): ").lower()
    
    if confirmation == 'oui':
        cursor.execute("""
            DELETE FROM clients 
            WHERE client_id = %s
        """, (client_id,))
        cnx.commit()
        print(f"Client avec l'ID {client_id} a été supprimé.")
    else:
        print("Suppression annulée.")

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    while True:
        print("\nGestion des clients:")
        print("1. Ajouter un client")
        print("2. Afficher les clients")
        print("3. Modifier un client")
        print("4. Voir un client")
        print("5. Supprimer un client")
        print("6. Quitter")
        
        choix = input("\nEntrez votre choix: ")

        if choix == '1':
            ajouter_client()
        elif choix == '2':
            afficher_clients()
        elif choix == '3':
            modifier_client()
        elif choix == '4':
            voir_client()
        elif choix == '5':
            supprimer_client()
        elif choix == '6':
            break
        else:
            print("Choix non reconnu. Essayez à nouveau.")
