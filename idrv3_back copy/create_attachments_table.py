# creer_db_tables.py

import mysql.connector
from db_utils import create_connection


def creer_attachments_table():
    # Connect to the audit_responses_db
    cnx, cursor = create_connection()

    try:
        cursor.execute("""
        CREATE TABLE attachments (
    attachment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    constat_id INT REFERENCES constats(constat_id),
    file BLOB
);
                       """)
        print("creation de table OK.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()
creer_attachments_table()