from tableu_de_jeu import Tableu_de_jeu
from radar import Radar
from bateau import Bateau

class Joueur:
    """La classe 'Player' gère les données et les actions des différents joueurs lors de la partie"""

    bateaux = {"Porte-avion": 5, "Croiseur": 4, "Destroyer": 3, "Frégate": 2}

    def __init__(self, nom):
        self.tableau = Tableu_de_jeu()
        self.radar = Radar()
        self.nom = nom
        self.flotte = []
        self.score = 64

    """Cette méthode utilise les input des joueurs pour placer les bateaux
    pour chaque bateau, un objet ship contenant les coordonnées des bateaux est ajouté au tableau de jeu"""

    def positionner_flotte(self):
        print("**********NOTE**************")
        input("Il faut encoder des chiffres entre 0 et 9 pour choisir les rangées et les colonnes sur le plateu de jeu")
        input("Les bateaux se place de gauche à droite et de haut en bas")
        print("****************************")
        for bateau, taille in self.bateaux.items():

            flag = True
            while flag:
                self.afficher_console()
                try:
                    print(f"Placer le {bateau}")
                    rangee = int(input("Quelle rangée ? "))
                    colonne = int(input("Quelle colonne ? "))
                    orientation = str(input("Voulez-vous le placer à la verticale ou à l'horizontale ? (choisir v ou h) "))

                    if orientation in ["v", "V"]:
                        if self.tableau.position_rangee_valide(rangee, colonne, taille):
                            self.tableau.def_rang_bateau(rangee, colonne, taille)
                            navire = Bateau(bateau, taille)
                            navire.placer_verticalement(rangee, colonne)
                            self.flotte.append(navire)
                            flag = False
                        else:
                            input("Les bateaux se croisent, placer-le autre part")

                    elif orientation in ["h", "H"]:
                        if self.tableau.position_colonne_valide(rangee, colonne, taille):
                            self.tableau.def_col_bateau(rangee, colonne, taille)
                            navire = Bateau(bateau, taille)
                            navire.placer_horizontalement(rangee, colonne)
                            self.flotte.append(navire)
                            flag = False
                        else:
                            input("Les bateaux se croisent, placer-le autre part")

                    else:
                        continue
                    self.afficher_console()

                except ValueError:
                    print("Vous avez oublié votre tête soldat ?\nIl faut écrire un chiffre..\n")

    # Cette méthode affiche le radar et l'océan d'une manière lisible

    def afficher_console(self):
        self.radar.afficher_radar()
        print("|                 |")
        self.tableau.voir_tableau()

    # Cette méthode vérifie le status des différents bateaux de la flotte du joueur

    def enregistrer_tir(self, rangee, colonne):
        for navire in self.flotte:
            if (rangee, colonne) in navire.coords:
                navire.coords.remove((rangee, colonne))
                if navire.check_etat_bateau():
                    self.flotte.remove(navire)
                    print("COULÉ!!!")
                    print(f"Le {navire.classe_bateau} de l'ennemi {self.nom} a été coulé !")

    """L'interface du joueur pour gérer les tirs,
    cette méthode met à jour l'état des plateaux de jeu des joueurs"""

    def tir(self, cible):
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
                        print("Zone déjà touchée, vérifier votre radar !")
                        self.tir(cible)
                    elif self.radar.radar[row][col] == "X":
                        print("Zone déjà touchée, vérifier votre radar !")
                        self.tir(cible)
                    else:
                        print("Négatif...")
                        self.radar.radar[row][col] = "O"
                        self.score -= 1

            else:
                print("Coordonnées hors d'atteinte...")
                self.tir(cible)
        except ValueError:
            print("Il faut encoder un nombre...\n")
            self.tir(cible)