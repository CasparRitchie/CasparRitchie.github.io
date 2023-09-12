import mysql.connector
from db_utils import create_connection

def ajouter_contact_client():
    cnx, cursor = create_connection()

    # Gather data from the user
    salutation_id = input("Entrez l'ID de salutation: ")
    prenom = input("Entrez le prénom: ")
    nom = input("Entrez le nom: ")
    adresse1 = input("Entrez l'adresse 1: ")
    adresse2 = input("Entrez l'adresse 2: ")
    adresse3 = input("Entrez l'adresse 3: ")
    cp = input("Entrez le code postal: ")
    ville = input("Entrez la ville: ")
    coords = input("Entrez les coordonnées: ")
    email = input("Entrez l'email: ")
    tel = input("Entrez le téléphone: ")
    role = input("Entrez le rôle: ")
    client_id = input("Entrez l'ID du client associé: ")

    try:
        cursor.execute("""
            INSERT INTO client_contacts (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, client_contact_adresse2, client_contact_adresse3, client_contact_cp, client_contact_ville, client_contact_coords, client_contact_email, client_contact_tel, client_contact_role, client_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (salutation_id, prenom, nom, adresse1, adresse2, adresse3, cp, ville, coords, email, tel, role, client_id))

        cnx.commit()
        print("Contact client ajouté avec succès!")

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

# Add functions for Afficher, Modifier, Voir, and Supprimer following the structure we've established before
# ... [previous functions]


def afficher_contacts_client():
    cnx, cursor = create_connection(dictionary=True)

    try:
        cursor.execute("SELECT * FROM client_contacts")
        contacts = cursor.fetchall()

        for contact in contacts:
            print(contact)

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

    finally:
        cursor.close()
        cnx.close()


def modifier_contact_client():
    cnx, cursor = create_connection(dictionary=True)

    contact_id = input("Entrez l'ID du contact à modifier: ")

    # Displaying current details for reference
    cursor.execute(f"SELECT * FROM client_contacts WHERE client_contact_id = {contact_id}")
    contact_details = cursor.fetchone()
    if not contact_details:
        print("Aucun contact trouvé avec cet ID.")
        return

    print("Détails actuels du contact:")
    for key, value in contact_details.items():
        print(f"{key}: {value}")

    # Gathering new data from the user
    print("\nEntrez les nouvelles informations (laissez vide pour ne pas changer):")
    prenom = input("Prénom: ") or contact_details['client_contact_prenom']
    nom = input("Nom: ") or contact_details['client_contact_nom']
    adresse1 = input("Adresse 1: ") or contact_details['client_contact_adresse1']
    adresse2 = input("Adresse 2: ") or contact_details['client_contact_adresse2']
    adresse3 = input("Adresse 3: ") or contact_details['client_contact_adresse3']
    cp = input("Code postal: ") or contact_details['client_contact_cp']
    ville = input("Ville: ") or contact_details['client_contact_ville']
    coords = input("Coordonnées: ") or contact_details['client_contact_coords']
    email = input("Email: ") or contact_details['client_contact_email']
    tel = input("Téléphone: ") or contact_details['client_contact_tel']
    role = input("Rôle: ") or contact_details['client_contact_role']

    # Execute the SQL UPDATE statement for the contact
    update_query = """
    UPDATE client_contacts SET 
        client_contact_prenom = %s,
        client_contact_nom = %s,
        client_contact_adresse1 = %s,
        client_contact_adresse2 = %s,
        client_contact_adresse3 = %s,
        client_contact_cp = %s,
        client_contact_ville = %s,
        client_contact_coords = %s,
        client_contact_email = %s,
        client_contact_tel = %s,
        client_contact_role = %s
    WHERE client_contact_id = %s
    """
    cursor.execute(update_query, (prenom, nom, adresse1, adresse2, adresse3, cp, ville, coords, email, tel, role, contact_id))
    
    cnx.commit()
    print("Contact client modifié avec succès!")


def voir_contact_client():
    cnx, cursor = create_connection(dictionary=True)

    contact_id = input("Entrez l'ID du contact que vous souhaitez voir: ")

    try:
        cursor.execute(f"SELECT * FROM client_contacts WHERE client_contact_id = {contact_id}")
        contact_details = cursor.fetchone()

        if not contact_details:
            print("Aucun contact trouvé avec cet ID.")
            return

        print("Détails du contact:")
        for key, value in contact_details.items():
            print(f"{key}: {value}")

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

    finally:
        cursor.close()
        cnx.close()


def supprimer_contact_client():
    cnx, cursor = create_connection()

    contact_id = input("Entrez l'ID du contact à supprimer: ")

    confirmation = input(f"Êtes-vous sûr de vouloir supprimer le contact avec ID {contact_id}? (Oui/Non): ").lower()
    if confirmation != 'oui':
        print("Suppression annulée.")
        return

    try:
        cursor.execute(f"DELETE FROM client_contacts WHERE client_contact_id = {contact_id}")
        cnx.commit()

        print("Contact client supprimé avec succès!")

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

# ... [main execution block]


if __name__ == '__main__':
    while True:
        print("\nGestion des contacts clients:")
        print("1. Ajouter un contact client")
        print("2. Afficher les contacts client")
        print("3. Modifier un contact client")
        print("4. Voir un contact client")
        print("5. Supprimer un contact client")
        print("6. Quitter")

        choix = input("Entrez votre choix: ")

        if choix == "1":
            ajouter_contact_client()
        elif choix == "2":
            afficher_contacts_client()
        elif choix == "3":
            modifier_contact_client()
        elif choix == "4":
            voir_contact_client()
        elif choix == "5":
            supprimer_contact_client()
        elif choix == "6":
            break
