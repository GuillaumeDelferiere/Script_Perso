"""
Script principal pour gérer les arguments de la ligne de commande
Avec DuckDB
"""
import os
from utils.data_operations import (
    consolidate_files, search_data, generate_rapport_categorie, generate_rapport
)

# Dossier pour les fichiers CSV
DATA_DIRECTORY = "data"

def afficher_menu():
    """
    Afficher le menu principal
    :return:
    """
    print("""
    Menu Gestion Inventaire
    1. Consolider les fichiers CSV
    2. Rechercher un produit
    3. Générer un rapport
    4. Générer un rapport par catégorie
    5. Quitter
    """)


# Fonction principale avec argparse
def main():
    """
    Fonction principale pour gérer les arguments de la ligne de commande
    """
    while True :
        afficher_menu()
        choix = input("Entrez votre choix: ")

        if choix == "1":
            df = consolidate_files(DATA_DIRECTORY)
            print("Fichiers consolidés avec succès !")
            print(df)

        elif choix == "2":
            query = input("Entrez votre recherche: ")
            results = search_data(query, DATA_DIRECTORY)
            print(results)

        elif choix == "3":
            output_file = input("Entrez le nom du fichier de sortie: ")
            output_path = os.path.join(DATA_DIRECTORY, output_file)
            generate_rapport(DATA_DIRECTORY, output_path)
            print(f"Rapport généré avec succès: {output_path}")

        elif choix == "4":
            output_file = input("Entrez le nom du fichier de sortie: ")
            output_path = os.path.join(DATA_DIRECTORY, output_file)
            generate_rapport_categorie(DATA_DIRECTORY, output_path)
            print(f"Rapport généré avec succès: {output_path}")

        elif choix == "5":
            print("Merci d'avoir utilisé le programme !")
            break

if __name__ == "__main__":
    main()
