import mysql.connector
import pandas as pd
from db_utils import create_connection


def visualiser_questions():
    # Connect to the audit_responses_db
    cnx, cursor = create_connection()

    try:
        # Fetch all data into a DataFrame
        query = """
            SELECT chapitre, titre, sous_titre, element_nom
            FROM elements
            ORDER BY chapitre, titre, sous_titre
        """
        df = pd.read_sql(query, cnx)

        # Structure the data (This is just a sample. Depending on your final structure, this may need modifications.)
        structured_data = {
            chapitre: {
                titre: df[(df['chapitre'] == chapitre) & (df['titre'] == titre)][['sous_titre', 'element_nom']].to_dict('records')
                for titre in df[df['chapitre'] == chapitre]['titre'].unique()
            }
            for chapitre in df['chapitre'].unique()
        }

        # Convert structured data to JSON format
        json_data = pd.DataFrame(structured_data).to_json(orient='split')

        return json_data

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    json_output = visualiser_questions()
    print(json_output)
