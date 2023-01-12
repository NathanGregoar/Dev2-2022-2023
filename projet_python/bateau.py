class Bateau:
    """La classe 'Ship' permet de stocker les coordonnées du bateau(x, y) et son type(Croiseur, Destroyer, etc...)"""


    def __init__(self, classe_bateau, taille):
        self.classe_bateau = classe_bateau
        self.taille = taille
        self.coords = []

    def placer_verticalement(self, rangee, colonne):
        for i in range(self.taille):
            self.coords.append((rangee, colonne))
            rangee = rangee + 1

    def placer_horizontalement(self, rangee, colonne):
        for i in range(self.taille):
            self.coords.append((rangee, colonne))
            colonne = colonne + 1

    def check_etat_bateau(self):
        if self.coords == []:
            return True
        else:
            return False