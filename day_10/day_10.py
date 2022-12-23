import re
import random

file = open('day_10.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n')
contenu = [int(i) for i in contenu]
contenu.sort()
print(contenu)

List_number_jolt = [0,0,0]
contenu.insert(0,0)
contenu.append(contenu[-1]+3)
for index in range(len(contenu)-1):
    if contenu[index+1]-contenu[index] == 1:
        List_number_jolt[0] = List_number_jolt[0] + 1
    elif contenu[index+1]-contenu[index] == 2:
        List_number_jolt[1] = List_number_jolt[1] + 1
    elif contenu[index+1]-contenu[index] == 3:
        List_number_jolt[2] = List_number_jolt[2] + 1
    else:
        print('!!!')
print(List_number_jolt)
print(List_number_jolt[0]*List_number_jolt[2])


#puzzle 2

def regarder_combien_d_adaptateur_fonctionne_rec(ligne,contenu):
    if ligne == len(contenu)-1:
        return 1
    calcul = 0
    for k in range (3):
        if contenu[ligne+k+1]-contenu[ligne] <= 3:
            calcul = calcul + regarder_combien_d_adaptateur_fonctionne_rec(ligne,contenu)
    return calcul

#que des sauts de 1 ou de 3

print(contenu)

del contenu [-1]
valid_arrangements = [1] * len(contenu)
for index in range(1, len(contenu)):
    valid_arrangements[index] = sum(
        valid_arrangements[src_index]
        for src_index in range(max(0, index - 3), index)
        if contenu[index] - contenu[src_index] <= 3
    )
print(valid_arrangements[-1])