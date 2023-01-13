import unittest
from tableau_de_jeu import TableauDeJeu


class TestOceanMethods(unittest.TestCase):
    def setUp(self):
        self.TableauDeJeu = TableauDeJeu()

    def test_init(self):
        self.assertEqual(self.TableauDeJeu.tableau, [["~" for i in range(10)] for i in range(10)])

    def test_getitem(self):
        self.assertEqual(self.TableauDeJeu[(0, 0)], "~")

    def test_setitem(self):
        self.TableauDeJeu[(0, 0)] = "S"
        self.assertEqual(self.TableauDeJeu[(0, 0)], "S")

    def test_valid_col(self):
        self.assertTrue(self.TableauDeJeu.col_valide(0))
        self.assertFalse(self.TableauDeJeu.col_valide(10))

    def test_valid_row(self):
        self.assertTrue(self.TableauDeJeu.rang_valide(0))
        self.assertFalse(self.TableauDeJeu.rang_valide(10))

    def test_can_use_col(self):
        self.assertTrue(self.TableauDeJeu.position_colonne_valide(0, 0, 3))
        self.TableauDeJeu[(0, 0)] = "S"
        self.assertFalse(self.TableauDeJeu.position_colonne_valide(0, 0, 3))

    def test_can_use_row(self):
        self.assertTrue(self.TableauDeJeu.position_rangee_valide(0, 0, 3))
        self.TableauDeJeu[(0, 0)] = "S"
        self.assertFalse(self.TableauDeJeu.position_rangee_valide(0, 0, 3))

    def test_set_ship_col(self):
        self.TableauDeJeu.def_col_bateau(0, 0, 3)
        self.assertEqual(self.TableauDeJeu[(0, 0)], "S")
        self.assertEqual(self.TableauDeJeu[(0, 1)], "S")
        self.assertEqual(self.TableauDeJeu[(0, 2)], "S")

    def test_set_ship_row(self):
        self.TableauDeJeu.def_rang_bateau(0, 0, 3)
        self.assertEqual(self.TableauDeJeu[(0, 0)], "S")
        self.assertEqual(self.TableauDeJeu[(1, 0)], "S")
        self.assertEqual(self.TableauDeJeu[(2, 0)], "S")


if __name__ == "__main__":
    unittest.main()
