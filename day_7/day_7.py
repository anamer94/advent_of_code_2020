import re
import random


#puzzle 1

file = open('day_7.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n')
for index in range(len(contenu)):
    contenu[index]= re.split(', | contain ', contenu[index])
    contenu[index][-1] = contenu[index][-1][:-1]

for index_contenu in range (len(contenu)):
    for index_rule in range(len(contenu[index_contenu])):
        contenu[index_contenu][index_rule] = contenu[index_contenu][index_rule].split()
        del contenu[index_contenu][index_rule][-1]
        if contenu[index_contenu][index_rule][0].isnumeric() == True:
            del contenu[index_contenu][index_rule] [0]



Liste_contenant = [['shiny', 'gold']]
Liste_sac_couleur = []
while Liste_contenant != []:
    Liste_intermediaire=[]
    for rule in contenu:
        for contenant in Liste_contenant:
            if contenant in rule:
                if rule[0] not in Liste_sac_couleur:
                    Liste_sac_couleur.append(rule[0])
                    Liste_intermediaire.append(rule[0])
    Liste_contenant = Liste_intermediaire
new_list = [] 
for i in Liste_sac_couleur : 
    if i not in new_list and i != ['shiny', 'gold']: 
        new_list.append(i) 
Liste_sac_couleur = new_list
print(len(Liste_sac_couleur))



#puzzle 2
file = open('day_7.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n')
for index in range(len(contenu)):
    contenu[index]= re.split(', | contain ', contenu[index])
    contenu[index][-1] = contenu[index][-1][:-1]

for index_contenu in range (len(contenu)):
    for index_rule in range(len(contenu[index_contenu])):
        contenu[index_contenu][index_rule] = contenu[index_contenu][index_rule].split()
        del contenu[index_contenu][index_rule][-1]
        contenu[index_contenu][index_rule][-2] = ' '.join([contenu[index_contenu][index_rule][-2], contenu[index_contenu][index_rule][-1]])
        del contenu[index_contenu][index_rule][-1]
print(contenu)

#def recupperer_sac(sac, contenu)

def recherche_sac(sac, contenu):
    for rule in contenu:
        if rule[0] == sac:
            return rule
    return 'probleme' 

def calcul_sac(sac, contenu):
    rule = recherche_sac(sac, contenu)
    rule = rule[1:]
    calcul = 1
    if rule == [['no other']]:
        return 1
    else:
        for bag in rule:
            calcul = calcul + int(bag[0]) * calcul_sac([bag[1]],contenu)
        return calcul


print(calcul_sac(['shiny gold'], contenu)-1) # -1 correspond au compte du sac shinny gold