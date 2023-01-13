import unittest
from joueur import Joueur
from mode_pvp import Mode_PVP


class TestModePVP(unittest.TestCase):

    def test_flotte_coulee(self):
        mode_pvp = Mode_PVP()
        joueur = Joueur("Test")
        joueur.tableau.tableau = [["S", "S", "S"], ["S", "S", "S"], ["S", "S", "S"]]
        self.assertEqual(mode_pvp.flotte_coulee(joueur), False)
        joueur.tableau.tableau = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
        self.assertEqual(mode_pvp.flotte_coulee(joueur), True)

    def test_prochain_tour(self):
        mode_pvp = Mode_PVP()
        self.assertEqual(mode_pvp.prochain_tour(), "\n Prochain tour ? \n")

    def test_message_victoire(self):
        mode_pvp = Mode_PVP()
        joueur1 = Joueur("Joueur 1")
        joueur1.score = 10
        joueur2 = Joueur("Joueur 2")
        self.assertEqual(mode_pvp.message_victoire(joueur1, joueur2),
        "\n\n\n*****************************************\nLa flotte de Joueur 2 a été détruite, le vainqueur est Joueur 1 !\n*****************************************\nJoueur 1, ton score est de : 10")

    def test_PVP(self):
        mode_pvp = Mode_PVP()
        mode_pvp.PVP()
        self.assertEqual(mode_pvp.PVP(), None)

    def test_init(self):
        mode_pvp = Mode_PVP()
        self.assertEqual(mode_pvp.__init__(), None)


if __name__ == '__main__':
    unittest.main()
