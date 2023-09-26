import mysql.connector
from db_utils import create_connection

def creer_audit():
    cnx, cursor = create_connection()

    # 1. Collecter les informations de l'utilisateur
    client_id = input("Entrez l'ID du client: ")
    date_audit = input("Entrez la date de l'audit (AAAA-MM-JJ): ")
    client_contact_id = input("Entrez l'ID du contact client: ")
    gestionnaire_id = input("Entrez l'ID du gestionnaire: ")
    auditeur_id = input("Entrez l'ID de l'auditeur: ")
    restaurant_id = input("Entrez l'ID du restaurant: ")
    nombre_de_couverts = input("Entrez le nombre de couverts: ")

    # Valeurs par défaut pour les heures de début et de fin
    horaires_du_self_debut = "11:30:00"
    horaires_du_self_fin = "14:00:00"

    # Vérifier si l'utilisateur souhaite remplacer les horaires par défaut
    remplacer_horaires = input("Souhaitez-vous remplacer les horaires par défaut? (oui/non): ").lower()
    if remplacer_horaires == 'oui':
        horaires_du_self_debut = input(f"Entrez l'heure de début (par défaut {horaires_du_self_debut}): ") or horaires_du_self_debut
        horaires_du_self_fin = input(f"Entrez l'heure de fin (par défaut {horaires_du_self_fin}): ") or horaires_du_self_fin

    responses = gather_responses()

    try:
        cursor.execute("""
            INSERT INTO audits (client_id, date_audit, client_contact_id, gestionnaire_id, auditeur_id, restaurant_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (client_id, date_audit, client_contact_id, gestionnaire_id, auditeur_id, restaurant_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin))

        audit_id = cursor.lastrowid

        for response in responses:
            cursor.execute("""
                INSERT INTO constats (constat, audit_id)
                VALUES (%s, %s)
            """, (response, audit_id))

        cnx.commit()
        print("Audit créé avec succès!")

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

def gather_responses():
    responses = []
    for i in range(3):
        response = int(input(f"Entrez la réponse à la question {i+1} (en chiffre): "))
        responses.append(response)
    return responses

if __name__ == '__main__':
    creer_audit()
