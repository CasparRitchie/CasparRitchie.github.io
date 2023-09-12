import mysql.connector
from db_utils import create_connection

def changer_audit():
    cnx, cursor = create_connection(dictionary=True)

    # 1. Demander l'ID de l'audit à modifier
    audit_id = input("Entrez l'ID de l'audit à modifier: ")

    # 2. Afficher les détails actuels de l'audit
    cursor.execute(f"SELECT * FROM audits WHERE audit_id = {audit_id}")
    audit_details = cursor.fetchone()

    if not audit_details:
        print("Aucun audit trouvé avec cet ID.")
        return

    print("\nDétails actuels de l'audit:")
    for key, value in audit_details.items():
        print(f"{key}: {value}")

    # 3. Permettre à l'utilisateur de modifier les détails
    print("\nEntrez les nouvelles valeurs (laissez vide pour ne pas changer):")
    new_values = {}
    for key, value in audit_details.items():
        if key != "audit_id":  # We shouldn't change the primary key
            new_value = input(f"{key} ({value}): ")
            if new_value:
                new_values[key] = new_value

    # 4. Mettre à jour la base de données avec les nouvelles informations
    update_query = "UPDATE audits SET "
    update_query += ", ".join([f"{key} = %s" for key in new_values.keys()])
    update_query += f" WHERE audit_id = {audit_id}"
    
    try:
        cursor.execute(update_query, tuple(new_values.values()))
        cnx.commit()
        print("Audit mis à jour avec succès!")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()

    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    changer_audit()
