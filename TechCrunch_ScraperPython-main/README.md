# TechCrunch Apps Section Web Scraping

# Description
Ce projet est un script Python pour le web scraping de la section "Apps" du site TechCrunch. Il vise à extraire les mots les plus fréquents dans les titres des articles des 5 premières pages de cette catégorie et à les visualiser sous forme de diagramme en barres.

# Fonctionnalités
- Récupération du contenu HTML des 5 premières pages de la section "Apps" de TechCrunch.
- Extraction et comptage des mots dans les titres des articles.
- Nettoyage des données en éliminant les mots de trois lettres ou moins.
- Visualisation des 50 mots les plus fréquents sous forme de diagramme en barres.

# Technologies Utilisées
- Python 3
- Bibliothèques Python : BeautifulSoup, Requests, Collections, Matplotlib

# Installation
Assurez-vous d'avoir Python installé sur votre machine. Pour installer les dépendances nécessaires, exécutez :

```bash
pip install beautifulsoup4 requests matplotlib
```

# Utilisation
Pour exécuter le script, lancez :

```bash
python techcrunch_scraping.py
```

# Structure du Projet
- `techcrunch_scraping.py` : Script principal pour le web scraping et la visualisation.

# Contribution
Les contributions, les suggestions d'amélioration, et les rapports de bugs sont bienvenus. Veuillez ouvrir une issue pour discuter de ce que vous aimeriez changer.

# Licence
[MIT](https://choosealicense.com/licenses/mit/)

## Avertissement
Ce script est destiné à des fins éducatives. Veuillez respecter les politiques de TechCrunch en matière de web scraping et les lois en vigueur.

