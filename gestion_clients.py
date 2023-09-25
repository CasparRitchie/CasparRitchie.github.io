import mysql.connector
from db_utils import create_connection

def ajouter_client(data):
    cnx, cursor = create_connection()

    nom = data.get('client_nom')
    logo = data.get('client_logo')
    adresse1 = data.get('client_adresse1')
    adresse2 = data.get('client_adresse2')
    adresse3 = data.get('client_adresse3')
    cp = data.get('client_cp')
    ville = data.get('client_ville')
    coords = data.get('client_coords')
    siret = data.get('client_siret')
    contact_principal = data.get('client_contact_principal')

    if not nom:
        return {"message": "Client name is required!"}

    try:
        cursor.execute("""
            INSERT INTO clients (client_nom, client_logo, client_adresse1, client_adresse2, client_adresse3, 
                                 client_cp, client_ville, client_coords, client_siret, client_contact_principal)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nom, logo, adresse1, adresse2, adresse3, cp, ville, coords, siret, contact_principal))
        cnx.commit()
        cursor.close()
        cnx.close()
        return {"message": "Client ajouté avec succès!"}
    except mysql.connector.Error as err:
        print("MySQL error:", err)
        return {"message": f"Erreur lors de l'ajout du client! Error: {err}"}

def afficher_clients():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    cursor.close()
    cnx.close()
    return clients

def modifier_client(client_id, data):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM clients WHERE client_id = %s", (client_id,))
    details = cursor.fetchone()

    if not details:
        return {"message": "Client non trouvé!"}

    new_nom = data.get('client_nom') or details['client_nom']
    new_logo = data.get('client_logo') or details['client_logo']
    new_adresse1 = data.get('client_adresse1') or details['client_adresse1']
    new_adresse2 = data.get('client_adresse2') or details['client_adresse2']
    new_adresse3 = data.get('client_adresse3') or details['client_adresse3']
    new_cp = data.get('client_cp') or details['client_cp']
    new_ville = data.get('client_ville') or details['client_ville']
    new_coords = data.get('client_coords') or details['client_coords']
    new_siret = data.get('client_siret') or details['client_siret']
    new_contact_principal = data.get('client_contact_principal') or details['client_contact_principal']

    cursor.execute("""
        UPDATE clients
        SET client_nom=%s, client_logo=%s, client_adresse1=%s, client_adresse2=%s, client_adresse3=%s, 
            client_cp=%s, client_ville=%s, client_coords=%s, client_siret=%s, client_contact_principal=%s
        WHERE client_id=%s
    """, (new_nom, new_logo, new_adresse1, new_adresse2, new_adresse3, new_cp, new_ville, new_coords, new_siret, new_contact_principal, client_id))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Client modifié avec succès!"}

def supprimer_client(client_id):
    cnx, cursor = create_connection()
    cursor.execute("DELETE FROM clients WHERE client_id = %s", (client_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Client supprimé avec succès!"}

def visualiser_client(client_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM clients WHERE client_id = %s", (client_id,))
    details = cursor.fetchone()
    cursor.close()
    cnx.close()

    if not details:
        return {"message": "Client non trouvé!"}

    return details
