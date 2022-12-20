from player import Player
from leaderboard import Leaderboard


class BattleshipsPVP:
    """La classe 'BattleshipsPVP permet de gérer la partie en mode PVP'"""

    def __init__(self):
        start = input("Commencer une partie? (choisir o ou n) -----> ")
        if start in ["o", "O"]:
            self.playPVP()
        else:
            print("Avorté...")


    def playPVP(self):
        p1name = input("Joueur 1, encode ton nom ! -----> ").capitalize()
        p1 = Player(p1name)
        p1.set_fleet()
        p1.view_console()
        self.clear_screen()

        p2name = input("\n\nJoueur 2, encode ton nom ! -----> ").capitalize()
        p2 = Player(p2name)
        p2.set_fleet()
        p2.view_console()
        self.clear_screen()

        flag = True
        while flag is True:
            p1.strike(p2)
            if self.fleet_sunk(p2) is True:
                new_player_score = Leaderboard(p1name, p1.score)
                new_player_score.update_score()
                self.victory_message(p1, p2)
                flag = False
            else:
                p2.strike(p1)
                if self.fleet_sunk(p1) is True:
                    new_player_score = Leaderboard(p2name, p2.score)
                    new_player_score.update_score()
                    self.victory_message(p2, p1)
                    flag = False
                else:
                    self.clear_screen()
        print("\nMerci d'avoir joué !")

        # Function checks remaining ship counters on a player's board

    def fleet_sunk(self, player):
        ship_counters = 0
        """Traverse la grille à la recherche des S"""
        for row in range(len(player.ocean.ocean)):
            for col in range(len(player.ocean.ocean)):
                if player.ocean.ocean[row][col] == "S":
                    ship_counters += 1
        if ship_counters == 0:
            return True
        else:
            return False

    def clear_screen(self):
        ("\n Prochain tour ? \n")

    def victory_message(self, winner, loser):
        print("\n\n\n*****************************************")
        print(f"La flotte de {loser.name} a été détruite, le vainqueur est {winner.name} !")
        print("*****************************************")
        print(f"{winner.name}, ton score est de : {winner.score}")
