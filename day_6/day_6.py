import re
import random

file = open('day_6.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n\n')
for index in range(len(contenu)):
    contenu[index]= re.split('\n| ', contenu[index])
print(contenu)


#puzzle 1
compte_rep = 0
for reponse in  contenu:
    Liste_lettre = []
    for element in reponse:
        for lettre in element:
            if lettre not in Liste_lettre:
                Liste_lettre.append(lettre)
    compte_rep = compte_rep + len(Liste_lettre)

print(compte_rep)

#puzzle 2

compte_rep = 0
for reponse in  contenu:
    Liste_lettre = []
    for element in reponse:
        for lettre in element:
            if lettre not in Liste_lettre:
                Liste_lettre.append(lettre)
    Liste_lettre_non_commune = []
    for lettre in Liste_lettre:
        for element in reponse:
            if lettre not in element and lettre not in Liste_lettre_non_commune:
                Liste_lettre_non_commune.append(lettre)
    
    for lettre in Liste_lettre_non_commune:
        del Liste_lettre[Liste_lettre.index(lettre)]

    compte_rep = compte_rep + len(Liste_lettre)
print(compte_rep)