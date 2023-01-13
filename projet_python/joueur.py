from tableau_de_jeu import TableauDeJeu
from radar import Radar
from bateau import Bateau


class Joueur:
    bateaux = {"Porte-avion": 5, "Croiseur": 4, "Destroyer": 3, "Frégate": 2}

    def __init__(self, nom):
        """
            Initialise un joueur avec un nom donné.

            PRE:
                - nom est une chaîne de caractères représentant le nom du joueur.
            POST:
                - Le joueur est initialisé avec un océan, un radar et le nom donné.
                - Le joueur a un score initialisé à 0.
                - Le joueur a une flotte initialement vide.
        """

        self.tableau = TableauDeJeu()
        self.radar = Radar()
        self.nom = nom
        self.flotte = []
        self.score = 0

    def positionner_flotte(self):
        """
            Demande au joueur de placer sa flotte sur le plateau de jeu.

            PRE:
                - /
            POST:
                - La flotte du joueur est placée sur le plateau de jeu.
        """

        input("Encodez des chiffres entre 0 et 9 pour choisir les rangées et les colonnes sur le plateau de jeu")
        input("Les bateaux se place de gauche à droite et de haut en bas")
        for bateau, taille in self.bateaux.items():

            flag = True
            while flag:
                self.afficher_console()
                try:
                    print(f"Placer le {bateau}")
                    rangee = int(input("Quelle rangée ? "))
                    colonne = int(input("Quelle colonne ? "))
                    orientation = str(
                        input("Placer le bateau à la verticale (v) ou à l'horizontale (h) ?"))

                    if orientation in ["v", "V"]:
                        if self.tableau.position_rangee_valide(rangee, colonne, taille):
                            self.tableau.def_rang_bateau(rangee, colonne, taille)
                            navire = Bateau(bateau, taille)
                            navire.placer_verticalement(rangee, colonne)
                            self.flotte.append(navire)
                            flag = False
                        else:
                            input("Plusieurs bateaux se croisent, mettez-le ailleurs !")

                    elif orientation in ["h", "H"]:
                        if self.tableau.position_colonne_valide(rangee, colonne, taille):
                            self.tableau.def_col_bateau(rangee, colonne, taille)
                            navire = Bateau(bateau, taille)
                            navire.placer_horizontalement(rangee, colonne)
                            self.flotte.append(navire)
                            flag = False
                        else:
                            input("Plusieurs bateaux se croisent, mettez-le ailleurs !")

                    else:
                        continue
                    self.afficher_console()

                except ValueError:
                    print("Veuillez entrer un chiffre de 0 à 9 !")

    def afficher_console(self):
        """
            Affiche le radar et le plateau de jeu du joueur.

            PRE:
                - /
            POST:
                - Le radar et le plateau de jeu du joueur sont affichés.
        """

        self.radar.afficher_radar()
        print("|                 |")
        self.tableau.voir_tableau()

    def enregistrer_tir(self, rangee, colonne):
        """
            Enregistre un coup reçu par le joueur à la coordonnée (rangee, colonne).

            PRE:
                - rangee est un entier représentant une ligne du plateau de jeu.
                - colonne est un entier représentant une colonne du plateau de jeu.
            POST:
                - Si un navire de la flotte du joueur est touché à la coordonnée (rangee, colonne), cette coordonnée
                  est retirée de la liste des coordonnées du navire.
                - Si le navire est coulé, il est retiré de la flotte du joueur et un message est affiché indiquant que
                  le navire a été coulé.
        """

        for navire in self.flotte:
            if (rangee, colonne) in navire.coords:
                navire.coords.remove((rangee, colonne))
                if navire.check_etat_bateau():
                    self.flotte.remove(navire)
                    print("Coulé !")
                    print(f"Le {navire.classe_bateau} de l'ennemi {self.nom} a été coulé !")

    def tir(self, cible):
        """
            Fait attaquer le joueur ciblé par un autre joueur.

            PRE:
                - self est un objet joueur représentant le joueur effectuant l'attaque.
                - cible est un objet joueur représentant le joueur ciblé par l'attaque.
            POST:
                - Le joueur ciblé est attaqué et son bateau est touché s'il se trouve sur les coordonnées choisies.
                - La grille de radar du joueur effectuant l'attaque est mise à jour en fonction de la réussite ou
                  l'échec de l'attaque.
                - Le score du joueur effectuant l'attaque est mis à jour en fonction de la réussite ou non de l'attaque.
        """

        self.afficher_console()
        try:
            print(f"\n{self.nom} choisissez votre cible...")
            row = int(input("Quelle rangée ?"))
            col = int(input("Quelle colonne ?"))

            if self.tableau.rang_valide(row) and self.tableau.col_valide(col):
                if cible.tableau.tableau[row][col] == "S":
                    print("TOUCHÉ!!!")
                    self.score -= 1
                    cible.tableau.tableau[row][col] = "X"
                    cible.enregistrer_tir(row, col)
                    self.radar.radar[row][col] = "X"

                else:
                    if self.radar.radar[row][col] == "O":
                        print("Vous avez déja tiré ici ! Vérifier votre radar !")
                        self.tir(cible)
                    elif self.radar.radar[row][col] == "X":
                        print("Vous avez déja tiré ici ! Vérifier votre radar !")
                        self.tir(cible)
                    else:
                        print("Raté...")
                        self.radar.radar[row][col] = "O"
                        self.score -= 1

            else:
                print("Hors zone !")
                self.tir(cible)
        except ValueError:
            print("Veuillez entrer un nombre !")
            self.tir(cible)
