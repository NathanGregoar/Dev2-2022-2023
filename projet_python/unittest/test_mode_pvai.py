import unittest
from mode_pvai import mode_PVAI
from joueur import Joueur
from ia import IA


class Testmode_PVAI(unittest.TestCase):

    def test_init(self):
        game = mode_PVAI()
        self.assertIsInstance(game, mode_PVAI)

    def test_jouerPVAI(self):
        partie = mode_PVAI()
        partie.jouer_PVAI()
        self.assertIsInstance(partie.p, Joueur)
        self.assertIsInstance(partie.c, IA)
        self.assertEqual(partie.flag, False)


if __name__ == '__main__':
    unittest.main()
