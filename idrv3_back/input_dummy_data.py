# input_dummy_data.py

import mysql.connector

SQL_SCRIPT = """

-- Populating salutations
INSERT INTO salutations (salutation) VALUES ('M.');
INSERT INTO salutations (salutation) VALUES ('Mme.');
INSERT INTO salutations (salutation) VALUES ('Ms.');
INSERT INTO salutations (salutation) VALUES ('Dr.');
INSERT INTO salutations (salutation) VALUES ('Lord.');
INSERT INTO salutations (salutation) VALUES ('Prof.');

-- Populating clients (assuming you've populated client_contacts)
INSERT INTO clients (client_nom, client_adresse1, client_cp, client_ville, client_siret) VALUES ('Example Corp. 1', '123 Example St.', 12345, 'Example City', 12345678901234);
INSERT INTO clients (client_nom, client_adresse1, client_cp, client_ville, client_siret) VALUES ('Example Corp. 2', '456 Another Rd.', 23456, 'Another Town', 23456789012345);
INSERT INTO clients (client_nom, client_adresse1, client_cp, client_ville, client_siret) VALUES ('Example Corp. 3', '789 Third Ave.', 34567, 'Third City', 34567890123456);
INSERT INTO clients (client_nom, client_adresse1, client_cp, client_ville, client_siret) VALUES ('Example Corp. 4', '012 Fourth Blvd.', 45678, 'Fourth Village', 45678901234567);
INSERT INTO clients (client_nom, client_adresse1, client_cp, client_ville, client_siret) VALUES ('Example Corp. 5', '345 Fifth Ln.', 56789, 'Fifth Hamlet', 56789012345678);

-- Populating client_contacts 

INSERT INTO client_contacts (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, client_contact_cp, client_contact_ville, client_contact_email, client_id) VALUES (1, 'Frank', 'Sauze', '123 Example St.', 12345, 'Example City', 'sauze@client1.com', 1);
INSERT INTO client_contacts (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, client_contact_cp, client_contact_ville, client_contact_email, client_id) VALUES (2, 'Philippe', 'Vilmot', '456 Another Rd.', 23456, 'Another Town', 'leroidefrance@client2.com', 2);
INSERT INTO client_contacts (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, client_contact_cp, client_contact_ville, client_contact_email, client_id) VALUES (3, 'Herve', 'Renard', '789 Third Ave.', 34567, 'Third City', 'managerdefoot@client3.com', 3);
INSERT INTO client_contacts (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, client_contact_cp, client_contact_ville, client_contact_email, client_id) VALUES (4, 'Harry', 'Kane', '012 Fourth Blvd.', 45678, 'Fourth Village', 'no_good_any_more@client4.com', 4);
INSERT INTO client_contacts (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, client_contact_cp, client_contact_ville, client_contact_email, client_id) VALUES (5, 'Def', 'Leotard', '345 Fifth Ln.', 56789, 'Fifth Hamlet', 'musicienloupe@client4.com', 4);
INSERT INTO client_contacts (client_contact_salutation_id, client_contact_prenom, client_contact_nom, client_contact_adresse1, client_contact_cp, client_contact_ville, client_contact_email, client_id) VALUES (5, 'Jef', 'Leopard', '3 Rue de La Croix Brulante', 56789, 'Petit Hameau', 'jef.leopard@client5.com', 5);

-- Populating restaurants


INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_cp, restaurant_ville, client_id) VALUES ('Café One', '123 Main St.', 12345, 'Example City', 1);
INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_cp, restaurant_ville, client_id) VALUES ('Bistro Two', '456 Center Rd.', 23456, 'Another Town', 2);
INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_cp, restaurant_ville, client_id) VALUES ('Diner Three', '789 Side Ave.', 34567, 'Third City', 3);
INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_cp, restaurant_ville, client_id) VALUES ('Eatery Four', '012 Back Blvd.', 45678, 'Fourth Village',3);
INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_cp, restaurant_ville, client_id) VALUES ('Restaurant Five', '345 Cross Ln.', 56789, 'Fifth Hamlet',4);
INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_cp, restaurant_ville, client_id) VALUES ('Restau TechHouse', '345 Rue Sainte Croix', 66666, 'Sixth Chameau',5);
INSERT INTO restaurants (restaurant_nom, restaurant_adresse1, restaurant_cp, restaurant_ville, client_id) VALUES ('Restaurant Tout Jeune Tout neuf', '345 Cross Lucas.', 11111, 'Seventh Chalumeau',4);

-- Populating auditeurs

INSERT INTO auditeurs (auditeur_salutation_id, auditeur_prenom, auditeur_nom, auditeur_tel, auditeur_email) VALUES (1, 'Tom', 'Taylor', '+1123456789', 'tom.taylor@idr.com');
INSERT INTO auditeurs (auditeur_salutation_id, auditeur_prenom, auditeur_nom, auditeur_tel, auditeur_email) VALUES (2, 'Sarah', 'Sanders', '+2234567890', 'sarah.sanders@idr.com');
INSERT INTO auditeurs (auditeur_salutation_id, auditeur_prenom, auditeur_nom, auditeur_tel, auditeur_email) VALUES (3, 'Ulysses', 'Upton', '+3345678901', 'ulysses.upton@idr.com');
INSERT INTO auditeurs (auditeur_salutation_id, auditeur_prenom, auditeur_nom, auditeur_tel, auditeur_email) VALUES (4, 'Vera', 'Vance', '+4456789012', 'vera.vance@idr.com');
INSERT INTO auditeurs (auditeur_salutation_id, auditeur_prenom, auditeur_nom, auditeur_tel, auditeur_email) VALUES (5, 'Walter', 'White', '+5567890123', 'walter.white@idr.com');

-- Populating gestionnaires
INSERT INTO gestionnaires (gestionnaire_nom, gestionnaire_coords) VALUES ('Sodexo', 'Coord A');
INSERT INTO gestionnaires (gestionnaire_nom, gestionnaire_coords) VALUES ('Gestionnaire B', 'Coord B');
INSERT INTO gestionnaires (gestionnaire_nom, gestionnaire_coords) VALUES ('Gestionnaire C', 'Coord C');
INSERT INTO gestionnaires (gestionnaire_nom, gestionnaire_coords) VALUES ('Gestionnaire D', 'Coord D');
INSERT INTO gestionnaires (gestionnaire_nom, gestionnaire_coords) VALUES ('Gestionnaire E', 'Coord E');

-- Populating audits
-- Assuming audit by first auditor for the first client's first restaurant managed by the first gestionnaire
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (1, 1, 1, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '10:00:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (1, 2, 1, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '11:00:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (3, 1, 3, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '10:30:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (4, 2, 4, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '12:00:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (3, 5, 5, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '12:30:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (3, 5, 2, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '10:00:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (3, 5, 4, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '12:00:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (3, 3, 1, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '11:00:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (3, 3, 5, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '12:00:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (3, 3, 5, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '12:00:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
 VALUES (5, 5, 5, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '12:30:00');
INSERT INTO audits (client_id, gestionnaire_id, auditeur_ID, chapitre, restaurant_id, date_audit, client_contact_id, nombre_de_couverts, horaires_du_self_debut, horaires_du_self_fin) 
VALUES (1, 1, 1, 1, 1, '2023-09-05 10:00:00', 1, 100, '08:00:00', '12:30:00');


-- Populating notes_structures
-- For simplicity, let's assume these are general categories for auditing
INSERT INTO notes_structures (notes_structure_nom, est_actif) VALUES ('Zero à cinq', TRUE);
INSERT INTO notes_structures (notes_structure_nom, est_actif) VALUES ('NPS', TRUE);
INSERT INTO notes_structures (notes_structure_nom, est_actif) VALUES ('Tripartite', TRUE);
INSERT INTO notes_structures (notes_structure_nom, est_actif) VALUES ('Binaire', TRUE);
INSERT INTO notes_structures (notes_structure_nom, est_actif) VALUES ('Oui ou non', TRUE);

-- Populating reponses_possibles
-- For simplicity, let's assume these are possible scores
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('5', 1);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('4', 1);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('3', 1);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('2', 1);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('1', 1);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('1', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('0', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('1', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('2', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('3', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('4', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('5', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('6', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('7', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('8', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('9', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('10', 2);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('Conforme', 3);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('Partiellement conforme', 3);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('Non conforme', 3);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('CONFORME', 4);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('NON CONFORME', 4);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('Oui', 5);
INSERT INTO reponses_possibles (response_value, notes_structure_id) VALUES ('Non', 5);


-- Populating elements
-- Assume these elements are items to be audited
INSERT INTO elements (chapitre, titre, sous_titre, element_nom, notes_structure_id) VALUES ('Chap 1', 'Title 1', 'Subtitle 1','element10', 4);
INSERT INTO elements (chapitre, titre, sous_titre, element_nom, notes_structure_id) VALUES ('Chap 2', 'Title 2', 'Subtitle 2','element11', 4);
INSERT INTO elements (chapitre, titre, sous_titre, element_nom, notes_structure_id) VALUES ('Chap 3', 'Title 3', 'Subtitle 3','element12', 5);
INSERT INTO elements (chapitre, titre, sous_titre, element_nom, notes_structure_id) VALUES ('Chap 4', 'Title 4', 'Subtitle 4','element13', 5);
INSERT INTO elements (chapitre, titre, sous_titre, element_nom, notes_structure_id) VALUES ('Chap 5', 'Title 5', 'Subtitle 5','element14', 5);

-- Populating legendes
-- Legend entries for the audit elements
INSERT INTO legendes (legende_name, chapitre, legende_elements) VALUES ('Legend 1', 1, 'Vert|Orange|Rouge');
INSERT INTO legendes (legende_name, chapitre, legende_elements) VALUES ('Legend 2', 2, '1|2');
INSERT INTO legendes (legende_name, chapitre, legende_elements) VALUES ('Legend 3', 3, 'Element E|Element F');
INSERT INTO legendes (legende_name, chapitre, legende_elements) VALUES ('Legend 4', 4, 'Element G|Element H');
INSERT INTO legendes (legende_name, chapitre, legende_elements) VALUES ('Legend 5', 5, 'Element I|Element J');


-- Populating elements_audites_details_prestations
-- Detailed items for auditing
INSERT INTO elements_audites_details_prestations (elements_audites_details_prestation_nom, elements_audites_details_prestation_grammage, elements_audites_details_prestation_temperature, elements_audites_details_prestation_sous_titre) VALUES ('Detail A', '50g', 'Hot', 1);
INSERT INTO elements_audites_details_prestations (elements_audites_details_prestation_nom, elements_audites_details_prestation_grammage, elements_audites_details_prestation_temperature, elements_audites_details_prestation_sous_titre) VALUES ('Detail B', '100g', 'Cold', 2);
INSERT INTO elements_audites_details_prestations (elements_audites_details_prestation_nom, elements_audites_details_prestation_grammage, elements_audites_details_prestation_temperature, elements_audites_details_prestation_sous_titre) VALUES ('Detail C', '150g', 'Warm', 3);
INSERT INTO elements_audites_details_prestations (elements_audites_details_prestation_nom, elements_audites_details_prestation_grammage, elements_audites_details_prestation_temperature, elements_audites_details_prestation_sous_titre) VALUES ('Detail D', '200g', 'Hot', 4);
INSERT INTO elements_audites_details_prestations (elements_audites_details_prestation_nom, elements_audites_details_prestation_grammage, elements_audites_details_prestation_temperature, elements_audites_details_prestation_sous_titre) VALUES ('Detail E', '250g', 'Cold', 5);
        """

def input_dummy_data():
    config = {
        'user': 'root',
        'password': 'password',
        'host': '127.0.0.1',
        'database': 'audit_responses_db',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        for result in cursor.execute(SQL_SCRIPT, multi=True):
            pass  # Iterate over results to ensure all statements are executed
        cnx.commit()
        print("Dummy data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    input_dummy_data()