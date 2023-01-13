from mode_pvp import Mode_PVP
from ia import IA
from joueur import Joueur
from tableau_scores import Tableau_scores


class mode_PVAI(Mode_PVP):
    """
        La classe 'Mode_PVAI' permet de gérer une partie en mode joueur contre IA (PVAI) dans le jeu touché_coulé.
        Cette classe hérite de la classe 'Mode_PVP'. Elle utilise des instances de la classe Joueur et Tableau_scores pour gérer les joueurs et les scores.
    """
    def __init__(self):
        """
                PRE: Aucune entrée
                POST: Elle initialise la partie en demandant à l'utilisateur s'il souhaite commencer une partie
                      - Si l'utilisateur entre "o" ou "O", la partie commence en appelant la méthode playCOMP()
                      - Sinon, elle affiche "Avorté..." et la partie est annulée
        """

        debut = input("Commencer une partie ? (o ou n) -----> ")
        if debut in ["o", "O"]:
            self.jouer_PVAI()
        else:
            print("Avorté...")

    def jouer_PVAI(self):
        """
                PRE: Aucune entrée
                POST: Elle gère une partie de bataille navale contre l'ordinateur
                      - Elle demande à l'utilisateur de saisir son nom
                      - Elle crée un objet Joueur pour l'utilisateur et lui demande de positionner sa flotte sur le tableau
                      - Elle crée un objet IA pour l'ordinateur et lui demande de positionner sa flotte sur le tableau
                      - Elle gère les tours de jeu jusqu'à ce qu'un des joueurs coule tous les navires de l'autre
                      - Elle affiche un message de victoire en fin de partie
        """

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