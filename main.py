# Module random pour le randint
# ‘X’ indique le bateau touché
# ‘-‘ indique le tir manqué
from random import randint

Hidden_Pattern = [[' '] * 8 for x in range(8)]
Guess_Pattern = [[' '] * 8 for x in range(8)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    print(' A B C D E F G H')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def get_ship_location():
    # Entrer une valeure de 1 à 8 pour spécifier le numero de ligne
    row = input('Entrer une ligne entre 1 et 8 ').upper()
    while row not in '12345678':
        print("Entrer un nombre valide (entre 1 et 8)")
        row = input('Entrer une ligne entre 1 et 8 ')
    # Entrer une valeure de A à H pour spécifier le numero de colonne
    column = input('Entrer une colonne entre A et H ').upper()
    while column not in 'ABCDEFGH':
        print("Entrer une colonne valide (entre A et H)")
        column = input('Entrer une colonne entre A et H ')
    return int(row) - 1, let_to_num[column]


# Fonction placent des bateaux (5) aléatoirement sur la grille
def create_ships(board):
    for ship in range(5):
        ship_x, ship_y = randint(0, 7), randint(0, 7)
        while board[ship_x][ship_y] == 'X':
            ship_x, ship_y = randint(0, 7), randint(0, 7)
        board[ship_x][ship_y] = 'X'


# fonction le nombre de bateaux touchés
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(Hidden_Pattern)
print_board(Hidden_Pattern)  # grille avec les bateaux affichés (pour le debuggage)
turns = 16
print('Bienvenu Monsieur Sparrow')
while turns > 0:
    print_board(Guess_Pattern)
    row, column = get_ship_location()
    if Guess_Pattern[row][column] == '-' or Guess_Pattern[row][column] == 'X':
        print('Vous avez déjà tiré ici')
    elif Hidden_Pattern[row][column] == 'X':
        print(' Bien joué ! Vous avez détruit un bateau !')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('Pas de chance, c\'est raté')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if count_hit_ships(Guess_Pattern) == 5:
        print("Victoire ! Bravo Monsieur Sparrow vous êtes le meilleur")
        break
    print(' Il vous reste ' + str(turns) + ' tirs ')
    if turns == 0:
        print('Game Over')