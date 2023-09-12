import mysql.connector
from db_utils import create_connection

def menu():
    print("\nGestion des constats:")
    print("1. Ajouter un constat")
    print("2. Afficher les constats")
    print("3. Voir un constat")
    print("4. Modifier un constat")
    print("5. Supprimer un constat")
    print("6. Quitter")
    choix = input("\nEntrez votre choix: ")
    return choix

from datetime import datetime

def ajouter_constat():
    cnx, cursor = create_connection()

    constat = input("Entrez le constat: ")
    elements_audites_details_prestation_id = input("Entrez l'ID de l'élément audité détail prestation: ")
    element_id = input("Entrez l'ID de l'élément: ")

    # Automatically set the current timestamp for heure_du_constat
    score = input("Entrez le score (ID de la réponse possible): ")
    observations = input("Entrez les observations: ")
    audit_id = input("Entrez l'ID de l'audit: ")
    auditeur_id = input("Entrez l'ID de l'auditeur: ")
    print(heure_du_constat)

    try:
        heure_du_constat = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Timestamp being inserted:", heure_du_constat)

        cursor.execute("""
            INSERT INTO constats (constat, elements_audites_details_prestation_id, element_id, heure_du_constat, score, observations, audit_id, auditeur_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (constat, elements_audites_details_prestation_id, element_id, heure_du_constat, score, observations, audit_id, auditeur_id))
        cnx.commit()
        print("Constat ajouté avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()


def afficher_constats():
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("""
        SELECT constats.constat_id, constats.constat, 
               eadp.elements_audites_details_prestation_nom, e.element_nom, 
               constats.heure_du_constat, rp.response_value AS score, 
               constats.observations, a.date_audit, a.audit_id,
               aud.auditeur_prenom, aud.auditeur_nom, 
               GROUP_CONCAT(att.file) AS attached_files
        FROM constats
        LEFT JOIN elements_audites_details_prestations eadp ON constats.elements_audites_details_prestation_id = eadp.elements_audites_details_prestation_id
        LEFT JOIN elements e ON constats.element_id = e.element_id
        LEFT JOIN reponses_possibles rp ON constats.score = rp.response_id
        LEFT JOIN audits a ON constats.audit_id = a.audit_id
        LEFT JOIN auditeurs aud ON constats.auditeur_id = aud.auditeur_id
        LEFT JOIN attachments att ON constats.constat_id = att.constat_id
        GROUP BY constats.constat_id
        ORDER BY e.chapitre, e.titre, e.sous_titre
    """)

    constats = cursor.fetchall()

    if not constats:
        print("Aucun constat trouvé!")
        return

    print("Liste des constats:")
    for constat in constats:
        print("-" * 80)
        for key, value in constat.items():
            print(f"{key}: {value}")

    cursor.close()
    cnx.close()


def voir_constat():
    cnx, cursor = create_connection(dictionary=True)

    constat_id = input("Entrez l'ID du constat que vous souhaitez voir: ")

    cursor.execute("""
        SELECT constats.constat_id, a.audit_id, constats.constat, eadp.elements_audites_details_prestation_nom, e.element_nom, constats.heure_du_constat, 
               rp.response_value AS score, constats.observations, a.date_audit, aud.auditeur_prenom, aud.auditeur_nom, 
               GROUP_CONCAT(att.file) AS attached_files
        FROM constats
        LEFT JOIN elements_audites_details_prestations eadp ON constats.elements_audites_details_prestation_id = eadp.elements_audites_details_prestation_id
        LEFT JOIN elements e ON constats.element_id = e.element_id
        LEFT JOIN reponses_possibles rp ON constats.score = rp.response_id
        LEFT JOIN audits a ON constats.audit_id = a.audit_id
        LEFT JOIN auditeurs aud ON constats.auditeur_id = aud.auditeur_id
        LEFT JOIN attachments att ON constats.constat_id = att.constat_id
        WHERE constats.constat_id = %s
        GROUP BY constats.constat_id
    """, (constat_id,))
    
    constat = cursor.fetchone()

    if not constat:
        print("Constat non trouvé!")
        return

    print("Détails du constat:")
    for key, value in constat.items():
        print(f"{key}: {value}")

    cursor.close()
    cnx.close()




def modifier_constat():
    cnx, cursor = create_connection(dictionary=True)

    constat_id = input("Entrez l'ID du constat à modifier: ")

    cursor.execute("SELECT * FROM constats WHERE constat_id = %s", (constat_id,))
    constat = cursor.fetchone()

    if not constat:
        print("Constat non trouvé!")
        return

    print("Laissez le champ vide pour conserver la valeur actuelle.")
    for key in constat.keys():
        if key != "constat_id":
            new_value = input(f"{key} (actuel: {constat[key]}): ")
            if new_value:
                constat[key] = new_value

    cursor.execute("""
        UPDATE constats
        SET constat=%s, elements_audites_details_prestation_id=%s, element_id=%s, heure_du_constat=%s, score=%s, observations=%s, audit_id=%s, auditeur_id=%s
        WHERE constat_id=%s
    """, (constat['constat'], constat['elements_audites_details_prestation_id'], constat['element_id'], constat['heure_du_constat'], constat['score'], constat['observations'], constat['audit_id'], constat['auditeur_id'], constat_id))

    cnx.commit()
    print("Constat modifié avec succès!")
    cursor.close()
    cnx.close()

def supprimer_constat():
    cnx, cursor = create_connection()

    constat_id = input("Entrez l'ID du constat à supprimer: ")
    confirmation = input(f"Êtes-vous sûr de vouloir supprimer le constat {constat_id}? (oui/non): ")

    if confirmation.lower() == 'oui':
        cursor.execute("DELETE FROM constats WHERE constat_id = %s", (constat_id,))
        cnx.commit()
        print("Constat supprimé avec succès!")
    else:
        print("Suppression annulée!")

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    while True:
        user_choice = menu()
        if user_choice == '1':
            ajouter_constat()
        elif user_choice == '2':
            afficher_constats()
        elif user_choice == '3':
            voir_constat()
        elif user_choice == '4':
            modifier_constat()
        elif user_choice == '5':
            supprimer_constat()
        elif user_choice == '6':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
