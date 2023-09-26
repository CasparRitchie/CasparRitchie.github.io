import mysql.connector
from db_utils import create_connection

from gestion_audits import ajouter_audit, get_all_audits, get_constats_for_audit, afficher_audits, visualiser_audit, modifier_audit, supprimer_audit


def save_audit_details(audit_info):
    return ajouter_audit(audit_info)


def fetch_audit_structure():
    # Connect to the audit_responses_db
    cnx, cursor = create_connection(dictionary=True)

    audit_structure = []

    try:
        # Fetch distinct chapitres
        cursor.execute("SELECT DISTINCT chapitre FROM elements ORDER BY chapitre")
        chapitres = cursor.fetchall()

        for chapitre_record in chapitres:
            chapitre_name = chapitre_record["chapitre"]
            chapitre_data = {
                "chapitre": chapitre_name,
                "titres": []
            }

            cursor.execute("SELECT DISTINCT titre FROM elements WHERE chapitre = %s ORDER BY titre", (chapitre_name,))
            titres = cursor.fetchall()
            for titre_record in titres:
                titre_name = titre_record["titre"]
                titre_data = {
                    "titre": titre_name,
                    "elements": []
                }

                cursor.execute("""
                    SELECT sous_titre, element_nom, notes_structure_id 
                    FROM elements 
                    WHERE chapitre = %s AND titre = %s 
                    ORDER BY sous_titre
                """, (chapitre_name, titre_name))
                elements = cursor.fetchall()
                for element_record in elements:
                    titre_data["elements"].append({
                        "sous_titre": element_record["sous_titre"],
                        "element_nom": element_record["element_nom"],
                        "notes_structure_id": element_record["notes_structure_id"]
                    })

                chapitre_data["titres"].append(titre_data)

            audit_structure.append(chapitre_data)

    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}

    finally:
        cursor.close()
        cnx.close()

    return audit_structure


def save_constat(element_id, constat_info):
    # Logic to save constat details for a specific element.
    pass


def delete_section(section_type, section_id):
    # Logic to delete a specific section.
    pass


def generate_csv(audit_id):
    # Logic to export the audit details into a CSV.
    pass


def calculate_progress(audit_id):
    # Logic to calculate the progress of an audit.
    pass
