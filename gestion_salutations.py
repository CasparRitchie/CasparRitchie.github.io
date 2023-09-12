from db_utils import create_connection

def ajouter_salutation(salutation):
    cnx, cursor = create_connection()
    
    # Check if the salutation already exists
    cursor.execute("SELECT 1 FROM salutations WHERE salutation = %s", (salutation,))
    exists = cursor.fetchone()
    if exists:
        cursor.close()
        cnx.close()
        return False  # Return False to indicate the salutation already exists
    
    # If not exists, then insert
    cursor.execute("INSERT INTO salutations (salutation) VALUES (%s)", (salutation,))
    cnx.commit()
    
    print(f"Salutation '{salutation}' ajoutée avec succès.")
    
    cursor.close()
    cnx.close()
    return True  # Return True to indicate successful insertion


def visualiser_salutation(salutation_id):
    cnx, cursor = create_connection(dictionary=True)
    
    cursor.execute("SELECT * FROM salutations WHERE salutation_id = %s", (salutation_id,))
    salutation = cursor.fetchone()

    cursor.close()
    cnx.close()
    return salutation


def afficher_salutations():
    cnx, cursor = create_connection(dictionary=True)
    
    cursor.execute("SELECT * FROM salutations")
    salutations = cursor.fetchall()

    cursor.close()
    cnx.close()
    return salutations



def modifier_salutation(salutation_id, nouvelle_salutation):
    cnx, cursor = create_connection()

    cursor.execute("UPDATE salutations SET salutation = %s WHERE salutation_id = %s", (nouvelle_salutation, salutation_id))
    cnx.commit()

    print(f"Salutation modifiée avec succès.")
    
    cursor.close()
    cnx.close()


def supprimer_salutation(salutation_id):
    cnx, cursor = create_connection()

    cursor.execute("DELETE FROM salutations WHERE salutation_id = %s", (salutation_id,))
    cnx.commit()

    print(f"Salutation supprimée avec succès.")
    
    cursor.close()
    cnx.close()



if __name__ == '__main__':
    while True:
        print("\nGestion des salutations:")
        print("1. Ajouter une salutation")
        print("2. Afficher les salutations")
        print("3. Modifier une salutation")
        print("4. Supprimer une salutation")
        print("5. Quitter")
        
        choix = input("\nEntrez votre choix: ")

        if choix == '1':
            ajouter_salutation()
        elif choix == '2':
            afficher_salutations()
        elif choix == '3':
            modifier_salutation()
        elif choix == '4':
            supprimer_salutation()
        elif choix == '5':
            break
        else:
            print("Choix non reconnu. Essayez à nouveau.")
