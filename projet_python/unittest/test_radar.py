import unittest
from radar import Radar


class TestRadar(unittest.TestCase):
    def test_init(self):
        radar = Radar()
        self.assertEqual(len(radar.radar), 10)
        self.assertEqual(len(radar.radar[0]), 10)

    def test_getitem(self):
        radar = Radar()
        self.assertEqual(radar[0, 0], ".")

    def test_setitem(self):
        radar = Radar()
        radar[0, 0] = "X"
        self.assertEqual(radar[0, 0], "X")

    def test_setitem_out_of_bounds(self):
        radar = Radar()
        with self.assertRaises(IndexError):
            radar[10, 10] = "X"


if __name__ == "__main__":
    unittest.main()
