import unittest
from unittest.mock import patch, Mock

from tableau_de_jeu import TableauDeJeu
from joueur import Joueur
from radar import Radar
from bateau import Bateau


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Joueur('player1')

    def test_init(self):
        self.assertIsInstance(self.player.tableau, TableauDeJeu)
        self.assertIsInstance(self.player.radar, Radar)
        self.assertEqual(self.player.nom, 'player1')
        self.assertEqual(self.player.flotte, [])
        self.assertEqual(self.player.score, 0)

    def test_set_fleet(self):
        # Créez un mock de l'objet Ship
        ship_mock = Mock(spec=Bateau)

        # Utilisez le mock pour remplacer l'objet Ship dans la flotte du joueur
        self.player.fleet = [ship_mock]

        self.assertIsNotNone(self.player.fleet)
        self.assertIsInstance(self.player.fleet[0], Bateau)

    def test_view_console(self):
        self.assertIsNone(self.player.afficher_console())

    def test_register_hit(self):
        self.player.enregistrer_tir(0, 0)
        self.assertIsNotNone(self.player.flotte)


if __name__ == "__main__":
    unittest.main()
