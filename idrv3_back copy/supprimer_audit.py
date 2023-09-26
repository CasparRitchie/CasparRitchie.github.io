import mysql.connector
from db_utils import create_connection

def supprimer_audit():
    cnx, cursor = create_connection(dictionary=True)
    
    # 1. Prompt the user for the audit ID
    audit_id = input("Entrez l'ID de l'audit à supprimer: ")

    # Fetch audit details
    cursor.execute(f"SELECT * FROM audits WHERE audit_id = {audit_id}")
    audit_details = cursor.fetchone()

    if not audit_details:
        print("Aucun audit trouvé avec cet ID.")
        return

    # 2. Display the audit details for confirmation
    print("\nDétails actuels de l'audit:")
    for key, value in audit_details.items():
        print(f"{key}: {value}")

    # 3. Ask the user for confirmation
    confirmation = input("\nÊtes-vous sûr de vouloir supprimer cet audit? (Oui/Non): ").lower()

    if confirmation == 'oui':
        # 4. Delete the audit
        cursor.execute(f"DELETE FROM audits WHERE audit_id = {audit_id}")
        cnx.commit()
        print(f"Audit {audit_id} supprimé avec succès.")
    else:
        print("Opération annulée.")

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    supprimer_audit()
