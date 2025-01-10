"""
Module contenant les fonctions pour consolider les fichiers CSV
en une seule table temporaire avec DuckDB
"""
import duckdb

# Fonction pour consolider les fichiers CSV en une seule table temporaire avec DuckDB
def consolidate_files(directory):
    """
    Consolider les fichiers CSV en une seule table temporaire avec DuckDB
    PRE: les fichiers CSV doivent être dans le dossier spécifié, le dossier doit exister.
    POST: Renvoie un tableau de l'ensemble des données consolidées
    :param directory:
    :return consolidate_data qui est un tableau de l'ensemble des données:
    """
    con = duckdb.connect()
    query = f"""
    SELECT * 
    FROM read_csv_auto('{directory}/*.csv')
    """
    consolidate_data = con.execute(query).df()
    return consolidate_data

# Fonction pour rechercher des informations dans les fichiers consolidés
def search_data(query, directory):
    """
    Rechercher des informations dans les fichiers consolidés
    PRE: les fichiers CSV doivent être dans le dossier spécifié, le dossier doit exister.
    POST: Renvoie un tableau de données correspondant à la recherche
    :param query:
    :param directory:
    :return results qui est un tableau de données correspondant à la recherche:
    """
    con = duckdb.connect()

    # Recherche par quantité
    if query.isdigit():
        sql_query = f"""
        SELECT * 
        FROM read_csv_auto('{directory}/*.csv')
        WHERE Quantite = {query}
        """
    # Recherche par prix unitaire
    elif query.replace(".", "").isdigit():
        sql_query = f"""
        SELECT * 
        FROM read_csv_auto('{directory}/*.csv')
        WHERE Prix_Unitaire = {query}
        """
    # Recherche par catégorie ou par nom de produit
    else:
        sql_query = f"""
        SELECT * 
        FROM read_csv_auto('{directory}/*.csv')
        WHERE Categorie like '%{query}%' OR Nom_Produit like '%{query}%'
        """

    results = con.execute(sql_query).df()
    return results

# Fonction pour générer un rapport récapitulatif
def generate_rapport(directory, output_file):
    """
    Générer un rapport récapitulatif
    PRE: les fichiers CSV doivent être dans le dossier spécifié, le dossier doit exister.
    POST: Renvoie un fichier dans le directory data avec le nom choisi en paramètres contenant le rapport récapitulatif de l'ensemble des données
    :param directory:
    :param output_file:
    :return un fichier contenant le rapport récapitulatif de l'ensemble des données:
    """
    con = duckdb.connect()
    query = f"""
    SELECT *
    FROM read_csv_auto('{directory}/*.csv')
    """
    report = con.execute(query).df()
    report.to_csv(output_file, index=False)
    print(f"Rapport généré avec succès: {output_file}")

# Fonction pour générer un rapport récapitulatif par catégorie
def generate_rapport_categorie(directory, output_file):
    """
    Générer un rapport récapitulatif par catégorie
    PRE: les fichiers CSV doivent être dans le dossier spécifié, le dossier doit exister.
    POST: Renvoie un fichier dans le directory data avec le nom choisi en paramètres contenant le rapport récapitulatif par catégorie
    :param directory:
    :param output_file:
    :return un fichier contenant le rapport récapitulatif par catégorie:
    """
    con = duckdb.connect()
    query = f"""
    SELECT Categorie, SUM(Quantite) AS Quantite_totale, AVG(Prix_Unitaire) AS Prix_moyen
    FROM read_csv_auto('{directory}/*.csv')
    GROUP BY Categorie
    ORDER BY Categorie
    """
    report = con.execute(query).df()
    report.to_csv(output_file, index=False)
    print(f"Rapport par catégorie généré avec succès: {output_file}")
