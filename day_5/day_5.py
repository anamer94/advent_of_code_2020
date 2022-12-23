import re
import random

file = open('day_5.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n')


#puzzle 1
id = 0
Liste_siege = []
for siege in contenu:
    ligne = [0,127]
    for element in siege[:6]:
        intermediaire = ((ligne[1]-ligne[0])/2)+ligne[0]
        if element == 'F':
            ligne[1] = round(intermediaire)-1
        else:
            ligne[0] = round(intermediaire)
    if siege[6] == 'F':
        ligne = ligne[0]
    else:
        ligne = ligne[1]

    colonne = [0,7]
    for element in siege[7:9]:
        intermediaire = ((colonne[1]-colonne[0])/2)+colonne[0]
        if element == 'L':
            colonne[1] = round(intermediaire)-1
        else:
            colonne[0] = round(intermediaire)
    if siege[9] == 'L':
        colonne = colonne[0]
    else:
        colonne = colonne[1]
    Liste_siege.append(ligne * 8 + colonne)
    id = max(ligne * 8 + colonne, id)

print(id)

#puzzle 2

Liste_siege.sort()

print(Liste_siege)

Liste_siege_compatible=[]
for nombre_siege in range(991):
    if nombre_siege+1 in Liste_siege:
        if nombre_siege-1 in Liste_siege:
            if nombre_siege not in Liste_siege:
                Liste_siege_compatible.append(nombre_siege)
print(Liste_siege_compatible)

