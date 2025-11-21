"""Tests for the quicksort demonstration script."""

import unittest

from quicksort import quicksort


class TestQuicksort(unittest.TestCase):
    """Unit tests for the quicksort() helper."""

    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])

    def test_single_element(self):
        self.assertEqual(quicksort([42]), [42])

    def test_already_sorted(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_with_duplicates(self):
        self.assertEqual(quicksort([4, 1, 3, 1, 4]), [1, 1, 3, 4, 4])

    def test_with_negative_numbers(self):
        self.assertEqual(quicksort([3, -1, 0, -5, 8]), [-5, -1, 0, 3, 8])

    def test_input_not_mutated(self):
        numbers = [3, 1, 2]
        snapshot = numbers.copy()
        result = quicksort(numbers)
        self.assertEqual(numbers, snapshot)
        self.assertEqual(result, [1, 2, 3])

    def test_accepts_non_list_sequences(self):
        numbers = (9, 2, 7)
        self.assertEqual(quicksort(numbers), [2, 7, 9])


if __name__ == "__main__":
    unittest.main()
