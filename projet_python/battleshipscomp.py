from battleshipspvp import BattleshipsPVP
from computer import Computer
from player import Player


class BattleshipsCOMP(BattleshipsPVP):
    """La classe 'BattlshipsCOMP' permet de gérer la partie contre l'ordinateur"""

    def __init__(self):
        start = input("Commencer une partie ? (o ou n) -----> ")
        if start in ["o", "O"]:
            self.playCOMP()
        else:
            print("Avorté...")

    def playCOMP(self):
        pname = input("Joueur 1, encode ton nom ! -----> ").capitalize()
        p = Player(pname)
        p.set_fleet()
        p.view_console()
        self.clear_screen()

        c = Computer()
        print("L'ordinateur place ses bateaux...")
        c.set_compu_fleet()
        self.clear_screen()

        flag = True
        while flag is True:
            p.strike(c)
            if self.fleet_sunk(c) is True:
                self.victory_message(p, c)
                flag = False
            else:
                self.clear_screen()

                c.compu_strike(p)
                if self.fleet_sunk(p) is True:
                    self.victory_message(c, p)
                    flag = False
                else:
                    self.clear_screen()
        print("\nMerci d'avoir joué!")