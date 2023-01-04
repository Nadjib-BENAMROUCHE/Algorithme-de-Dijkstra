import heapq 
import numpy as np

import math
from io import StringIO
import time 


# fonction importé pour afficher le tas binaire (facultatif)
#-------------------------------------------------------------------------------------------------
def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return 






# algorithme de Dijkstra, prcour d
#----------------------------------------------------------------------------------------------------
def parcour(dic,u,graphe):  

	# vérifier que le tas n'est pas vide 
	if ( u not in dic.keys()):  
				# fin du programme
				return("done")
	else : 

		# récupérer les valeur du dictionnaire (poids de chaque noeud)
		tas= list(dic.values())  


		# vérifier que le tas n'est pas vide 
		if (tas !=[]): 


			# parcourir les voisins du noeud u 
			for i in range(len(graphe[u])):  

				# récupérer les voisins du noeud u 
				indice =graphe[u][i][0] 

				# vérifier si le noeud n'a pas encore été traité 
				if (indice in dic.keys()): 

					# mise à jour des poids des noeuds voisins de u en fonction du poids de u et  le coût  (u,voisins)
					dic[indice][0]= graphe[u][i][1] + dic[u][0] 

			# supprimer le noeud déjà traité du dictionnaire 
			dic.pop(u) 
			# état du dictionnaire de poids
			print("état du dictionnaire de poids.....\n",dic)
			
			# transformer le dictionnaire en tas binaire afin d'extraire la racine c'est à dire 
			# le noeud de poids minimum
			tas= list(dic.values()) 
			heapq.heapify(tas)  

			# afficher le tas binaire courant 
			print("état de l'arbre min heap")
			show_tree(tas) 

			#  vérifier si le tas n'est pas vide afin de ne pas lever une erreur en essayant de supprimer un noeud dans une liste vide
			if (tas != []): 

				# supprimer le noeud traité du tas 
				val=heapq.heappop(tas) 

				# récupérer le numéro du prochain noeud à traiter 
				u = val[1]
				
				# nouvel appel "récursif" de parcour de graphe 
				parcour(dic,u,graphe)  
							
				return dic 
								

# programme principal 
#----------------------------------------------------------------------------------------------------------------------------------

# définir un graphe grace au dictionnaire python  "{clé : valeur} "
graphe = { 1: [(6,5)],    
		   2: [(4,10),(5,3),(6,11),(1,3)], 
		   3: [(2,1),(4,7)], 
		   4: [],
		   5: [(4,4)],
		   6: [(1,1)], 
		   7: [(1,5),(5,4)]
		}


# dictionnaire pour représenter les poids de chaque noeuds 
dic  = {1 : [1000,1] ,
		2 : [1000,2] ,
		3 :[0,3] , 
		4: [1000,4], 
		5:[1000,5], 
		6:[1000,6], 
		7:[1000,7]
		} 



# appel de la fonction parcour() à partir du noeud racine : 3 
# dic représente le tas binaire 
start_time = time.time()
parcour(dic,3,graphe)
print(time.time()-start_time)
#print(dic)
