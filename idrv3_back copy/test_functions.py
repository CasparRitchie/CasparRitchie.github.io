# import mysql.connector
# from datetime import datetime
# from db_utils import create_connection


# def test_heure_du_constat_insertion():
#     # Create a connection
#     cnx, cursor = create_connection()
    
#     # Generate a timestamp
#     heure_du_constat = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     print("Timestamp being inserted:", heure_du_constat)
    
#     try:
#         # Insert a dummy record into constats with the generated timestamp
#         cursor.execute("""
#             INSERT INTO constats (heure_du_constat)
#             VALUES (%s)
#         """, (heure_du_constat,))
#         cnx.commit()
#         print("Record inserted successfully!")
        
#         # Now fetch the last record and check the heure_du_constat value
#         cursor.execute("SELECT heure_du_constat FROM constats ORDER BY constat_id DESC LIMIT 1")
#         result = cursor.fetchone()
#         if result:
#             print("Timestamp in database:", result[0])
#         else:
#             print("Could not fetch the last record.")
        
#     except mysql.connector.Error as err:
#         print(f"Erreur: {err}")
#         cnx.rollback()
        
#     finally:
#         cursor.close()
#         cnx.close()

# # NOTE: Before running this function, ensure that:
# # - The `create_connection()` function is defined and working
# # - The `constats` table can accept a record with only the `heure_du_constat` column (i.e., other columns can be null or have default values)
import mysql.connector
from datetime import datetime
from db_utils import create_connection


def test_heure_du_constat_insertion():
    # Create a connection
    cnx, cursor = create_connection()
    
    # Generate a timestamp
    heure_du_constat = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Timestamp being inserted:", heure_du_constat)
    
    try:
        # Insert a dummy record into constats with the generated timestamp
        cursor.execute("""
        INSERT INTO constats (heure_du_constat) VALUES (NOW());            VALUES (%s)
        """, (heure_du_constat,))
        cnx.commit()
        print("Record inserted successfully!")
        
        # Now fetch the last record and check the heure_du_constat value
        cursor.execute("SELECT heure_du_constat FROM constats ORDER BY constat_id DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
            print("Timestamp in database:", result[0])
        else:
            print("Could not fetch the last record.")
        
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        cnx.rollback()
        
    finally:
        cursor.close()
        cnx.close()

# NOTE: Before running this function, ensure that:
# - The `create_connection()` function is defined and working
# - The `constats` table can accept a record with only the `heure_du_constat` column (i.e., other columns can be null or have default values)

