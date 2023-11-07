import a1
import unittest

class TestSwapK(unittest.TestCase):
    # Test class for function a1.swap_k.

    def test_swap_k_even_length(self):
        # Test with an even-length list.
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [5, 6, 3, 4, 1, 2])

    def test_swap_k_odd_length(self):
        # Test with an odd-length list.
        nums = [1, 2, 3, 4, 5]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [4, 5, 3, 1, 2])

    def test_swap_k_full_swap(self):
        # Test with a full swap of the list.
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 3)
        self.assertEqual(nums, [4, 5, 6, 1, 2, 3])

if __name__ == '__main__':
    unittest.main(exit=False)
