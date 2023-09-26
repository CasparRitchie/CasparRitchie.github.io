import mysql.connector
from db_utils import create_connection

def ajouter_contact_client(data):
    cnx, cursor = create_connection()

    salutation_id = data.get('client_contact_salutation_id')
    prenom = data.get('client_contact_prenom')
    nom = data.get('client_contact_nom')
    adresse1 = data.get('client_contact_adresse1')
    adresse2 = data.get('client_contact_adresse2')
    adresse3 = data.get('client_contact_adresse3')
    cp = data.get('client_contact_cp')
    ville = data.get('client_contact_ville')
    coords = data.get('client_contact_coords')
    email = data.get('client_contact_email')
    tel = data.get('client_contact_tel')
    role = data.get('client_contact_role')
    client_id = data.get('client_id')

    if not all([salutation_id, prenom, nom, adresse1, cp, ville, coords, email, tel, role, client_id]):
        return {"message": "All contact details are required!"}

    try:
        cursor.execute("""
            INSERT INTO client_contacts 
                (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, 
                client_contact_adresse2, client_contact_adresse3, client_contact_cp, client_contact_ville, 
                client_contact_coords, client_contact_email, client_contact_tel, client_contact_role, client_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (salutation_id, prenom, nom, adresse1, adresse2, adresse3, cp, ville, coords, email, tel, role, client_id))

        cnx.commit()
        cursor.close()
        cnx.close()
        return {"message": "Contact client ajouté avec succès!"}

    except mysql.connector.Error as err:
        return {"message": f"Erreur lors de l'ajout du contact! Error: {err}"}

def afficher_contacts_clients():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM client_contacts")
    contacts = cursor.fetchall()
    cursor.close()
    cnx.close()
    return contacts

def modifier_contact_client(contact_id, data):
    cnx, cursor = create_connection(dictionary=True)

    cursor.execute("SELECT * FROM client_contacts WHERE client_contact_id = %s", (contact_id,))
    details = cursor.fetchone()

    if not details:
        return {"message": "Contact non trouvé!"}

    new_data = {
        'client_contact_salutation_id': data.get('client_contact_salutation_id', details['client_contact_salutation_id']),
        'client_contact_prenom': data.get('client_contact_prenom', details['client_contact_prenom']),
        'client_contact_nom': data.get('client_contact_nom', details['client_contact_nom']),
        'client_contact_adresse1': data.get('client_contact_adresse1', details['client_contact_adresse1']),
        # ... Add other fields in a similar manner ...
    }

    cursor.execute("""
        UPDATE client_contacts
        SET client_contact_salutation_id=%s, client_contact_prenom=%s, client_contact_nom=%s, client_contact_adresse1=%s
        WHERE client_contact_id=%s
    """, (new_data['client_contact_salutation_id'], new_data['client_contact_prenom'], new_data['client_contact_nom'], 
          new_data['client_contact_adresse1'], contact_id))

    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Contact client modifié avec succès!"}

def supprimer_contact_client(contact_id):
    cnx, cursor = create_connection()
    cursor.execute("DELETE FROM client_contacts WHERE client_contact_id = %s", (contact_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": "Contact client supprimé avec succès!"}

def visualiser_contact_client(contact_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("SELECT * FROM client_contacts WHERE client_contact_id = %s", (contact_id,))
    details = cursor.fetchone()
    cursor.close()
    cnx.close()

    if not details:
        return {"message": "Contact non trouvé!"}

    return details
