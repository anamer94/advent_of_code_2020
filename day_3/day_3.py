file = open('day_3.txt','r')
contenu = file.read()
file.close()
contenu = contenu.split('\n')
for index in range(len(contenu)):
    contenu[index]= [elt for elt in contenu[index]]
print(contenu)

#puzzle 1
position = [0,0]
nombre_colonne = len (contenu[index])
nombre_ligne = len(contenu)
nombre_arbre=0

while position[0] < nombre_ligne:
    if contenu[position[0]][position[1]] == '#':
        nombre_arbre = nombre_arbre + 1
    position = [position[0]+1, (position[1]+3)%nombre_colonne]

print(nombre_arbre)

#puzzle 2

nombre_colonne = len (contenu[index])
nombre_ligne = len(contenu)
multiplication_nombre_arbre=1
liste_deplacement = [[1,1], [3,1],[5,1],[7,1],[1,2]]

for deplacement in liste_deplacement:
    nombre_arbre=0
    position = [0,0]
    while position[0] < nombre_ligne:
        if contenu[position[0]][position[1]] == '#':
            nombre_arbre = nombre_arbre + 1
        position = [position[0]+deplacement[1], (position[1]+deplacement[0])%nombre_colonne]
    multiplication_nombre_arbre = multiplication_nombre_arbre * nombre_arbre
    print(multiplication_nombre_arbre)

print(multiplication_nombre_arbre)
    


