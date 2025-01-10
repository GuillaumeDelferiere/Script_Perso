"""
Script principal pour gérer les arguments de la ligne de commande
Avec DuckDB
"""
import os
import argparse
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


def gestion_interactive():
    """
    Mode interactif avec menu.
    """
    while True:
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


def main():
    """
    Fonction principale pour gérer les arguments de la ligne de commande
    """
    parser = argparse.ArgumentParser(description="Gestion de l'inventaire avec DuckDB")
    parser.add_argument(
        "--mode", choices=["interactive", "consolidate", "search", "report", "report-category"],
        help="Mode d'exécution : 'interactive', 'consolidate', 'search', 'report', 'report-category'."
    )
    parser.add_argument("--query", type=str, help="Recherche d'un produit ou catégorie (utilisé avec --mode search).")
    parser.add_argument("--output", type=str, help="Nom du fichier de sortie (utilisé avec --mode report/report-category).")
    args = parser.parse_args()

    if args.mode == "interactive":
        gestion_interactive()

    elif args.mode == "consolidate":
        df = consolidate_files(DATA_DIRECTORY)
        print("Fichiers consolidés avec succès !")
        print(df)

    elif args.mode == "search":
        if not args.query:
            print("Erreur : Vous devez fournir une recherche avec --query.")
        else:
            results = search_data(args.query, DATA_DIRECTORY)
            print(results)

    elif args.mode == "report":
        if not args.output:
            print("Erreur : Vous devez fournir un fichier de sortie avec --output.")
        else:
            output_path = os.path.join(DATA_DIRECTORY, args.output)
            generate_rapport(DATA_DIRECTORY, output_path)
            print(f"Rapport généré avec succès : {output_path}")

    elif args.mode == "report-category":
        if not args.output:
            print("Erreur : Vous devez fournir un fichier de sortie avec --output.")
        else:
            output_path = os.path.join(DATA_DIRECTORY, args.output)
            generate_rapport_categorie(DATA_DIRECTORY, output_path)
            print(f"Rapport généré avec succès : {output_path}")

    else:
        print("Aucun mode valide sélectionné. Utilisez --help pour voir les options disponibles.")


if __name__ == "__main__":
    main()

