from joueur import Joueur
from bateau import Bateau
import random


class IA(Joueur):
    """La classe 'Computer' hérite de la classe 'Player'. Elle stock les données de l'ordinateur
    et lui permet de faire des actions pour le mode PVC"""


    def __init__(self):
        super().__init__(self)
        self.nom = "Ordinateur"

    # Version automatisée de la méthode set_fleet de la classe Player

    def placer_flotte_IA(self):
        positions = ["v", "h"]

        for bateau, taille in self.bateaux.items():

            flag = True
            while flag:
                rangee = random.randint(0, 9)
                colonne = random.randint(0, 9)
                orientation = random.choice(positions)

                if orientation == "v":
                    if self.tableau.position_rangee_valide(rangee, colonne, taille):
                        self.tableau.def_rang_bateau(rangee, colonne, taille)
                        boat = Bateau(bateau, taille)
                        boat.placer_verticalement(rangee, colonne)
                        self.flotte.append(boat)
                        flag = False

                    else:
                        rangee = rangee + 2

                elif orientation == "h":
                    if self.tableau.position_colonne_valide(rangee, colonne, taille):
                        self.tableau.def_col_bateau(rangee, colonne, taille)
                        boat = Bateau(bateau, taille)
                        boat.placer_horizontalement(rangee, colonne)
                        self.flotte.append(boat)
                        flag = False

                    else:
                        colonne = colonne + 2

                else:
                    continue

                # Méthode automatisée pour gérer les tirs

    def tir_IA(self, cible):
        rangee = random.randint(0, 9)
        colonne = random.randint(0, 9)

        if self.radar.radar[rangee][colonne] == ".":
            input(f"...Recherche de la Cible....")
            input(f"Tir sur cible en ({rangee}, {colonne})")

            if cible.tableau.tableau[rangee][colonne] == "S":
                print("TOUCHÉ!!!")
                cible.tableau.tableau[rangee][colonne] = "X"
                cible.enregistrer_tir(rangee, colonne)
                self.radar.radar[rangee][colonne] = "X"

            else:
                print("Raté....recalibrage")
                self.radar.radar[rangee][colonne] = "O"

        else:
            self.tir_IA(cible)