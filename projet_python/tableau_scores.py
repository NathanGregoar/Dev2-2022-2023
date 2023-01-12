from pathlib import Path
import json
from operator import itemgetter


with open(Path("tableau_scores.json"), "r") as f:
    liste_joueur = list(json.load(f))


class Tableau_scores:
    """La classe 'Tableau_scores' contient les informations sur le tableau des scores
     et sur les scores des différents joueurs"""

    def afficher_leaderboard():
        liste_joueur.sort(key=itemgetter('best_score'), reverse=True)
        print("------------------LEADERBOARD--------------------")
        for joueur in range(len(liste_joueur)):
            print(f"{joueur + 1}) {liste_joueur[joueur]['name']} : {liste_joueur[joueur]['best_score']} ")

    def __init__(self, nom, score: int):
        self.nom = nom
        self.score = score

    # Met à jour le score si le joueur est déjà encoder, le crée dans le cas contraire

    def Maj_score(self):
        a_un_score = False

        for joueur in liste_joueur:
            if joueur["name"] != self.nom:
                continue
            elif joueur["name"] == self.nom:
                a_un_score = True

            if joueur["name"] == self.nom and joueur["best_score"] < self.score:
                joueur["best_score"] = self.score
                with open(Path("tableau_scores.json"), "w") as f:
                    json.dump(liste_joueur, f, indent=4)

        if not a_un_score:
            nouveau_joueur = dict()
            nouveau_joueur["name"] = self.nom
            nouveau_joueur["best_score"] = self.score
            liste_joueur.append(nouveau_joueur)
            with open(Path("tableau_scores.json"), "w") as f:
                json.dump(liste_joueur, f, indent=4)


