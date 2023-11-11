# UofT - University of Toronto
# Course - Learn to Program: Crafting Quality Code
# Student: Ariel Ladislau Reises
# Github: github.com/arielreises

# Revision 1: carried out after feedback from Robert Minkler

import a1
import unittest

class TestNumBuses(unittest.TestCase):
    # Test class for function a1.num_buses.

    def test_min_buses_exact(self):
        # Test with an exact multiple of bus capacity.
        self.assertEqual(a1.num_buses(100), 2)

    def test_min_buses_uneven(self):
        # Test with a number that requires extra bus capacity.
        self.assertEqual(a1.num_buses(103), 3)

    def test_min_buses_zero(self):
        # Test with zero people.
        self.assertEqual(a1.num_buses(0), 0)


    # New tests, suggested by Robert Minkler
    
    def test_large_number_not_multiple(self):
        # Test with a large number that is not a multiple of 50.
        self.assertEqual(a1.num_buses(175), 4)

    def test_small_number(self):
        # Test with a small number that is less than the bus capacity.
        self.assertEqual(a1.num_buses(30), 1)

    def test_large_number_exact_multiple(self):
        # Test with a large number that is exactly a multiple of 50.
        self.assertEqual(a1.num_buses(300), 6)

    def test_negative_number(self):
        # Test with negative numbers.
        self.assertEqual(a1.num_buses(-50), 0)

    def test_large_negative_number(self):
        # Test with a large negative number.
        self.assertEqual(a1.num_buses(-175), 0)

    def test_zero_capacity(self):
        # Test with zero capacity.
        self.assertEqual(a1.num_buses(100, 0), float('inf'))

if __name__ == '__main__':
    unittest.main(exit=False)
