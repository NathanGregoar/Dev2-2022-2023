from battleshipspvp import BattleshipsPVP
from battleshipscomp import BattleshipsCOMP
import leaderboard

# Le script principal pour lancer la partie


def playbattleships():
    print("\n\n***********************")
    print("Bienvenue à Touché-Coulé!")
    print("***********************\n")

    print("\n 1) Joueur contre Joueur")
    print("\n 2) Joueur contre Ordinateur")
    print("\n 3) Voir le tableau des scores")

    flag = True

    while flag:
        try:
            mode = int(input("\n\nChoisir un chiffre ----> "))
            if mode == 1:
                flag = False
                BattleshipsPVP()
            elif mode == 2:
                flag = False
                BattleshipsCOMP()
            elif mode == 3:
                flag = False
                leaderboard.Leaderboard.print_leaderboard()
            else:
                continue
        except ValueError:
            print("Vous ne pouvez que choisir entre l'option 1, 2 ou 3")


playbattleships()