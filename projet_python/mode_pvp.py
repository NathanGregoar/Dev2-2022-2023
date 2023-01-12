from joueur import Joueur
from tableau_scores import Tableau_scores


class Mode_PVP:
    """La classe 'BattleshipsPVP permet de gérer la partie en mode PVP'"""

    def __init__(self):
        start = input("Commencer une partie? (choisir o ou n) -----> ")
        if start in ["o", "O"]:
            self.PVP()
        else:
            print("Avorté...")


    def PVP(self):
        nom_joueur1 = input("Joueur 1, encode ton nom ! -----> ").capitalize()
        j1 = Joueur(nom_joueur1)
        j1.positionner_flotte()
        j1.afficher_console()
        self.prochain_tour()

        nom_joueur2 = input("\n\nJoueur 2, encode ton nom ! -----> ").capitalize()
        j2 = Joueur(nom_joueur2)
        j2.positionner_flotte()
        j2.afficher_console()
        self.prochain_tour()

        flag = True
        while flag is True:
            j1.tir(j2)
            if self.flotte_coulee(j2) is True:
                nouveau_score_joueur = Tableau_scores(nom_joueur1, j1.score)
                nouveau_score_joueur.Maj_score()
                self.message_victoire(j1, j2)
                flag = False
            else:
                j2.tir(j1)
                if self.flotte_coulee(j1) is True:
                    nouveau_score_joueur = Tableau_scores(nom_joueur2, j2.score)
                    nouveau_score_joueur.Maj_score()
                    self.message_victoire(j2, j1)
                    flag = False
                else:
                    self.prochain_tour()
        print("\nMerci d'avoir joué !")

        # Function checks remaining ship counters on a player's board

    def flotte_coulee(self, joueur):
        compteur_bateaux = 0
        """Traverse la grille à la recherche des S"""
        for rangee in range(len(joueur.tableau.tableau)):
            for colonne in range(len(joueur.tableau.tableau)):
                if joueur.tableau.tableau[rangee][colonne] == "S":
                    compteur_bateaux += 1
        if compteur_bateaux == 0:
            return True
        else:
            return False

    def prochain_tour(self):
        ("\n Prochain tour ? \n")

    def message_victoire(self, vainqueur, perdant):
        print("\n\n\n*****************************************")
        print(f"La flotte de {perdant.nom} a été détruite, le vainqueur est {vainqueur.nom} !")
        print("*****************************************")
        print(f"{vainqueur.nom}, ton score est de : {vainqueur.score}")
