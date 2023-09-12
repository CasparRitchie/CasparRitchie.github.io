# UNIQUEMENT ADMIN

import mysql.connector
import pandas as pd
from db_utils import create_connection


def mettre_a_jour_questions(df):
    cnx, cursor = create_connection()

    # Clear the entries from the elements table
    try:
        cursor.execute("DELETE FROM elements")
    except mysql.connector.Error as err:
        print(f"Error while clearing the elements table: {err}")
        cnx.rollback()

    # For each row in the dataframe, insert the data into the elements table
    for _, row in df.iterrows():
        chapitre = row['chapitre']
        titre = row['titre']
        sous_titre = row['sous_titre'] if not pd.isna(row['sous_titre']) else None  # Handling NaN values
        element_nom = row['element_nom']

        try:
            cursor.execute("""
                INSERT INTO elements (chapitre, titre, sous_titre, element_nom)
                VALUES (%s, %s, %s, %s)
            """, (chapitre, titre, sous_titre, element_nom))
        except mysql.connector.Error as err:
            print(f"Error while inserting row: {err}")
            cnx.rollback()

    # Commit the changes
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Data from CSV inserted successfully!")

# Load the CSV data
data_questions = pd.read_csv('data_questions.csv', delimiter=';')

# Call the function to insert data
mettre_a_jour_questions(data_questions)
