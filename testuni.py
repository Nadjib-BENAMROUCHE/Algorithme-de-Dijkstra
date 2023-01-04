import dijkstra_tas as mp
import heap_done as mf
import unittest

m = 6

di  = {1 : [1000,1] ,															#Le dictionnaire d'inialisation de poids
		2 : [1000,2] ,
		3 :[0,3] , 
		4: [1000,4], 
		5:[1000,5], 
		6:[1000,6], 
		7:[1000,7]
		} 
graphe = { 1: [(6,5)],    														# Notre graphe pour le test.
		   2: [(4,10),(5,3),(6,11),(1,3)], 
		   3: [(2,1),(4,7)], 
		   4: [],
		   5: [(4,4)],
		   6: [(1,1)], 
		   7: [(5,4),(1,5)]
		}


class TestMonProjet(unittest.TestCase):


    def testresultat(self):
        a =  ([1, 2], [4, 1], [4, 5], [7, 4], [9, 6], [1000, 7])             #Le resultat obtenue par le parcour manuel de l'algorithme dijkstra pour notre graphe 
        b,c = mp.parcour(di,3,graphe,mp.resultat)				#Le parcour avec la fonction de notre programme avec le méme graphe
        for i  in range(m):
            self.assertEqual(a[i],c[i])											 #La comparaison de resultats (sommets,poids) 


	
    	
		
if __name__ == "__main__":
    unittest.main()
