import mysql.connector
from db_utils import create_connection


def insert_elements():
    # Connect to the audit_responses_db
    cnx, cursor = create_connection()

    try:
        # We'll use the chapitres, titres, and sous-titres already in the table as our base.
        cursor.execute("SELECT DISTINCT chapitre FROM elements ORDER BY chapitre")
        chapitres = cursor.fetchall()

        for (chapitre,) in chapitres:
            cursor.execute("SELECT DISTINCT titre FROM elements WHERE chapitre = %s ORDER BY titre", (chapitre,))
            titres = cursor.fetchall()
            for (titre,) in titres:
                cursor.execute("SELECT DISTINCT sous_titre FROM elements WHERE chapitre = %s AND titre = %s ORDER BY sous_titre", (chapitre, titre))
                sous_titres = cursor.fetchall()
                for (sous_titre,) in sous_titres:
                    # Inserting multiple elements for each chapitre, titre, and sous-titre combination
                    for i in range(1, 11): # This will insert 10 elements for each combination
                        element_nom = f"element_{chapitre[-1]}_{titre[-1]}_{sous_titre[-1]}_{i}"  # Example naming convention
                        cursor.execute("""
                            INSERT INTO elements (chapitre, titre, sous_titre, element_nom) 
                            VALUES (%s, %s, %s, %s)
                        """, (chapitre, titre, sous_titre, element_nom))

        cnx.commit()
        print("Elements inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    insert_elements()
