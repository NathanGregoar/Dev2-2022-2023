class Radar:
    """La classe 'Radar' permet de voir ses tirs et si ils sont touché ou raté"""


    def __init__(self, largeur=10, hauteur=10):
        self.radar = [["." for i in range(largeur)] for i in range(hauteur)]

    def __getitem__(self, point):
        rangee, colonne = point
        return self.radar[rangee][colonne]

    def __setitem__(self, point, valeur):
        rangee, colonne = point
        self.radar[rangee][colonne] = valeur

    def afficher_radar(self):
        for rangee in self.radar:
            print(" ".join(rangee))