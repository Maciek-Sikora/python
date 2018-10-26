import random
import sys

listaGraczy = ["g1","g2","g3","g4","g5","g6","g7","g9","g10"]
def matchmaker(lista):
    random.shuffle(lista)
    dlugoscListy = len(lista)
    pol = dlugoscListy // 2
    team1 = lista[ : pol]
    team2 = lista[pol : ]
    return team1, team2
print(matchmaker(sys.argv[1:]))