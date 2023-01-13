class TableauDeJeu:

    def __init__(self, largeur=10, hauteur=10):
        """
            Initialise le plateau de jeu qui possède une largeur et une hauteur.

            PRE:
                - largeur est un entier représentant la largeur du plateau de jeu.
                - hauteur est un entier représentant la hauteur de plateau de jeu.
            POST:
                - Le plateau de jeu est initialisé avec les valeurs de largeur et hauteur.
                - Le plateau de jeu est initialisé avec une grille remplie de "~" (Représentation de l'eau).
        """

        self.tableau = [["~" for i in range(largeur)] for i in range(hauteur)]

    def __getitem__(self, point):
        """
            Renvoie la valeur du plateau de jeu à la coordonnée point donnée.

            PRE:
                - point est un tuple (séquence non modifiable de données ordonnées) de deux entiers représentant
                  une coordonnée de l'océan.
            POST:
                - Retourne la valeur de l'océan à la coordonnée point.
        """

        rangee, colonne = point
        return self.tableau[rangee][colonne]

    def __setitem__(self, point, valeur):
        """
            Modifie la valeur du plateau de jeu à la coordonnée point donnée.

            PRE:
            - point est un tuple de deux entiers représentant une coordonnée valide de l'océan.
            - valeur est une valeur à insérer dans l'océan.
            POST:
                - La valeur de l'océan à la coordonnée point est modifiée par valeur.
        """

        rangee, colonne = point
        self.tableau[rangee][colonne] = valeur

    def voir_tableau(self):
        """
            Affiche le plateau de jeu sous forme de grille.

            PRE:
                - /
            POST:
                - Le plateau de jeu est affiché sous forme de grille en console.
        """

        for rangee in self.tableau:
            print(" ".join(rangee))

    def col_valide(self, rangee):
        """
            Vérifie si la ligne rangee est une ligne valide du plateau de jeu.

            PRE:
                - rangee est un entier représentant une ligne du plateau de jeu.
            POST:
                - Retourne True si la ligne rangee est valide, False sinon.
        """

        try:
            self.tableau[rangee]
            return True
        except IndexError:
            return False

    def rang_valide(self, colonne):
        """
            Vérifie si colonne est une colonne valide du plateau de jeu.

            PRE:
                - colonne est un entier représentant une colonne du plateau de jeu.
            POST:
                - Retourne True si colonne est valide, False sinon.
        """

        try:
            self.tableau[0][colonne]
            return True
        except IndexError:
            return False

    def position_colonne_valide(self, rangee, colonne, taille):
        """
            Vérifie si colonne peut accueillir un navire de "taille".

            PRE:
                - rangee est un entier représentant une ligne du plateau de jeu.
                - colonne est un entier représentant une colonne du plateau de jeu.
                - taille est un entier représentant la taille du navire à placer.
            POST:
                - Retourne True si colonne peut accueillir un navire de "taille", False sinon.
        """

        coord_valides = []

        for i in range(taille):

            if self.col_valide(colonne) and self.rang_valide(rangee):
                if self.tableau[rangee][colonne] == "~":
                    coord_valides.append((rangee, colonne))
                    colonne = colonne + 1
                else:
                    colonne = colonne + 1
            else:
                return False

        if taille == len(coord_valides):
            return True
        else:
            return False

    def position_rangee_valide(self, rangee, colonne, taille):
        """
            Vérifie si la ligne rangee peut accueillir un navire de "taille".

            PRE:
                - rangee est un entier représentant une ligne du plateau de jeu.
                - colonne est un entier représentant une colonne du plateau de jeu.
                - taille est un entier représentant la taille du navire à placer.
            POST:
                - Retourne True si la ligne rangee peut accueillir un navire de "taille", False sinon.
        """

        coord_valides = []

        for i in range(taille):

            if self.rang_valide(rangee) and self.col_valide(colonne):
                if self.tableau[rangee][colonne] == "~":
                    coord_valides.append((rangee, colonne))
                    rangee = rangee + 1
                else:
                    rangee = rangee + 1
            else:
                return False

        if taille == len(coord_valides):
            return True
        else:
            return False

    def def_col_bateau(self, rangee, colonne, taille):
        """
            Place un navire de "taille" dans colonne du plateau de jeu.

            PRE:
                - rangee est un entier représentant une ligne du plateau de jeu.
                - colonne est un entier représentant une colonne du plateau de jeu.
                - taille est un entier représentant la taille du navire à placer.
                - colonne peut accueillir un navire de "taille".
            POST:
                - Un navire de "taille" est placé dans colonne du plateau de jeu.
        """

        for i in range(taille):
            self.tableau[rangee][colonne] = "S"
            colonne = colonne + 1

    def def_rang_bateau(self, rangee, colonne, taille):
        """
            Place un navire de "taille" dans la ligne rangee du plateau de jeu.

            PRE:
                - rangee est un entier représentant une ligne du plateau de jeu.
                - colonne est un entier représentant une colonne du plateau de jeu.
                - taille est un entier représentant la taille du navire à placer.
                - La ligne rangee peut accueillir un navire de "taille".
            POST:
                - Un navire de "taille" est placé dans la ligne rangee de l'océan.
        """

        for i in range(taille):
            self.tableau[rangee][colonne] = "S"
            rangee = rangee + 1
