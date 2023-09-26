import mysql.connector
from db_utils import create_connection


def visualiser_questions():
    # Connect to the audit_responses_db
    cnx, cursor = create_connection()

    try:
        # Fetch distinct chapitres
        cursor.execute("SELECT DISTINCT chapitre FROM elements ORDER BY chapitre")
        chapitres = cursor.fetchall()

        for (chapitre,) in chapitres:
            print(f"Chapitre: {chapitre}")
            cursor.execute("SELECT DISTINCT titre FROM elements WHERE chapitre = %s ORDER BY titre", (chapitre,))
            titres = cursor.fetchall()
            for (titre,) in titres:
                print(f"\tTitre: {titre}")
                cursor.execute("""
                    SELECT sous_titre, element_nom 
                    FROM elements 
                    WHERE chapitre = %s AND titre = %s 
                    ORDER BY sous_titre
                """, (chapitre, titre))
                elements = cursor.fetchall()
                for sous_titre, element_nom in elements:
                    print(f"\t\tSous-titre: {sous_titre}")
                    print(f"\t\tElement: {element_nom}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    visualiser_questions()
