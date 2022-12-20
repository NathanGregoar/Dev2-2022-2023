class Ocean:
    """La classe 'Ocean' crée le plateau de jeu ou le joueur place ses bateaux.
    La classe contient toutes les données sur les bateaux placés"""

    def __init__(self, width=10, height=10):
        self.ocean = [["~" for i in range(width)] for i in range(height)]

    def __getitem__(self, point):
        row, col = point
        return self.ocean[row][col]

    def __setitem__(self, point, value):
        row, col = point
        self.ocean[row][col] = value

    def view_ocean(self):
        for row in self.ocean:
            print(" ".join(row))

    # Deux méthodes pour vérifier les coordonnées des bateaux placés

    def valid_col(self, row):
        try:
            self.ocean[row]
            return True
        except IndexError:
            return False

    def valid_row(self, col):
        try:
            self.ocean[0][col]
            return True
        except IndexError:
            return False

    # Deux méthodes pour vérifier la validité des coordonnées choisies

    def can_use_col(self, row, col, size):

        valid_coords = []

        for i in range(size):

            if self.valid_col(col) and self.valid_row(row):
                if self.ocean[row][col] == "~":
                    valid_coords.append((row, col))
                    col = col + 1
                else:
                    col = col + 1
            else:
                return False

        if size == len(valid_coords):
            return True
        else:
            return False

    def can_use_row(self, row, col, size):

        valid_coords = []

        for i in range(size):

            if self.valid_row(row) and self.valid_col(col):
                if self.ocean[row][col] == "~":
                    valid_coords.append((row, col))
                    row = row + 1
                else:
                    row = row + 1
            else:
                return False

        if size == len(valid_coords):
            return True
        else:
            return False

    # Deux méthodes qui placent les bateaux aux endroits valides

    def set_ship_col(self, row, col, size):
        for i in range(size):
            self.ocean[row][col] = "S"
            col = col + 1

    def set_ship_row(self, row, col, size):
        for i in range(size):
            self.ocean[row][col] = "S"
            row = row + 1