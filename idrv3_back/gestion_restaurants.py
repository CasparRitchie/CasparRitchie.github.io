import mysql.connector
from db_utils import create_connection

def ajouter_restaurant(data):
    cnx, cursor = create_connection()

    # Extract data from the provided payload
    restaurant_nom = data["restaurant_nom"]
    restaurant_adresse1 = data["restaurant_adresse1"]
    restaurant_adresse2 = data.get("restaurant_adresse2", "")  # .get() to handle optional fields
    restaurant_adresse3 = data.get("restaurant_adresse3", "")
    restaurant_cp = data["restaurant_cp"]
    restaurant_ville = data["restaurant_ville"]
    restaurant_coords = data["restaurant_coords"]
    client_id = data["client_id"]

    try:
        # Insert into restaurants table
        cursor.execute("""
            INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_adresse2, 
                                     restaurant_adresse3, restaurant_cp, restaurant_ville, 
                                     restaurant_coords, client_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (restaurant_nom, restaurant_adresse1, restaurant_adresse2, restaurant_adresse3,
              restaurant_cp, restaurant_ville, restaurant_coords, client_id))

        cnx.commit()
        cursor.close()
        cnx.close()
        return {"message": "Restaurant ajouté avec succès!"}
    except Exception as e:
        return {"error": str(e)}



def afficher_restaurants():
    cnx, cursor = create_connection(dictionary=True)
    
    cursor.execute("SELECT * FROM restaurants")
    results = cursor.fetchall()

    cursor.close()
    cnx.close()
    return results

def modifier_restaurant(restaurant_id, updated_data):
    cnx, cursor = create_connection()

    # 1. Fetch Current Data
    cursor.execute("SELECT * FROM restaurants WHERE restaurant_id = %s", (restaurant_id,))
    current_data = cursor.fetchone()

    columns = ["restaurant_nom", "restaurant_adresse1", "restaurant_adresse2", 
               "restaurant_adresse3", "restaurant_cp", "restaurant_ville", 
               "restaurant_coords", "client_id"]  # Add other column names as required.

    current_data_dict = dict(zip(columns, current_data))

    # 2. Merge Data with Updated Data
    # If a value is None in the updated_data, use the original value from the database.
    merged_data = {key: updated_data.get(key, current_data_dict[key]) for key in columns}

    # 3. Update the Database
    # Only update the fields provided in the updated_data to prevent overriding other fields.
    update_columns = ", ".join(f"{key} = %s" for key in updated_data.keys())
    sql_update_query = f"UPDATE restaurants SET {update_columns} WHERE restaurant_id = %s"
    
    values = [merged_data[key] for key in updated_data.keys()]
    values.append(restaurant_id)
    
    cursor.execute(sql_update_query, values)
    cnx.commit()

    cursor.close()
    cnx.close()

    return {"message": "Restaurant updated successfully!"}





def visualiser_restaurant(restaurant_id):
    cnx, cursor = create_connection(dictionary=True)

    # No need to prompt the user for restaurant_id as we're passing it now
    cursor.execute("SELECT * FROM restaurants WHERE restaurant_id = %s", (restaurant_id,))
    restaurant = cursor.fetchone()

    if not restaurant:
        print("Restaurant non trouvé!")
        return

    print("Détails du restaurant:")
    for key, value in restaurant.items():
        print(f"{key}: {value}")

    cursor.close()
    cnx.close()
    return restaurant  # Ensure you return the fetched restaurant



def supprimer_restaurant(restaurant_id):
    cnx, cursor = create_connection()

    try:
        cursor.execute("DELETE FROM restaurants WHERE restaurant_id = %s", (restaurant_id,))
        cnx.commit()
        message = "Restaurant supprimé avec succès!"
    except mysql.connector.Error as err:
        message = f"Error: {err}"
    finally:
        cursor.close()
        cnx.close()
    
    return {"message": message}




if __name__ == '__main__':
    while True:
        print("\nGestion des restaurants:")
        print("1. Ajouter un restaurant")
        print("2. Afficher les restaurants")
        print("3. Modifier un restaurant")
        print("4. Voir un restaurant")
        print("5. Supprimer un restaurant")
        print("6. Quitter")

        choix = input("Entrez votre choix: ")

        if choix == "1":
            ajouter_restaurant()
        elif choix == "2":
            afficher_restaurants()
        elif choix == "3":
            modifier_restaurant()
        elif choix == "4":
            visualiser_restaurant()
        elif choix == "5":
            supprimer_restaurant()
        elif choix == "6":
            break
