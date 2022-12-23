import re

file = open('day_4.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n\n')
for index in range(len(contenu)):
    contenu[index]= re.split('\n| ', contenu[index])
print(contenu)

#puzzle 1
liste_passeport_valide_puzzle_1 = []
liste_a_verifier = ['byr','iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
nombre_valide = 0
for passeport in contenu:
    champ_ok = 0
    for champ in liste_a_verifier:
        for element in passeport:
            if element[0:3] == champ:
                champ_ok = champ_ok + 1
    if champ_ok == 7:
        liste_passeport_valide_puzzle_1.append(passeport)
        nombre_valide = nombre_valide +1
print(nombre_valide)

# puzzle 2


def byr (champ):
    annee = int(champ[4:])
    if annee>2002:
        return 1
    if annee<1920:
        return 1
    return 0

def iyr (champ):
    annee = int(champ[4:])
    if annee>2020:
        return 1
    if annee<2010:
        return 1
    return 0


def eyr (champ):
    annee = int(champ[4:])
    if annee>2030:
        return 1
    if annee<2020:
        return 1
    return 0


def hgt (champ):
    if len(champ)>6:
        annee = int(champ[4:len(champ)-2])
        mesure = champ[len(champ)-2:]
        if mesure == 'cm':
            if annee>193:
                return 1
            if annee<150:
                return 1
            return 0
        elif mesure == 'in':
            if annee>76:
                return 1
            if annee<59:
                return 1
            return 0
    return 1

def hcl (champ):
    diese = champ[4]
    numero_lettre = champ[5:]
    if len(numero_lettre) != 6:
        return 1
    liste_lettre = ['a','b','c','d','e','f']
    if diese != '#':
        return 1
    for element in numero_lettre:
        if element in liste_lettre or element.isnumeric() == True:
            return 0
    return 1

def ecl (champ):
    liste = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    eye = champ[4:]
    if eye in liste:
        return 0
    return 1

def pid (champ):
    id = champ[4:]
    if len(id) != 9:
        return 1
    if id.isnumeric() != True:
        return 1
    return 0

def repartition_fonction_champ (champ):
    nom_champ = champ[:3]
    ok = 1
    if nom_champ == 'byr':
        ok = byr (champ)
    elif nom_champ == 'iyr':
        ok = iyr (champ)
    elif nom_champ == 'eyr':
        ok = eyr (champ)
    elif nom_champ == 'hgt':
        ok = hgt (champ)
    elif nom_champ == 'hcl':
        ok = hcl (champ)
    elif nom_champ == 'ecl':
        ok = ecl (champ)
    elif nom_champ == 'pid':
        ok = pid (champ)
    elif nom_champ == 'cid':
        ok = 0
    return ok


print(liste_passeport_valide_puzzle_1)
nombre_valide = 0
for passeport in liste_passeport_valide_puzzle_1:
    champ_ok = 0
    for element in passeport:
        champ_ok = champ_ok + repartition_fonction_champ (element)
    if champ_ok == 0:
        nombre_valide = nombre_valide + 1
print(nombre_valide)


            
    

    

