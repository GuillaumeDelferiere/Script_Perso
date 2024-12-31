import argparse
import os
from utils.data_operations import consolidate_files, search_data, generate_rapport

# Dossier pour les fichiers CSV
data_directory = "data"

# Fonction principale avec argparse
def main():
    parser = argparse.ArgumentParser(description="Gestion de stock avec DuckDB")
    parser.add_argument("--consolidate", action = "store_true", help="Consolider les fichiers CSV en une base unique")
    parser.add_argument("--search", type=str, help="Rechercher un produit dans la base")
    parser.add_argument("--report", action = "store_true", help="Générer un rapport sur les produits")
    args = parser.parse_args()

    if args.consolidate:
        data = consolidate_files(data_directory)
        print(data)
    elif args.search:
        results = search_data(args.search, data_directory)
        print(results)
    elif args.report:
        report_file = os.path.join(data_directory, "rapport.csv")
        generate_rapport(data_directory, report_file)
    else:
        print("Aucune option sélectionnée. Utilisez --help pour voir les options disponibles.")

if __name__ == "__main__":
    main()