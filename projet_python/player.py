from ocean import Ocean
from radar import Radar
from ship import Ship

class Player:
    """La classe 'Player' gère les données et les actions des différents joueurs lors de la partie"""

    ships = {"Porte-avion": 5, "Croiseur": 4, "Destroyer": 3, "Frégate": 2}

    def __init__(self, name):
        self.ocean = Ocean()
        self.radar = Radar()
        self.name = name
        self.fleet = []
        self.score = 64

    """Cette méthode utilise les input des joueurs pour placer les bateaux
    pour chaque bateau, un objet ship contenant les coordonnées des bateaux est ajouté au tableau de jeu"""

    def set_fleet(self):
        print("**********NOTE**************")
        input("Il faut encoder des chiffres entre 0 et 9 pour choisir les rangées et les colonnes sur le plateu de jeu")
        input("Les bateaux se place de gauche à droite et de haut en bas")
        print("****************************")
        for ship, size in self.ships.items():

            flag = True
            while flag:
                self.view_console()
                try:
                    print(f"Placer le {ship}")
                    row = int(input("Quelle rangée ? "))
                    col = int(input("Quelle colonne ? "))
                    orientation = str(input("Voulez-vous le placer à la verticale ou à l'horizontale ? (choisir v ou h) "))

                    if orientation in ["v", "V"]:
                        if self.ocean.can_use_row(row, col, size):
                            self.ocean.set_ship_row(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_vertical(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Les bateaux se croisent, placer-le autre part")

                    elif orientation in ["h", "H"]:
                        if self.ocean.can_use_col(row, col, size):
                            self.ocean.set_ship_col(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_horizontal(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Les bateaux se croisent, placer-le autre part")

                    else:
                        continue
                    self.view_console()

                except ValueError:
                    print("Vous avez oublié votre tête soldat ?\nIl faut écrire un chiffre..\n")

    # Cette méthode affiche le radar et l'océan d'une manière lisible

    def view_console(self):
        self.radar.view_radar()
        print("|                 |")
        self.ocean.view_ocean()

    # Cette méthode vérifie le status des différents bateaux de la flotte du joueur

    def register_hit(self, row, col):
        for boat in self.fleet:
            if (row, col) in boat.coords:
                boat.coords.remove((row, col))
                if boat.check_status():
                    self.fleet.remove(boat)
                    print("COULÉ!!!")
                    print(f"Le {boat.ship_type} de l'ennemi {self.name} a été coulé !")

    """L'interface du joueur pour gérer les tirs,
    cette méthode met à jour l'état des plateaux de jeu des joueurs"""

    def strike(self, target):
        self.view_console()
        try:
            print(f"\n{self.name} choisissez votre cible...")
            row = int(input("Quelle rangée ?"))
            col = int(input("Quelle colonne ?"))

            if self.ocean.valid_row(row) and self.ocean.valid_col(col):
                if target.ocean.ocean[row][col] == "S":
                    print("TOUCHÉ!!!")
                    self.score -= 1
                    target.ocean.ocean[row][col] = "X"
                    target.register_hit(row, col)
                    self.radar.radar[row][col] = "X"

                else:
                    if self.radar.radar[row][col] == "O":
                        print("Zone déjà touchée, vérifier votre radar !")
                        self.strike(target)
                    elif self.radar.radar[row][col] == "X":
                        print("Zone déjà touchée, vérifier votre radar !")
                        self.strike(target)
                    else:
                        print("Négatif...")
                        self.radar.radar[row][col] = "O"
                        self.score -= 1

            else:
                print("Coordonnées hors d'atteinte...")
                self.strike(target)
        except ValueError:
            print("Il faut encoder un nombre...\n")
            self.strike(target)