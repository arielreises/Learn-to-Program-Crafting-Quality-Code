# UofT - University of Toronto
# Course - Learn to Program: Crafting Quality Code
# Student: Ariel Ladislau Reises
# Github: github.com/arielreises

import a1
import unittest

class TestNumBuses(unittest.TestCase):
    # Test class for function a1.num_buses. """

    def test_min_buses_exact(self):
        # Test with an exact multiple of bus capacity. """
        self.assertEqual(a1.num_buses(100), 2)

    def test_min_buses_uneven(self):
        # Test with a number that requires extra bus capacity. """
        self.assertEqual(a1.num_buses(103), 3)

    def test_min_buses_zero(self):
        # Test with zero people. """
        self.assertEqual(a1.num_buses(0), 0)

if __name__ == '__main__':
    unittest.main(exit=False)
