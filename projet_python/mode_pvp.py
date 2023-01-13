from joueur import Joueur
from tableau_scores import Tableau_scores


class Mode_PVP:
    """
    La classe 'Mode_PVP' permet de gérer une partie en mode joueur contre joueur (PVP) dans le jeu Battleship.
    Elle utilise des instances de la classe Joueur et Tableau_scores pour gérer les joueurs et les scores.
    """
    def __init__(self):
        """
           Constructeur de la classe
           PRE : None
           POST : Demande si le joueur souhaite démarrer une partie ou non. Si oui, la méthode 'PVP' est appelée.
           Sinon, le message "Avorté..." est affiché.
        """

        start = input("Commencer une partie? (choisir o ou n) -----> ")
        if start in ["o", "O"]:
            self.PVP()
        else:
            print("Avorté...")

    def PVP(self):
        """
            Permet de démarrer une partie en mode PVP.
            PRE : None
            POST : Demande les noms des deux joueurs, crée des instances de la classe Joueur pour chaque joueur, les fait positionner leurs flottes, et affiche leur tableau de jeu.
            Gère les tours de jeu en utilisant une boucle while qui continue tant que la flotte d'aucun joueur n'est coulée.
            Appelle les méthodes 'tir', 'flotte_coulee', 'prochain_tour' et 'message_victoire' pour gérer les tours de jeu,
             vérifier si la flotte d'un joueur est coulée, afficher un message pour passer au tour suivant et afficher un message de victoire.
        """

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
        """
           Vérifie s'il reste des navires sur le tableau de jeu d'un joueur donné
           PRE : joueur (instance de la classe Joueur)
           POST : retourne True si il n'y a plus de navires sur le tableau, False sinon
        """

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
        """
          Affiche un message pour passer au tour suivant
          PRE : None
          POST : Affiche le message "Prochain tour ?"
        """

        ("\n Prochain tour ? \n")

    def message_victoire(self, vainqueur, perdant):
        """
          Affiche un message de victoire pour le joueur vainqueur et le nom et le score de celui-ci
          PRE : vainqueur (instance de la classe Joueur) perdant (instance de la classe Joueur)
          POST : Affiche le message de victoire et les informations du joueur vainqueur
        """

        print("\n\n\n*****************************************")
        print(f"La flotte de {perdant.nom} a été détruite, le vainqueur est {vainqueur.nom} !")
        print("*****************************************")
        print(f"{vainqueur.nom}, ton score est de : {vainqueur.score}")
