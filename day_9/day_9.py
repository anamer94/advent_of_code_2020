import re
import random

file = open('day_9.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n')
print(contenu)


#puzzle 1
def comparaison(ligne, contenu):
    liste_nombre = contenu[ligne-25: ligne]
    for nombre_1 in liste_nombre:
        for nombre_2 in liste_nombre:
            if int(nombre_1) + int(nombre_2) == int(contenu[ligne]):
                return 1
    return 0

def calcul_somme_25(contenu):
    ligne = 25
    while ligne < 1000:
        arret = comparaison (ligne, contenu)
        if arret == 0:
            return contenu[ligne]
        ligne = ligne +1

print(calcul_somme_25(contenu))

#756008079

#puzzle 2

def comparaison_2 (contenu, nombre_contigu):
    nombre_a_calculer = 756008079
    for ligne in range(len(contenu)-nombre_contigu+1):
        calcul = 0
        for k in range (nombre_contigu):
            calcul = calcul + int(contenu[ligne+k])
        if calcul == nombre_a_calculer:
            return contenu[ligne: ligne+nombre_contigu]
    return 0

def calcul_somme_contigu(contenu):
    arret = 0
    nombre_contigu = 2
    while nombre_contigu < 1000:
        print(nombre_contigu)
        arret = comparaison_2 (contenu, nombre_contigu)
        if arret != 0:
            arret = [int(i) for i in arret]
            somme = min(arret) + max(arret)
            print(sum(arret))
            return somme
        nombre_contigu = nombre_contigu + 1
    return 0



print(calcul_somme_contigu(contenu))
