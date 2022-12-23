file_puzzle_1 = open('day_1.txt','r')
contenu_puzzle_1 = file_puzzle_1.read()
file_puzzle_1.close()
contenu_puzzle_1 = contenu_puzzle_1.split('\n')
for index in range(len(contenu_puzzle_1)):
    contenu_puzzle_1[index] = int(contenu_puzzle_1[index])

# puzzle 1
for nombre_1 in contenu_puzzle_1:
    for nombre_2 in contenu_puzzle_1:
        if nombre_1+nombre_2 == 2020:
            print([nombre_1, nombre_2, nombre_1*nombre_2])

#puzzle 2
for nombre_1 in contenu_puzzle_1:
    for nombre_2 in contenu_puzzle_1:
        for nombre_3 in contenu_puzzle_1:
                if nombre_1+nombre_2+nombre_3 == 2020:
                    print([nombre_1, nombre_2, nombre_3, nombre_1*nombre_2*nombre_3])