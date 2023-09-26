# creer_db_tables.py

import mysql.connector
from db_utils import create_connection


def creer_db_tables():
    # Connect to the audit_responses_db
    cnx, cursor = create_connection()

    try:
        # Here, you'll have all the SQL commands to create your tables.
         # Create the 'salutations' table
        cursor.execute("""
            CREATE TABLE salutations (
                salutation_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                salutation TEXT
            );
        """)

        # Create the 'clients' table
        cursor.execute("""
            CREATE TABLE clients (
                client_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
                client_nom TEXT,
                client_logo BLOB,
                client_adresse1 VARCHAR(255),
                client_adresse2 VARCHAR(255),
                client_adresse3 VARCHAR(255),
                client_cp INT CHECK (LENGTH(client_cp) = 5),
                client_ville VARCHAR(100),
                client_coords TEXT,
                client_siret VARCHAR(255),
                client_contact_principal INTEGER
            );
        """)

        # Create the 'client_contacts' table
        cursor.execute("""
            CREATE TABLE client_contacts (
                client_contact_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
                client_contact_salutation_id INT REFERENCES salutations(salutation_id),
                client_contact_prenom TEXT,
                client_contact_nom TEXT,
                client_contact_adresse1 VARCHAR(255),
                client_contact_adresse2 VARCHAR(255),
                client_contact_adresse3 VARCHAR(255),
                client_contact_cp INT CHECK (LENGTH(client_contact_cp) = 5),
                client_contact_ville VARCHAR(100),
                client_contact_coords TEXT,
                client_contact_email TEXT,
                client_contact_tel TEXT,
                client_contact_role TEXT,
                client_id INTEGER REFERENCES clients(client_id)
            );
        """)

        # create table
        cursor.execute("""
            CREATE TABLE gestionnaires (
    gestionnaire_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    gestionnaire_nom VARCHAR(100),
    gestionnaire_coords TEXT
);

        """)
        
        # create table
        cursor.execute("""
            CREATE TABLE auditeurs (
    auditeur_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    auditeur_salutation_id INT REFERENCES salutations(salutation_id),
    auditeur_prenom VARCHAR(100),
    auditeur_nom VARCHAR(100),
    auditeur_tel VARCHAR(15),
    auditeur_email VARCHAR(255),
    auditeur_login_id TEXT,
    auditeur_permissions TEXT
);
        """)
        
        # create table
        cursor.execute("""
            CREATE TABLE notes_structures (
    notes_structure_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    notes_structure_nom TEXT,
    element_audite INT,  -- This will be filled later
    est_actif BOOLEAN
);
        """)
        
        # create table
        cursor.execute("""
            CREATE TABLE reponses_possibles (
    response_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    response_value TEXT,
    notes_structure_id INT REFERENCES notes_structures(notes_structure_id)
);
        """)
        
        # create table
        cursor.execute("""
            CREATE TABLE elements (
    element_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    chapitre TEXT,
    titre TEXT,
    sous_titre VARCHAR(255),
    element_nom VARCHAR(255),
    notes_structure_id INT REFERENCES notes_structures(notes_structure_id)
);
        """)
        
        # create table
        cursor.execute("""
            CREATE TABLE restaurants (
    restaurant_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    restaurant_nom VARCHAR(100),
    restaurant_adresse1 VARCHAR(255),
    restaurant_adresse2 VARCHAR(255),
    restaurant_adresse3 VARCHAR(255),
    restaurant_cp INT CHECK (LENGTH(restaurant_cp) = 5),
    restaurant_ville VARCHAR(100),
    restaurant_coords TEXT,
    client_id INT REFERENCES clients(client_id)
);
        """)
        
        # create table
        cursor.execute("""
            CREATE TABLE audits (
    audit_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    client_id INT REFERENCES clients(client_id),
    gestionnaire_id INT REFERENCES gestionnaires(gestionnaire_id),
    auditeur_id INT REFERENCES auditeurs(auditeur_id),
    chapitre INT REFERENCES elements(element_id),
    restaurant_id INT REFERENCES restaurants(restaurant_id),
    date_audit DATETIME,
    client_contact_id INT REFERENCES client_contacts(client_contact_id),
    nombre_de_couverts INT,
    horaires_du_self_debut TIME,
    horaires_du_self_fin TIME
);
        """)
        
        # create table
        cursor.execute("""
            CREATE TABLE legendes (
    legende_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    legende_name TEXT,
    chapitre INT REFERENCES elements(element_id),
    legende_elements TEXT
);
        """)

        # create table
        cursor.execute("""
            CREATE TABLE elements_audites_details_prestations (
    elements_audites_details_prestation_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    elements_audites_details_prestation_nom TEXT,
    elements_audites_details_prestation_grammage TEXT,
    elements_audites_details_prestation_temperature TEXT,
    elements_audites_details_prestation_sous_titre INT REFERENCES elements(element_id)
);
        """)
        # create table
        cursor.execute("""
            CREATE TABLE constats (
    constat_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    constat INT,  -- This will be filled later
    elements_audites_details_prestation_id  INT REFERENCES elements_audites_details_prestations(elements_audites_details_prestation_id),
    element_id  INT REFERENCES elements(element_id),
    heure_du_constat DATETIME,
    score INT REFERENCES reponses_possibles(response_id),
    observations TEXT,
    audit_id INT REFERENCES audits(audit_id),
    auditeur_id INT REFERENCES auditeurs(auditeur_id)
);
        """)
        

        # Add the foreign key constraint to clients for client_contact_principal
        cursor.execute("""
            CREATE TABLE attachments (
    attachment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    constat_id INT REFERENCES constats(constat_id),
    file BLOB
);
                       """)
        
        cursor.execute("""
            ALTER TABLE clients
            ADD FOREIGN KEY (client_contact_principal) REFERENCES client_contacts(client_contact_id);
        """)
        # ... other table creations
        print("creation de tables OK.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()
