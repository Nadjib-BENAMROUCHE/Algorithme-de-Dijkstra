import numpy as np



#complexite O(n)=N²

graphe = [[0, 4, 1, 0, 3, 0],
          [4, 0, 10, 1, 0, 0],
          [1, 10, 0, 5, 1, 0],
          [0, 1, 5, 0, 3, 1],
          [3, 0, 1, 3, 0, 1],
          [0, 0, 0, 1, 1, 0]]


def matricedijkstra(mg,s):
    #arguments : - mg matrice d'adjacencee du graphe pondéré
    #            - s le somment de depart
    #sortie : s_connu - dictionnaire { sommet : [logueur, plus court chemin] }

    #------------Initialisation ----------------------

    infini = 10000
    nb_sommets = len(mg)
    
    s_connu = { s : [0, [s]]}
    s_inconnu = {k : [infini, ''] for k in range (nb_sommets) if k != s }
    print("La liste des elements connus :" ,s_connu)
    print("La liste des inconnus " ,s_inconnu)
    for suivant in range(nb_sommets):
        if mg[s][suivant]:
            s_inconnu[suivant] = [mg[s][suivant], s]


    print("Dans le graphe d\'origine {} de matrice d\'adjacence : ".format(s))
    for ligne in mg:
        print(ligne)
    print()
    print("Plus court chemins de ")

#------------- La recherche -------------------------

    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):
        u = min(s_inconnu, key = s_inconnu.get)
        longueur_u, precedent_u = s_inconnu[u]
        for v in range(nb_sommets):
            if mg[u][v] and v in s_inconnu:
                d = longueur_u + mg[u][v]
                if d < s_inconnu[v][0]:
                    s_inconnu[v] = [d, u]
        s_connu[u] = [ longueur_u, s_connu[precedent_u][1] + [u] ]
        del s_inconnu[u]
        print("Longueur ", longueur_u, ":", " -<< ".join(map(str, s_connu[u][1])))

    for k in s_inconnu:
        print("Il n\'y a aucun chemin de {} à {} ".format( s, k ))
    

    return s_connu

matricedijkstra(graphe, 1)