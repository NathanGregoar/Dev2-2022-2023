from player import Player
from ship import Ship
import random


class Computer(Player):
    """La classe 'Computer' hérite de la classe 'Player'. Elle stock les données de l'ordinateur
    et lui permet de faire des actions pour le mode PVC"""


    def __init__(self):
        super().__init__(self)
        self.name = "Ordinateur"

    # Version automatisée de la méthode set_fleet de la classe Player

    def set_compu_fleet(self):
        positions = ["v", "h"]

        for ship, size in self.ships.items():

            flag = True
            while flag:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                orientation = random.choice(positions)

                if orientation == "v":
                    if self.ocean.can_use_row(row, col, size):
                        self.ocean.set_ship_row(row, col, size)
                        boat = Ship(ship, size)
                        boat.plot_vertical(row, col)
                        self.fleet.append(boat)
                        flag = False

                    else:
                        row = row + 2

                elif orientation == "h":
                    if self.ocean.can_use_col(row, col, size):
                        self.ocean.set_ship_col(row, col, size)
                        boat = Ship(ship, size)
                        boat.plot_horizontal(row, col)
                        self.fleet.append(boat)
                        flag = False

                    else:
                        col = col + 2

                else:
                    continue

                # Méthode automatisée pour gérer les tirs

    def compu_strike(self, target):
        row = random.randint(0, 9)
        col = random.randint(0, 9)

        if self.radar.radar[row][col] == ".":
            input(f"...Recherche de la Cible....")
            input(f"Tir sur cible en ({row}, {col})")

            if target.ocean.ocean[row][col] == "S":
                print("TOUCHÉ!!!")
                target.ocean.ocean[row][col] = "X"
                target.register_hit(row, col)
                self.radar.radar[row][col] = "X"

            else:
                print("Raté....recalibrage")
                self.radar.radar[row][col] = "O"

        else:
            self.compu_strike(target)