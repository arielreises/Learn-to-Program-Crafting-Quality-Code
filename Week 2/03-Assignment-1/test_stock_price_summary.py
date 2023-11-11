# UofT - University of Toronto
# Course - Learn to Program: Crafting Quality Code
# Student: Ariel Ladislau Reises
# Github: github.com/arielreises

# Revision 1: carried out after feedback from Robert Minkler

import a1
import unittest

class TestStockPriceSummary(unittest.TestCase):
    # Test class for function a1.stock_price_summary.

    def test_price_changes_empty(self):
        # Test with an empty list of price changes.
        self.assertEqual(a1.stock_price_summary([]), (0, 0))

    def test_price_changes_mixed(self):
        # Test with mixed positive and negative price changes.
        self.assertEqual(a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]), (0.14, -0.17))

    def test_price_changes_all_gains(self):
        # Test with all positive price changes.
        self.assertEqual(a1.stock_price_summary([0.02, 0.05, 0.1]), (0.17, 0))

    # New tests, suggested by Robert Minkler
    
    def test_price_changes_empty(self):
        # Test with an empty list of price changes.
        self.assertEqual(a1.stock_price_summary([]), (0, 0))

    def test_price_changes_one_element(self):
        # Test with a list containing only one element.
        self.assertEqual(a1.stock_price_summary([0.05]), (0.05, 0))

    def test_price_changes_all_losses(self):
        # Test with a list containing only negative values.
        self.assertEqual(a1.stock_price_summary([-0.02, -0.1, -0.05]), (0, -0.17))

    def test_price_changes_large_gains(self):
        # Test with a list containing large positive values.
        self.assertEqual(a1.stock_price_summary([100, 200, 300]), (600, 0))

    def test_price_changes_large_losses(self):
        # Test with a list containing large negative values.
        self.assertEqual(a1.stock_price_summary([-100, -200, -300]), (0, -600))

if __name__ == '__main__':
    unittest.main(exit=False)
