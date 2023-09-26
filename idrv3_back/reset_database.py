import mysql.connector
from creer_db_tables import creer_db_tables
from input_dummy_data import input_dummy_data
from mettre_a_jour_questions import mettre_a_jour_questions
from db_utils import create_connection


def reset_database():
    # Database configuration
    cnx, cursor = create_connection()

    try:
        # Drop the database if it exists
        cursor.execute("DROP DATABASE IF EXISTS audit_responses_db;")
        print("Database dropped successfully.")

        # Create the database
        cursor.execute("CREATE DATABASE audit_responses_db;")
        print("Database created successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

    # Call the functions to create tables and input dummy data
    creer_db_tables()
    input_dummy_data()


# Call the function
reset_database()