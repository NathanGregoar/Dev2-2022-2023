from pathlib import Path
import json
from operator import itemgetter


with open(Path("tableau_scores.json"), "r") as f:
    liste_joueur = list(json.load(f))


class Tableau_scores:
    """La classe 'Tableau_scores' contient les informations sur le tableau des scores
     et sur les scores des différents joueurs"""

    def afficher_leaderboard():
        """Affiche le classement des joueurs en fonction de leur meilleur score"""

        liste_joueur.sort(key=itemgetter('meilleur_score'), reverse=True)
        print("------------------LEADERBOARD--------------------")
        for joueur in range(len(liste_joueur)):
            print(f"{joueur + 1}) {liste_joueur[joueur]['nom']} : {liste_joueur[joueur]['meilleur_score']} ")

    def __init__(self, nom : str, score: int):
        """
                Initie la classe Tableau_scores avec le nom et le score du joueur.

                PRE : nom est une chaîne de caractères valide et score est un entier valide
                POST : la classe Tableau_scores est initialisée avec les variables nom et score
        """

        self.nom = nom
        self.score = score

    # Met à jour le score si le joueur est déjà encoder, le crée dans le cas contraire

    def Maj_score(self):
        """
                Met à jour le score d'un joueur s'il existe déjà, le crée sinon

                PRE : self est une instance de Tableau_scores
                POST : le score du joueur est mis à jour ou créé dans le fichier json
        """

        a_un_score = False

        for joueur in liste_joueur:
            if joueur["nom"] != self.nom:
                continue
            elif joueur["nom"] == self.nom:
                a_un_score = True

            if joueur["nom"] == self.nom and joueur["meilleur_score"] < self.score:
                joueur["meilleur_score"] = self.score
                with open(Path("tableau_scores.json"), "w") as f:
                    json.dump(liste_joueur, f, indent=4)

        if not a_un_score:
            nouveau_joueur = dict()
            nouveau_joueur["nom"] = self.nom
            nouveau_joueur["meilleur_score"] = self.score
            liste_joueur.append(nouveau_joueur)
            with open(Path("tableau_scores.json"), "w") as f:
                json.dump(liste_joueur, f, indent=4)


