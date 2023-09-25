import mysql.connector
from db_utils import create_connection


def ajouter_legende(legende_name, chapitre, legende_elements):
    cnx, cursor = create_connection()
    try:
        cursor.execute("""
            INSERT INTO legendes (legende_name, chapitre, legende_elements)
            VALUES (%s, %s, %s)
        """, (legende_name, chapitre, legende_elements))
        cnx.commit()
        return {"status": "success", "message": "Légende ajoutée avec succès!"}
    except mysql.connector.Error as err:
        cnx.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        cnx.close()


def afficher_legendes():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM legendes")
    legendes = cursor.fetchall()
    cursor.close()
    cnx.close()
    return legendes


def visualiser_legende(legende_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM legendes WHERE legende_id = %s", (legende_id,))
    legende = cursor.fetchone()
    cursor.close()
    cnx.close()
    return legende


def modifier_legende(legende_id, updates):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM legendes WHERE legende_id = %s", (legende_id,))
    legende = cursor.fetchone()
    if not legende:
        return {"status": "error", "message": "Légende non trouvée!"}

    # Update values
    legende.update(updates)

    cursor.execute("""
        UPDATE legendes
        SET legende_name=%s, chapitre=%s, legende_elements=%s
        WHERE legende_id=%s
    """, (legende['legende_name'], legende['chapitre'], legende['legende_elements'], legende_id))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"status": "success", "message": "Légende modifiée avec succès!"}


def supprimer_legende(legende_id):
    cnx, cursor = create_connection()
    cursor.execute("DELETE FROM legendes WHERE legende_id = %s", (legende_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"status": "success", "message": "Légende supprimée avec succès!"}
