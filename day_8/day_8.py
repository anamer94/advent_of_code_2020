import re
import random

file = open('day_8.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n')
for index in range(len(contenu)):
    contenu[index]= re.split(' ', contenu[index])
print(contenu)


#puzzle 1

def acc (nombre, index, accumulateur):
    return(index+1, accumulateur+int(nombre))

def jmp (nombre,index,accumulateur):
    return(index+int(nombre), accumulateur)

def nop (nombre,index,accumulateur):
    return (index+1, accumulateur)

def repartition (ligne,index,accumulateur):
    nom = ligne[0]
    if nom == 'acc':
        return acc (ligne[1], index, accumulateur)
    elif nom == 'jmp':
        return jmp (ligne[1], index, accumulateur)
    else:
        return nop (ligne[1], index, accumulateur)

def jeu (contenu):
    liste_index = []
    index = 0
    accumulateur = 0
    while index not in liste_index:
        liste_index.append (index)
        ligne = contenu [index]
        index,accumulateur = repartition(ligne,index,accumulateur)
        if index >= len(contenu)-1:
            break
    return index,accumulateur

print(jeu(contenu))

# puzzle 2

def modification(numero_ligne, contenu):
    contenu_mod = contenu[:]
    if contenu[numero_ligne][0] == 'acc':
        return None
    elif contenu[numero_ligne][0] == 'jmp':
        contenu_mod[numero_ligne][0] = 'nop'
        return contenu_mod
    else:
        contenu_mod[numero_ligne][0] = 'jmp'
        return contenu_mod


def puzzle_2(contenu):
    numero_ligne = 0

    while numero_ligne<654:
        contenu_mod = modification(numero_ligne,contenu)
        if contenu_mod != None:
            index,accumulateur = jeu (contenu_mod)
            if index == 653:            
                index_f = index
                accumulateur_f = accumulateur
                break
        contenu_mod = modification(numero_ligne,contenu)
        numero_ligne = numero_ligne + 1
    return (index, accumulateur)

print(puzzle_2(contenu))