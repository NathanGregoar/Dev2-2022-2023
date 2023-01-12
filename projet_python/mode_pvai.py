from mode_pvp import Mode_PVP
from ia import IA
from joueur import Joueur
from tableau_scores import Tableau_scores


class mode_PVAI(Mode_PVP):
    """La classe 'BattlshipsCOMP' permet de gérer la partie contre l'ordinateur.
    Elle hérite de la classe 'BattleshipsPVP"""

    def __init__(self):
        debut = input("Commencer une partie ? (o ou n) -----> ")
        if debut in ["o", "O"]:
            self.playCOMP()
        else:
            print("Avorté...")

    def playCOMP(self):
        nom_joueur = input("Joueur 1, encode ton nom ! -----> ").capitalize()
        p = Joueur(nom_joueur)
        p.positionner_flotte()
        p.afficher_console()
        self.prochain_tour()

        c = IA()
        print("L'ordinateur place ses bateaux...")
        c.placer_flotte_IA()
        self.prochain_tour()

        flag = True
        while flag is True:
            p.tir(c)
            if self.flotte_coulee(c) is True:
                self.message_victoire(p, c)
                nouveau_score_joueur = Tableau_scores(nom_joueur, p.score)
                nouveau_score_joueur.Maj_score()
                flag = False
            else:
                self.prochain_tour()

                c.tir_IA(p)
                if self.flotte_coulee(p) is True:
                    self.message_victoire(c, p)
                    flag = False
                else:
                    self.prochain_tour()
        print("\nMerci d'avoir joué!")