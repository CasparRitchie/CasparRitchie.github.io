import mysql.connector
from db_utils import create_connection


def ajouter_auditeur():
    cnx, cursor = create_connection()

    salutation_id = input("Entrez l'ID de salutation de l'auditeur: ")
    prenom = input("Entrez le prénom de l'auditeur: ")
    nom = input("Entrez le nom de l'auditeur: ")
    tel = input("Entrez le numéro de téléphone de l'auditeur: ")
    email = input("Entrez l'email de l'auditeur: ")
    login_id = input("Entrez l'ID de connexion de l'auditeur: ")
    permissions = input("Entrez les permissions de l'auditeur: ")

    cursor.execute("""
        INSERT INTO auditeurs (auditeur_salutation_id, auditeur_prenom, auditeur_nom, auditeur_tel, auditeur_email, auditeur_login_id, auditeur_permissions)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (salutation_id, prenom, nom, tel, email, login_id, permissions))

    cnx.commit()
    print("Auditeur ajouté avec succès!")
    cursor.close()
    cnx.close()


def afficher_auditeurs():
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("""
        SELECT auditeurs.auditeur_id, salutations.salutation, auditeurs.auditeur_prenom, auditeurs.auditeur_nom,
               auditeurs.auditeur_tel, auditeurs.auditeur_email
        FROM auditeurs
        LEFT JOIN salutations ON auditeurs.auditeur_salutation_id = salutations.salutation_id
    """)

    auditeurs = cursor.fetchall()

    if not auditeurs:
        print("Aucun auditeur trouvé.")
        return

    print("\nListe des auditeurs:")
    for auditeur in auditeurs:
        print(f"ID: {auditeur['auditeur_id']}, Salutation: {auditeur['salutation']}, Prénom: {auditeur['auditeur_prenom']}, Nom: {auditeur['auditeur_nom']}, Téléphone: {auditeur['auditeur_tel']}, Email: {auditeur['auditeur_email']}")

    cursor.close()
    cnx.close()


def modifier_auditeur():
    cnx, cursor = create_connection(dictionary=True)

    auditeur_id = input("Entrez l'ID de l'auditeur à modifier: ")
    cursor.execute(f"SELECT * FROM auditeurs WHERE auditeur_id = {auditeur_id}")
    details = cursor.fetchone()

    if not details:
        print("Auditeur non trouvé!")
        return

    print("Détails actuels:")
    for key, value in details.items():
        print(f"{key}: {value}")

    print("\nEntrez les nouvelles informations (laissez vide pour ne pas changer):")
    salutation_id = input("ID de salutation: ") or details['auditeur_salutation_id']
    prenom = input("Prénom: ") or details['auditeur_prenom']
    nom = input("Nom: ") or details['auditeur_nom']
    tel = input("Numéro de téléphone: ") or details['auditeur_tel']
    email = input("Email: ") or details['auditeur_email']
    login_id = input("ID de connexion: ") or details['auditeur_login_id']
    permissions = input("Permissions: ") or details['auditeur_permissions']

    cursor.execute("""
        UPDATE auditeurs 
        SET auditeur_salutation_id = %s, auditeur_prenom = %s, auditeur_nom = %s, auditeur_tel = %s, auditeur_email = %s, auditeur_login_id = %s, auditeur_permissions = %s
        WHERE auditeur_id = %s
    """, (salutation_id, prenom, nom, tel, email, login_id, permissions, auditeur_id))

    cnx.commit()
    print("Auditeur modifié avec succès!")
    cursor.close()
    cnx.close()


def supprimer_auditeur():
    cnx, cursor = create_connection()

    auditeur_id = input("Entrez l'ID de l'auditeur à supprimer: ")
    sure = input("Êtes-vous sûr de vouloir supprimer cet auditeur? (Oui/Non): ").lower()

    if sure == 'oui':
        cursor.execute(f"DELETE FROM auditeurs WHERE auditeur_id = {auditeur_id}")
        cnx.commit()
        print("Auditeur supprimé avec succès!")
    else:
        print("Opération annulée.")

    cursor.close()
    cnx.close()


def voir_auditeur():
    cnx, cursor = create_connection(dictionary=True)

    auditeur_id = input("Entrez l'ID de l'auditeur que vous souhaitez voir: ")
    cursor.execute("""
        SELECT auditeurs.*, salutations.salutation 
        FROM auditeurs 
        LEFT JOIN salutations ON auditeurs.auditeur_salutation_id = salutations.salutation_id 
        WHERE auditeur_id = %s
    """, (auditeur_id,))
    details = cursor.fetchone()

    if not details:
        print("Auditeur non trouvé!")
        return

    print("Détails de l'auditeur:")
    for key, value in details.items():
        if key != "auditeur_salutation_id":
            print(f"{key}: {value}")

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    while True:
        print("\nGestion des auditeurs:")
        print("1. Ajouter un auditeur")
        print("2. Afficher les auditeurs")
        print("3. Modifier un auditeur")
        print("4. Voir un auditeur")
        print("5. Supprimer un auditeur")
        print("6. Quitter")
        
        choix = input("\nEntrez votre choix: ")

        if choix == '1':
            ajouter_auditeur()
        elif choix == '2':
            afficher_auditeurs()
        elif choix == '3':
            modifier_auditeur()
        elif choix == '4':
            voir_auditeur()
        elif choix == '5':
            supprimer_auditeur()
        elif choix == '6':
            break
        else:
            print("Choix non valide!")
