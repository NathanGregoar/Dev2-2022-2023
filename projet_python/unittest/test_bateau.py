import unittest
from bateau import Bateau


class TestShipMethods(unittest.TestCase):
    def setUp(self):
        self.ship = Bateau("Destroyer", 3)

    def test_init(self):
        self.assertEqual(self.ship.classe_bateau, "Destroyer")
        self.assertEqual(self.ship.taille, 3)
        self.assertEqual(self.ship.coords, [])

    def test_plot_vertical(self):
        self.ship.placer_verticalement(0, 0)
        self.assertEqual(self.ship.coords, [(0, 0), (1, 0), (2, 0)])

    def test_plot_horizontal(self):
        self.ship.placer_horizontalement(0, 0)
        self.assertEqual(self.ship.coords, [(0, 0), (0, 1), (0, 2)])

    def test_check_status(self):
        self.assertTrue(self.ship.check_etat_bateau())
        self.ship.coords = [(0, 0), (1, 0), (2, 0)]
        self.assertFalse(self.ship.check_etat_bateau())


if __name__ == "__main__":
    unittest.main()
