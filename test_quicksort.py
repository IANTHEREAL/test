"""
Unit tests for quicksort implementation.

This module provides comprehensive test coverage for both the functional
and in-place quicksort implementations.
"""

import unittest
import random
from quicksort import quicksort, quicksort_inplace


class TestQuicksort(unittest.TestCase):
    """Test cases for the functional quicksort implementation."""

    def test_empty_list(self):
        """Test that an empty list returns an empty list."""
        self.assertEqual(quicksort([]), [])

    def test_single_element(self):
        """Test that a single-element list returns the same list."""
        self.assertEqual(quicksort([42]), [42])

    def test_two_elements_sorted(self):
        """Test sorting two elements that are already in order."""
        self.assertEqual(quicksort([1, 2]), [1, 2])

    def test_two_elements_unsorted(self):
        """Test sorting two elements that are out of order."""
        self.assertEqual(quicksort([2, 1]), [1, 2])

    def test_multiple_elements(self):
        """Test sorting a list with multiple elements."""
        self.assertEqual(quicksort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])

    def test_duplicates(self):
        """Test that duplicate elements are handled correctly."""
        self.assertEqual(quicksort([5, 2, 8, 2, 9, 1, 5]), [1, 2, 2, 5, 5, 8, 9])

    def test_all_same_elements(self):
        """Test sorting a list where all elements are identical."""
        self.assertEqual(quicksort([7, 7, 7, 7, 7]), [7, 7, 7, 7, 7])

    def test_already_sorted(self):
        """Test that an already sorted list remains sorted."""
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Test sorting a list in reverse order."""
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        self.assertEqual(quicksort([-5, 3, -1, 0, 8, -3]), [-5, -3, -1, 0, 3, 8])

    def test_mixed_positive_negative(self):
        """Test sorting a list with both positive and negative numbers."""
        self.assertEqual(quicksort([10, -5, 3, -1, 0]), [-5, -1, 0, 3, 10])

    def test_large_numbers(self):
        """Test sorting a list with large numbers."""
        self.assertEqual(
            quicksort([1000000, 500, 999999, 1, 50000]),
            [1, 500, 50000, 999999, 1000000]
        )

    def test_floating_point(self):
        """Test sorting a list with floating-point numbers."""
        result = quicksort([3.14, 2.71, 1.41, 2.71, 0.5])
        expected = [0.5, 1.41, 2.71, 2.71, 3.14]
        self.assertEqual(result, expected)

    def test_random_data_small(self):
        """Test sorting a small random dataset."""
        random.seed(42)
        arr = [random.randint(1, 100) for _ in range(20)]
        result = quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)

    def test_random_data_medium(self):
        """Test sorting a medium random dataset."""
        random.seed(123)
        arr = [random.randint(-1000, 1000) for _ in range(100)]
        result = quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)

    def test_original_list_unchanged(self):
        """Test that the original list is not modified (functional style)."""
        original = [3, 1, 4, 1, 5, 9, 2, 6]
        original_copy = original.copy()
        quicksort(original)
        self.assertEqual(original, original_copy)

    def test_strings(self):
        """Test sorting a list of strings."""
        result = quicksort(['banana', 'apple', 'cherry', 'date'])
        expected = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(result, expected)


class TestQuicksortInplace(unittest.TestCase):
    """Test cases for the in-place quicksort implementation."""

    def test_empty_list(self):
        """Test that an empty list remains empty."""
        arr = []
        quicksort_inplace(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        """Test that a single-element list remains unchanged."""
        arr = [42]
        quicksort_inplace(arr)
        self.assertEqual(arr, [42])

    def test_two_elements_sorted(self):
        """Test sorting two elements that are already in order."""
        arr = [1, 2]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2])

    def test_two_elements_unsorted(self):
        """Test sorting two elements that are out of order."""
        arr = [2, 1]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2])

    def test_multiple_elements(self):
        """Test sorting a list with multiple elements."""
        arr = [3, 6, 8, 10, 1, 2, 1]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 6, 8, 10])

    def test_duplicates(self):
        """Test that duplicate elements are handled correctly."""
        arr = [5, 2, 8, 2, 9, 1, 5]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2, 2, 5, 5, 8, 9])

    def test_all_same_elements(self):
        """Test sorting a list where all elements are identical."""
        arr = [7, 7, 7, 7, 7]
        quicksort_inplace(arr)
        self.assertEqual(arr, [7, 7, 7, 7, 7])

    def test_already_sorted(self):
        """Test that an already sorted list remains sorted."""
        arr = [1, 2, 3, 4, 5]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Test sorting a list in reverse order."""
        arr = [5, 4, 3, 2, 1]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        arr = [-5, 3, -1, 0, 8, -3]
        quicksort_inplace(arr)
        self.assertEqual(arr, [-5, -3, -1, 0, 3, 8])

    def test_random_data_small(self):
        """Test sorting a small random dataset."""
        random.seed(42)
        arr = [random.randint(1, 100) for _ in range(20)]
        expected = sorted(arr)
        quicksort_inplace(arr)
        self.assertEqual(arr, expected)

    def test_random_data_large(self):
        """Test sorting a large random dataset."""
        random.seed(456)
        arr = [random.randint(-10000, 10000) for _ in range(1000)]
        expected = sorted(arr)
        quicksort_inplace(arr)
        self.assertEqual(arr, expected)

    def test_modifies_in_place(self):
        """Test that the array is modified in-place."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        arr_id = id(arr)
        result = quicksort_inplace(arr)
        # Check that the same object is returned
        self.assertEqual(id(result), arr_id)
        # Check that the array is sorted
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 6, 9])


class TestQuicksortComparison(unittest.TestCase):
    """Test cases comparing both implementations."""

    def test_both_produce_same_result(self):
        """Test that both implementations produce the same sorted output."""
        test_cases = [
            [],
            [1],
            [2, 1],
            [3, 6, 8, 10, 1, 2, 1],
            [5, 5, 5, 5],
            list(range(10, 0, -1)),
            [random.randint(-100, 100) for _ in range(50)]
        ]

        for arr in test_cases:
            arr_for_inplace = arr.copy()
            result_functional = quicksort(arr)
            result_inplace = quicksort_inplace(arr_for_inplace)
            self.assertEqual(result_functional, result_inplace,
                           f"Results differ for input: {arr}")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios."""

    def test_large_range_values(self):
        """Test with values spanning a large range."""
        arr = [1000000, 1, 500000, -1000000, 0]
        result = quicksort(arr)
        self.assertEqual(result, [-1000000, 0, 1, 500000, 1000000])

    def test_many_duplicates(self):
        """Test with many duplicate values."""
        arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        result = quicksort(arr)
        self.assertEqual(result, [1, 1, 1, 1, 1, 2, 2, 2, 2, 2])

    def test_alternating_values(self):
        """Test with alternating high and low values."""
        arr = [100, 1, 99, 2, 98, 3, 97, 4]
        result = quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 97, 98, 99, 100])

    def test_nearly_sorted(self):
        """Test with a nearly sorted list (one element out of place)."""
        arr = [1, 2, 3, 4, 10, 6, 7, 8, 9, 5]
        result = quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main(verbosity=2)
