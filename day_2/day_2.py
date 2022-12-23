import re
file = open('day_2.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n')
for index in range(len(contenu)):
    contenu[index]= re.split(' |: |-',contenu[index])

#puzzle1
nombre_valid = 0
for ligne in contenu:
    compte = 0
    for lettre in ligne[3]:
        if lettre == ligne[2]:
            compte = compte + 1
    if compte <= int(ligne[1]):
        if compte >= int(ligne[0]):
            nombre_valid = nombre_valid + 1

print(nombre_valid)

#puzzle2
nombre_valid = 0
for ligne in contenu:
    compte = 0
    if ligne[3][int(ligne[0])-1] == ligne[2]:
        compte = compte + 1
    if ligne[3][int(ligne[1])-1] == ligne[2]:
        compte = compte + 1
    if compte == 1:
        nombre_valid = nombre_valid + 1

print(nombre_valid)

