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

if __name__ == '__main__':
    unittest.main(exit=False)
