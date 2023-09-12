#FICHIER POUR METTRE À JOUR DES QUESTIONS DANS LES AUDITS

import pandas as pd
from db_utils import create_connection
from mettre_a_jour_questions import mettre_a_jour_questions


DATA_QUESTIONS_CSV = 'data_questions.csv'

def modifier_element():
    element_id = input("Entrez l'ID de l'élément à modifier: ")

    df = pd.read_csv(DATA_QUESTIONS_CSV, delimiter=';')

    if int(element_id) > len(df):
        print("ID de l'élément non trouvé!")
        return

    current_values = df.iloc[int(element_id)-1]
    print("Laissez le champ vide pour conserver la valeur actuelle.")
    chapitre = input(f"Chapitre (actuel: {current_values['chapitre']}): ") or current_values['chapitre']
    titre = input(f"Titre (actuel: {current_values['titre']}): ") or current_values['titre']
    sous_titre = input(f"Sous-titre (actuel: {current_values['sous_titre']}): ") or current_values['sous_titre']
    element_nom = input(f"Nom de l'élément (actuel: {current_values['element_nom']}): ") or current_values['element_nom']

    df.at[int(element_id)-1, 'chapitre'] = chapitre
    df.at[int(element_id)-1, 'titre'] = titre
    df.at[int(element_id)-1, 'sous_titre'] = sous_titre
    df.at[int(element_id)-1, 'element_nom'] = element_nom

    df.to_csv(DATA_QUESTIONS_CSV, sep=';', index=False)
    mettre_a_jour_questions(df)

def supprimer_element():
    element_id = input("Entrez l'ID de l'élément à supprimer: ")

    df = pd.read_csv(DATA_QUESTIONS_CSV, delimiter=';')

    if int(element_id) > len(df):
        print("ID de l'élément non trouvé!")
        return

    df.drop(int(element_id)-1, inplace=True)
    df.to_csv(DATA_QUESTIONS_CSV, sep=';', index=False)
    mettre_a_jour_questions(df)

import pandas as pd
from db_utils import create_connection
from mettre_a_jour_questions import mettre_a_jour_questions

DATA_QUESTIONS_CSV = 'data_questions.csv'

def ajouter_element():
    chapitre = input("Entrez le chapitre: ")
    titre = input("Entrez le titre: ")
    sous_titre = input("Entrez le sous-titre: ")
    element_nom = input("Entrez le nom de l'élément: ")

    new_element = pd.DataFrame({
        'chapitre': [chapitre],
        'titre': [titre],
        'sous_titre': [sous_titre],
        'element_nom': [element_nom]
    })

    df = pd.read_csv(DATA_QUESTIONS_CSV, delimiter=';')
    df = pd.concat([df, new_element], ignore_index=True)
    df.to_csv(DATA_QUESTIONS_CSV, sep=';', index=False)

    mettre_a_jour_questions(df)



def voir_element():
    element_id = input("Entrez l'ID de l'élément à voir: ")

    df = pd.read_csv(DATA_QUESTIONS_CSV, delimiter=';')

    if int(element_id) > len(df) or int(element_id) <= 0:
        print("ID de l'élément non trouvé!")
        return

    element_details = df.iloc[int(element_id)-1]
    print("\nDétails de l'élément:")
    for col, value in element_details.items():
        print(f"{col}: {value}")


def afficher_elements():
    df = pd.read_csv(DATA_QUESTIONS_CSV, delimiter=';')
    print(df)


def menu():
    print("\nGestion des éléments:")
    print("1. Ajouter un élément")
    print("2. Afficher les éléments")
    print("3. Modifier un élément")
    print("4. Supprimer un élément")
    print("5. Voir un élément")
    print("6. Quitter")
    choix = input("\nEntrez votre choix: ")
    return choix

if __name__ == "__main__":
    while True:
        user_choice = menu()
        if user_choice == '1':
            ajouter_element()
        elif user_choice == '2':
            afficher_elements()
        elif user_choice == '3':
            modifier_element()
        elif user_choice == '5':
            voir_element()
        elif user_choice == '4':
            supprimer_element()
        elif user_choice == '6':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")



# Main execution
if __name__ == "__main__":
    # Load the CSV data
    data_questions = pd.read_csv(DATA_QUESTIONS_CSV, delimiter=';')
    # Call the function to insert data
    mettre_a_jour_questions(data_questions)
    print("Data from CSV inserted successfully!")
