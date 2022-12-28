from pathlib import Path
import json
from operator import itemgetter


with open(Path("leaderboard.json"), "r") as f:
    leader_list = list(json.load(f))


class Leaderboard:
    """La classe 'Leaderboard' contient les informations sur le tableau des scores
     et sur les scores des différents joueurs"""

    def print_leaderboard():
        leader_list.sort(key=itemgetter('best_score'), reverse=True)
        print("------------------LEADERBOARD--------------------")
        for player in range(len(leader_list)):
            print(f"{player + 1}) {leader_list[player]['name']} : {leader_list[player]['best_score']} ")

    def __init__(self, name, score: int):
        self.name = name
        self.score = score

    # Met à jour le score si le joueur est déjà encoder, le crée dans le cas contraire

    def update_score(self):
        is_in_leader_list = False

        for player in leader_list:
            if player["name"] != self.name:
                continue
            elif player["name"] == self.name:
                is_in_leader_list = True

            if player["name"] == self.name and player["best_score"] < self.score:
                player["best_score"] = self.score
                with open(Path("leaderboard.json"), "w") as f:
                    json.dump(leader_list, f, indent=4)

        if not is_in_leader_list:
            new_player = dict()
            new_player["name"] = self.name
            new_player["best_score"] = self.score
            leader_list.append(new_player)
            with open(Path("leaderboard.json"), "w") as f:
                json.dump(leader_list, f, indent=4)


