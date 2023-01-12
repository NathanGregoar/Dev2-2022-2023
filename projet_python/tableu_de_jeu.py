class Tableu_de_jeu:
    """La classe 'Ocean' crée le plateau de jeu ou le joueur place ses bateaux.
    La classe contient toutes les données sur les bateaux placés"""

    def __init__(self, largeur=10, hauteur=10):
        self.tableau = [["~" for i in range(largeur)] for i in range(hauteur)]

    def __getitem__(self, point):
        rangee, colonne = point
        return self.tableau[rangee][colonne]

    def __setitem__(self, point, valeur):
        rangee, colonne = point
        self.tableau[rangee][colonne] = valeur

    def voir_tableau(self):
        for rangee in self.tableau:
            print(" ".join(rangee))

    # Deux méthodes pour vérifier les coordonnées des bateaux placés

    def col_valide(self, rangee):
        try:
            self.tableau[rangee]
            return True
        except IndexError:
            return False

    def rang_valide(self, colonne):
        try:
            self.tableau[0][colonne]
            return True
        except IndexError:
            return False

    # Deux méthodes pour vérifier la validité des coordonnées choisies

    def position_colonne_valide(self, rangee, colonne, taille):

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

    # Deux méthodes qui placent les bateaux aux endroits valides

    def def_col_bateau(self, rangee, colonne, taille):
        for i in range(taille):
            self.tableau[rangee][colonne] = "S"
            colonne = colonne + 1

    def def_rang_bateau(self, rangee, colonne, taille):
        for i in range(taille):
            self.tableau[rangee][colonne] = "S"
            rangee = rangee + 1