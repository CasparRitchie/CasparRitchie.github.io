import mysql.connector
from db_utils import create_connection

def ajouter_restaurant():
    cnx, cursor = create_connection()

    # Gather data from the user
    restaurant_nom = input("Entrez le nom du restaurant: ")
    restaurant_adresse1 = input("Entrez l'adresse 1 du restaurant: ")
    restaurant_adresse2 = input("Entrez l'adresse 2 du restaurant (laissez vide si inexistante): ")
    restaurant_adresse3 = input("Entrez l'adresse 3 du restaurant (laissez vide si inexistante): ")
    restaurant_cp = input("Entrez le code postal du restaurant: ")
    restaurant_ville = input("Entrez la ville du restaurant: ")
    restaurant_coords = input("Entrez les coordonnées du restaurant (par exemple, lat,long): ")
    client_id = input("Entrez l'ID du client associé au restaurant: ")

    # Insert into restaurants table
    cursor.execute("""
        INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_adresse2, 
                                 restaurant_adresse3, restaurant_cp, restaurant_ville, 
                                 restaurant_coords, client_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (restaurant_nom, restaurant_adresse1, restaurant_adresse2, restaurant_adresse3,
          restaurant_cp, restaurant_ville, restaurant_coords, client_id))

    cnx.commit()

    print("Restaurant ajouté avec succès!")
    cursor.close()
    cnx.close()


def afficher_restaurants():
    cnx, cursor = create_connection(dictionary=True)
    
    cursor.execute("SELECT * FROM restaurants")
    results = cursor.fetchall()

    for restaurant in results:
        print(restaurant)

    cursor.close()
    cnx.close()


def modifier_restaurant():
    cnx, cursor = create_connection(dictionary=True)

    # Ask user for restaurant ID
    restaurant_id = input("Entrez l'ID du restaurant à modifier: ")

    # Fetch the current details of the restaurant
    cursor.execute("SELECT * FROM restaurants WHERE restaurant_id = %s", (restaurant_id,))
    restaurant = cursor.fetchone()
    if not restaurant:
        print("Restaurant non trouvé!")
        return

    print("Détails actuels du restaurant:")
    for key, value in restaurant.items():
        print(f"{key}: {value}")

    # Prompt user for new details
    restaurant_nom = input(f"Entrez le nouveau nom du restaurant ({restaurant['restaurant_nom']}): ") or restaurant['restaurant_nom']
    restaurant_adresse1 = input(f"Entrez la nouvelle adresse 1 du restaurant ({restaurant['restaurant_adresse1']}): ") or restaurant['restaurant_adresse1']
    restaurant_adresse2 = input(f"Entrez la nouvelle adresse 2 du restaurant ({restaurant['restaurant_adresse2']}): ") or restaurant['restaurant_adresse2']
    restaurant_adresse3 = input(f"Entrez la nouvelle adresse 3 du restaurant ({restaurant['restaurant_adresse3']}): ") or restaurant['restaurant_adresse3']
    restaurant_cp = input(f"Entrez le nouveau code postal du restaurant ({restaurant['restaurant_cp']}): ") or restaurant['restaurant_cp']
    restaurant_ville = input(f"Entrez la nouvelle ville du restaurant ({restaurant['restaurant_ville']}): ") or restaurant['restaurant_ville']
    restaurant_coords = input(f"Entrez les nouvelles coordonnées du restaurant ({restaurant['restaurant_coords']}): ") or restaurant['restaurant_coords']
    client_id = input(f"Entrez le nouvel ID du client associé au restaurant ({restaurant['client_id']}): ") or restaurant['client_id']

    # Update the restaurant details
    cursor.execute("""
        UPDATE restaurants
        SET restaurant_nom = %s, restaurant_adresse1 = %s, restaurant_adresse2 = %s,
            restaurant_adresse3 = %s, restaurant_cp = %s, restaurant_ville = %s,
            restaurant_coords = %s, client_id = %s
        WHERE restaurant_id = %s
    """, (restaurant_nom, restaurant_adresse1, restaurant_adresse2, restaurant_adresse3, 
          restaurant_cp, restaurant_ville, restaurant_coords, client_id, restaurant_id))

    cnx.commit()
    print("Restaurant modifié avec succès!")
    cursor.close()
    cnx.close()


def voir_restaurant():
    cnx, cursor = create_connection(dictionary=True)

    restaurant_id = input("Entrez l'ID du restaurant que vous souhaitez voir: ")
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


def supprimer_restaurant():
    cnx, cursor = create_connection()

    restaurant_id = input("Entrez l'ID du restaurant à supprimer: ")

    # Confirm deletion
    confirmation = input("Êtes-vous sûr de vouloir supprimer ce restaurant? (Oui/Non): ").lower()
    if confirmation != 'oui':
        print("Opération annulée.")
        return

    cursor.execute("DELETE FROM restaurants WHERE restaurant_id = %s", (restaurant_id,))
    cnx.commit()

    print("Restaurant supprimé avec succès!")
    cursor.close()
    cnx.close()




# ... [main execution block]


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
            voir_restaurant()
        elif choix == "5":
            supprimer_restaurant()
        elif choix == "6":
            break
