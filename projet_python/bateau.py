class Bateau:

    def __init__(self, classe_bateau, taille):
        """
            Initialise un navire avec un type et une taille donnés.

            PRE:
                - classe_bateau est un str représentant le type de navire.
                - taille est un entier représentant la taille du navire.
            POST:
                - Le navire est initialisé avec les valeurs de classe_bateau et taille.
                - La liste des coordonnées du navire est initialisée vide.
        """

        self.classe_bateau = classe_bateau
        self.taille = taille
        self.coords = []

    def placer_verticalement(self, rangee, colonne):
        """
            Trace un navire verticalement à partir de la coordonnée (row, col) donnée.

            PRE:
                - rangee est un entier représentant la ligne où le navire commence.
                - colonne est un entier représentant la colonne où le navire commence.
            POST:
                - Les coordonnées du navire sont ajoutées à la liste self.coords.
                - La liste self.coords contient toutes les coordonnées du navire, en partant de (rangee, colonne) et
                en s'incrémentant de 1 en ligne à chaque itération.
        """

        self.coords = [(rangee + i, colonne) for i in range(self.taille)]

    def placer_horizontalement(self, rangee, colonne):
        """
            Trace un navire horizontalement à partir de la coordonnée (row, col) donnée.

            PRE:
                - rangee est un entier représentant la ligne où le navire commence.
                - colonne est un entier représentant la colonne où le navire commence.
            POST:
                - Les coordonnées du navire sont ajoutées à la liste self.coords.
                - La liste self.coords contient toutes les coordonnées du navire, en partant de (rangee, colonne) et en
                  s'incrémentant de 1 en colonne à chaque itération.
        """

        self.coords = [(rangee, colonne + i) for i in range(self.taille)]

    def check_etat_bateau(self):
        """
            Vérifie si le navire est coulé ou non.

            PRE:
                - /
            POST:
                - Retourne True si la liste self.coords est vide, False sinon.
        """

        return not bool(self.coords)
