import mysql.connector
from db_utils import create_connection

def menu():
    print("\nGestion des audits:")
    print("1. Ajouter un audit")
    print("2. Afficher les audits")
    print("3. Voir un audit")
    print("4. Modifier un audit")
    print("5. Supprimer un audit")
    print("6. Quitter")
    choix = input("\nEntrez votre choix: ")
    return choix


def ajouter_audit(data):
    cnx, cursor = create_connection(dictionary=True)

    # 1. Collecter les informations de l'utilisateur
    client_id = data['client_id']
    date_audit = data['date_audit']
    client_contact_id = data['client_contact_id']
    gestionnaire_id = data['gestionnaire_id']
    auditeur_id = data['auditeur_id']
    restaurant_id = data['restaurant_id']
    nombre_de_couverts = data['nombre_de_couverts']

    # Valeurs par défaut pour les heures de début et de fin
    horaires_du_self_debut = "11:30:00"
    horaires_du_self_fin = "14:00:00"

    # Vérifier si l'utilisateur souhaite remplacer les horaires par défaut
    remplacer_horaires = input("Souhaitez-vous remplacer les horaires par défaut? (oui/non): ").lower()
    if remplacer_horaires == 'oui':
        horaires_du_self_debut = input(f"Entrez l'heure de début (par défaut {horaires_du_self_debut}): ") or horaires_du_self_debut
        horaires_du_self_fin = input(f"Entrez l'heure de fin (par défaut {horaires_du_self_fin}): ") or horaires_du_self_fin

    try:
        cursor.execute("""
            INSERT INTO audits (client_id, date_audit, client_contact_id, gestionnaire_id, auditeur_id, restaurant_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (client_id, date_audit, client_contact_id, gestionnaire_id, auditeur_id, restaurant_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin))

        audit_id = cursor.lastrowid
        cnx.commit()
        print("Audit créé avec succès!")

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

    # Re-open the connection for the questions
    cnx, cursor = create_connection(dictionary=True)

    try:
        # Prompt the auditor to answer the first 10 questions from the elements table
        cursor.execute("SELECT * FROM elements LIMIT 10")
        questions = cursor.fetchall()

        for question in questions:
            print(f"Question: {question['element_nom']}")
            cursor.execute("SELECT * FROM reponses_possibles")
            options = cursor.fetchall()
            for option in options:
                print(f"{option['response_id']}. {option['response_value']}")

            response = input("Entrez votre réponse (ID de la réponse possible): ")
            constat_description = input("Entrez une description pour ce constat: ")

            cursor.execute("""
                INSERT INTO constats (observations, element_id, audit_id, score)
                VALUES (%s, %s, %s, %s)
            """, (constat_description, question['element_id'], audit_id, response))

            cnx.commit()
            print("Audit créé avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()


def afficher_audits():
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("""
        SELECT audits.audit_id, clients.client_nom, gestionnaires.gestionnaire_nom, auditeurs.auditeur_prenom, 
               auditeurs.auditeur_nom, elements.element_nom, restaurants.restaurant_nom, audits.date_audit,
               client_contacts.client_contact_prenom, client_contacts.client_contact_nom, audits.nombre_de_couverts,
               audits.horaires_du_self_debut, audits.horaires_du_self_fin
        FROM audits
        LEFT JOIN clients ON audits.client_id = clients.client_id
        LEFT JOIN gestionnaires ON audits.gestionnaire_id = gestionnaires.gestionnaire_id
        LEFT JOIN auditeurs ON audits.auditeur_id = auditeurs.auditeur_id
        LEFT JOIN elements ON audits.chapitre = elements.element_id
        LEFT JOIN restaurants ON audits.restaurant_id = restaurants.restaurant_id
        LEFT JOIN client_contacts ON audits.client_contact_id = client_contacts.client_contact_id
    """)
    
    audits = cursor.fetchall()

    if not audits:
        print("Aucun audit trouvé!")
        return

    print("Liste des audits:")
    for audit in audits:
        print("-" * 40)
        for key, value in audit.items():
            print(f"{key}: {value}")
        
        # Create a new cursor for fetching constats
        inner_cursor = cnx.cursor(dictionary=True)
        
        # Fetch constats for the audit with descriptions
        inner_cursor.execute("""
            SELECT constats.constat, e.element_nom, rp.response_value AS score
            FROM constats
            LEFT JOIN elements e ON constats.element_id = e.element_id
            LEFT JOIN reponses_possibles rp ON constats.score = rp.response_id
            WHERE audit_id = %s
        """, (audit['audit_id'],))
        constats = inner_cursor.fetchall()
        inner_cursor.close()
        
        if constats:
            print("\nConstats associés à cet audit:")
            for constat in constats:
                print(f"- Question: {constat['element_nom']}, Réponse: {constat['score']}, Description: {constat['constat']}")
        print("-" * 40)

    cursor.close()
    cnx.close()
    

def visualiser_audit(audit_id):
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("""
        SELECT audits.audit_id, clients.client_nom, gestionnaires.gestionnaire_nom, auditeurs.auditeur_prenom, 
               auditeurs.auditeur_nom, elements.element_nom, restaurants.restaurant_nom, audits.date_audit,
               client_contacts.client_contact_prenom, client_contacts.client_contact_nom, audits.nombre_de_couverts,
               audits.horaires_du_self_debut, audits.horaires_du_self_fin
        FROM audits
        LEFT JOIN clients ON audits.client_id = clients.client_id
        LEFT JOIN gestionnaires ON audits.gestionnaire_id = gestionnaires.gestionnaire_id
        LEFT JOIN auditeurs ON audits.auditeur_id = auditeurs.auditeur_id
        LEFT JOIN elements ON audits.chapitre = elements.element_id
        LEFT JOIN restaurants ON audits.restaurant_id = restaurants.restaurant_id
        LEFT JOIN client_contacts ON audits.client_contact_id = client_contacts.client_contact_id
        WHERE audits.audit_id = %s
    """, (audit_id,))
    
    audit = cursor.fetchone()

    if not audit:
        print("Audit non trouvé!")
        return
    print("Détails de l'audit:")
    for key, value in audit.items():
        print(f"{key}: {value}")
    
    # Fetch constats for the audit with descriptions
    cursor.execute("""
        SELECT constats.constat, e.element_nom, rp.response_value AS score
        FROM constats
        LEFT JOIN elements e ON constats.element_id = e.element_id
        LEFT JOIN reponses_possibles rp ON constats.score = rp.response_id
        WHERE audit_id = %s
    """, (audit_id,))
    constats = cursor.fetchall()
    
    if constats:
        print("\nConstats associés à cet audit:")
        for constat in constats:
            print(f"- Question: {constat['element_nom']}, Réponse: {constat['score']}, Description: {constat['constat']}")

    cursor.close()
    cnx.close()



def changer_audit():
    cnx, cursor = create_connection(dictionary=True)

    audit_id = input("Entrez l'ID de l'audit à modifier: ")

    cursor.execute("SELECT * FROM audits WHERE audit_id = %s", (audit_id,))
    audit = cursor.fetchone()

    if not audit:
        print("Audit non trouvé!")
        return

    print("Laissez le champ vide pour conserver la valeur actuelle.")
    for key in audit.keys():
        if key != "audit_id":
            new_value = input(f"{key} (actuel: {audit[key]}): ")
            if new_value:
                audit[key] = new_value

    cursor.execute("""
        UPDATE audits
        SET client_id=%s, gestionnaire_id=%s, auditeur_id=%s, chapitre=%s,
            restaurant_id=%s, date_audit=%s, client_contact_id=%s, nombre_de_couverts=%s,
            horaires_du_self_debut=%s, horaires_du_self_fin=%s
        WHERE audit_id=%s
    """, (audit['client_id'], audit['gestionnaire_id'], audit['auditeur_id'], audit['chapitre'],
          audit['restaurant_id'], audit['date_audit'], audit['client_contact_id'], 
          audit['nombre_de_couverts'], audit['horaires_du_self_debut'], audit['horaires_du_self_fin'],
          audit_id))

    cnx.commit()
    print("Audit modifié avec succès!")
    cursor.close()
    cnx.close()


def supprimer_audit():
    cnx, cursor = create_connection()

    audit_id = input("Entrez l'ID de l'audit à supprimer: ")
    confirmation = input(f"Êtes-vous sûr de vouloir supprimer l'audit {audit_id}? (oui/non): ")

    if confirmation.lower() == 'oui':
        cursor.execute("DELETE FROM audits WHERE audit_id = %s", (audit_id,))
        cnx.commit()
        print("Audit supprimé avec succès!")
    else:
        print("Suppression annulée!")

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    while True:
        user_choice = menu()
        if user_choice == '1':
            ajouter_audit()
        elif user_choice == '2':
            afficher_audits()
        elif user_choice == '3':
            audit_id = input("Entrez l'ID de l'audit que vous souhaitez voir: ")
            visualiser_audit(audit_id)
        elif user_choice == '4':
            changer_audit()
        elif user_choice == '5':
            supprimer_audit()
        elif user_choice == '6':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

