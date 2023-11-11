# UofT - University of Toronto
# Course - Learn to Program: Crafting Quality Code
# Student: Ariel Ladislau Reises
# Github: github.com/arielreises

# Revision 1: carried out after feedback from Robert Minkler


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

    # New tests, suggested by Robert Minkler
    
    def test_swap_k_zero(self):
        # Test with k equal to 0.
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 0)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

    def test_swap_k_half_length(self):
        # Test with k equal to half the length of the list.
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 3)
        self.assertEqual(nums, [4, 5, 6, 1, 2, 3])

    def test_swap_k_large_k(self):
        # Test with k larger than the length of the list.
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 10)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

    def test_swap_k_empty_list(self):
        # Test with an empty list.
        nums = []
        a1.swap_k(nums, 0)
        self.assertEqual(nums, [])
    
    def test_swap_k_large_list(self):
        # Test with a large list.
        nums = list(range(1, 1001))
        a1.swap_k(nums, 5)
        self.assertEqual(nums, list(range(996, 1001)) + list(range(1, 996)))

if __name__ == '__main__':
    unittest.main(exit=False)
