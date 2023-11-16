from bs4 import BeautifulSoup
import requests
from collections import Counter
import matplotlib.pyplot as plt

techCrunchData = ''

# Scraping des 5 premières pages de la section Apps de TechCrunch
for num in range(1, 6):
    linkToScrap = f'https://techcrunch.com/category/apps/page/{num}/'
    research = requests.get(linkToScrap)
    techCrunchData += research.text

soup = BeautifulSoup(techCrunchData, 'html.parser')

# Vous devrez identifier la balise et la classe correctes pour les titres des articles
# Cela pourrait nécessiter une modification en fonction de la structure du site
article_titles = soup.find_all('h2', {'class': 'post-block__title'})

words_in_titles = []

for title in article_titles:
    words_in_titles.extend(title.text.strip().split())

# Nettoyage de la liste en supprimant les mots de trois lettres et moins
cleaned_words_list = [word for word in words_in_titles if len(word) > 3]

# Utilisation de Counter pour compter le nombre d'occurrences de chaque mot
word_count = Counter(cleaned_words_list)

# Sélection des 50 mots les plus fréquents
most_common_words = word_count.most_common(50)

# Diviser la liste en mots et occurrences
words, occurrences = zip(*most_common_words)

# Création d'un diagramme en barres
plt.bar(words, occurrences, color='blue')
plt.xlabel('Mots')
plt.ylabel('Occurrences')
plt.title('Fréquence des mots dans les titres des articles sur TechCrunch (Apps)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Affichage du diagramme
plt.show()
