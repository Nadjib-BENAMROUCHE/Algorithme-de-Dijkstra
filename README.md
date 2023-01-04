# Algorithme-de-Dijkstra

# Description
Il s'agit d'une implémentation Python de l'algorithme de Dijkstra, un algorithme de recherche de graphe utilisé pour trouver le plus court chemin entre deux nœuds dans un graphe. L'algorithme fonctionne en relaxant répétitivement les bords d'un graphe et en mettant à jour les distances provisoires des nœuds jusqu'à ce que le plus court chemin soit trouvé.

# Exigences
- Python 3.6 ou supérieur
- NumPy 
- heapq (Ce module expose une implémentation de l'algorithme de file de priorité, basée sur un tas)
- Test unitaire 


# Utilisation
Pour utiliser l'algorithme de Dijkstra, vous pouvez exécuter soit le script dijkstra.py, soit le script dijkstra_heap.py qui utilise des tas pour parcourir le graphe

# Notes
Cette implémentation de l'algorithme de Dijkstra utilise une file de priorité pour prioriser la relaxation des bords de poids plus faibles. Cela entraîne un temps d'exécution de O (E log V) pour les graphes peu denses.
L'algorithme ne fonctionnera que pour les graphes avec des poids de bord non négatifs.
