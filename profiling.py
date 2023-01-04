import numpy as np 
import matplotlib.pyplot as plt
from time import time 
import djikstra as mp
tmp = [0,0,0,0,0,0,0,0,0]
graphe = [[0, 4, 1, 0, 3, 0],
          [4, 0, 10, 1, 0, 0],
          [1, 10, 0, 5, 1, 0],
          [0, 1, 5, 0, 3, 1],
          [3, 0, 1, 3, 0, 1],
          [0, 0, 0, 1, 1, 0]]
for i in range(5):
    start = time()
    mp.matricedijkstra(graphe,1)
    print("temps d'execution pour l'algorithme trouver sur internet : ", time()-start)
    tmp[i] = time()-start
