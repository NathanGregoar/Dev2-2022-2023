from mode_pvp import Mode_PVP
from mode_pvai import mode_PVAI
import tableau_scores

# Le script principal pour lancer la partie


def Main():
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
                Mode_PVP()
            elif mode == 2:
                flag = False
                mode_PVAI()
            elif mode == 3:
                flag = False
                tableau_scores.Tableau_scores.afficher_leaderboard()
            else:
                continue
        except ValueError:
            print("Vous ne pouvez que choisir entre l'option 1, 2 ou 3")


Main()