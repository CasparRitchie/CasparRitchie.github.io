import mysql.connector
from db_utils import create_connection

def ajouter_auditeur(data):
    cnx, cursor = create_connection()

    # Extract data
    salutation_id = data.get('salutation_id')
    prenom = data.get('prenom')
    nom = data.get('nom')
    tel = data.get('tel')
    email = data.get('email')
    login_id = data.get('login_id')
    permissions = data.get('permissions')

    if not all([salutation_id, prenom, nom]):
        return {"message": "All fields are required!"}

    try:
        cursor.execute("""
            INSERT INTO auditeurs (auditeur_salutation_id, auditeur_prenom, auditeur_nom, auditeur_tel, auditeur_email, auditeur_login_id, auditeur_permissions)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (salutation_id, prenom, nom, tel, email, login_id, permissions))
        cnx.commit()
        return {"message": f"Auditeur {prenom} {nom} ajouté avec succès."}
    except mysql.connector.Error as err:
        print("MySQL error:", err)
        return {"message": f"Erreur lors de l'ajout de l'auditeur! Error: {err}"}
    finally:
        cursor.close()
        cnx.close()

def afficher_auditeurs():
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("""
        SELECT auditeurs.auditeur_id, salutations.salutation, auditeurs.auditeur_prenom, auditeurs.auditeur_nom,
               auditeurs.auditeur_tel, auditeurs.auditeur_email
        FROM auditeurs
        LEFT JOIN salutations ON auditeurs.auditeur_salutation_id = salutations.salutation_id
    """)
    auditeurs = cursor.fetchall()
    cursor.close()
    cnx.close()
    return auditeurs

def modifier_auditeur(auditeur_id, data):
    cnx, cursor = create_connection()

    # Extract updated data
    salutation_id = data.get('salutation_id')
    prenom = data.get('prenom')
    nom = data.get('nom')
    tel = data.get('tel')
    email = data.get('email')
    login_id = data.get('login_id')
    permissions = data.get('permissions')

    cursor.execute("""
        UPDATE auditeurs 
        SET auditeur_salutation_id = %s, auditeur_prenom = %s, auditeur_nom = %s, auditeur_tel = %s, auditeur_email = %s, auditeur_login_id = %s, auditeur_permissions = %s
        WHERE auditeur_id = %s
    """, (salutation_id, prenom, nom, tel, email, login_id, permissions, auditeur_id))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": f"Auditeur ID {auditeur_id} modifié avec succès."}

def supprimer_auditeur(auditeur_id):
    cnx, cursor = create_connection()
    cursor.execute("""
        DELETE FROM auditeurs 
        WHERE auditeur_id = %s
    """, (auditeur_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {"message": f"Auditeur avec l'ID {auditeur_id} a été supprimé."}

def visualiser_auditeur(auditeur_id):
    cnx, cursor = create_connection(dictionary=True)
    cursor.execute("""
        SELECT auditeurs.*, salutations.salutation 
        FROM auditeurs 
        LEFT JOIN salutations ON auditeurs.auditeur_salutation_id = salutations.salutation_id 
        WHERE auditeur_id = %s
    """, (auditeur_id,))
    details = cursor.fetchone()
    cursor.close()
    cnx.close()
    if not details:
        return {"message": "Auditeur non trouvé!"}
    return details
