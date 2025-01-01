# Gestion des stocks avec DuckDB

Ce projet permet de gérer et d'analyser des fichiers CSV contenant des informations sur les stocks d'une entreprise, en utilisant DuckDB.

## Fonctionnalités
- Consolider plusieurs fichiers CSV en une seule base de données temporaire.
- Rechercher des informations par produit, par catégorie ou plage de prix.
- Générer un rapport récapitulatif exportable en CSV.
- Générer un rapport récapitulatif par catégorie exportable en CSV.

## Installation
1. Cloner le dépôt :
    ```bash
    git clone <https://github.com/GuillaumeDelferiere/Script_Perso>
    cd <stock_management>
    ```

2. Créer un environnement virtuel et l'activer :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
    ```

3. Installer les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation
Exécutez le script avec les options souhaitées :

- Pour consolider les fichiers CSV :
    ```bash
    python main.py --consolidate
    ```

- Pour rechercher un produit :
    ```bash
    python main.py --search <nom_du_produit>
    ```

- Pour générer un rapport récapitulatif :
    ```bash
    python main.py --report
    ```

- Pour générer un rapport récapitulatif par catégorie :
    ```bash
    python main.py --report_category
    ```

## Structure du projet
- `main.py` : Script principal pour gérer les arguments de la ligne de commande.
- `utils/data_operations.py` : Contient les fonctions pour consolider les fichiers, rechercher des données et générer des rapports.
- `data/` : Répertoire contenant les fichiers CSV.

## Exemple de fichier CSV
Un exemple de fichier CSV (`data/aliment.csv`) :
```csv
Nom_Produit, Quantite, Prix_Unitaire, Categorie
Pomme, 100, 0.3, Fruits
Pain, 50, 1.2, Boulangerie
Banane, 70, 0.2, Fruits
Fromage, 30, 2.5, Laitier
