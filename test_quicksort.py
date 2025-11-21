"""
Comprehensive test suite for quicksort algorithm implementation.

Tests both the standard quicksort and in-place quicksort implementations
across various edge cases and scenarios.
"""

import unittest
import random
from quicksort import quicksort, quicksort_inplace


class TestQuicksort(unittest.TestCase):
    """Test cases for the standard quicksort function."""

    def test_empty_list(self):
        """Test that quicksort handles empty lists correctly."""
        self.assertEqual(quicksort([]), [])

    def test_single_element(self):
        """Test that quicksort handles single-element lists."""
        self.assertEqual(quicksort([1]), [1])
        self.assertEqual(quicksort([42]), [42])
        self.assertEqual(quicksort([-5]), [-5])

    def test_two_elements_sorted(self):
        """Test sorting two elements that are already sorted."""
        self.assertEqual(quicksort([1, 2]), [1, 2])

    def test_two_elements_unsorted(self):
        """Test sorting two elements that need to be swapped."""
        self.assertEqual(quicksort([2, 1]), [1, 2])

    def test_multiple_elements(self):
        """Test sorting a list with multiple elements."""
        self.assertEqual(quicksort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])

    def test_already_sorted(self):
        """Test that quicksort handles already sorted lists efficiently."""
        sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(quicksort(sorted_list), sorted_list)

    def test_reverse_sorted(self):
        """Test sorting a list that is sorted in reverse order."""
        reverse_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(quicksort(reverse_list), expected)

    def test_all_duplicates(self):
        """Test sorting a list where all elements are identical."""
        self.assertEqual(quicksort([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])

    def test_some_duplicates(self):
        """Test sorting a list with some duplicate values."""
        self.assertEqual(quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_negative_numbers(self):
        """Test sorting lists containing negative numbers."""
        self.assertEqual(quicksort([-5, -1, -3, 0, 2]), [-5, -3, -1, 0, 2])
        self.assertEqual(quicksort([-10, 5, -3, 8, -1]), [-10, -3, -1, 5, 8])

    def test_mixed_positive_negative(self):
        """Test sorting lists with both positive and negative numbers."""
        self.assertEqual(quicksort([3, -1, 4, -5, 2, 0]), [-5, -1, 0, 2, 3, 4])

    def test_floating_point_numbers(self):
        """Test sorting lists with floating point numbers."""
        result = quicksort([3.5, 1.2, 4.8, 2.1, 0.5])
        expected = [0.5, 1.2, 2.1, 3.5, 4.8]
        self.assertEqual(result, expected)

    def test_large_list(self):
        """Test sorting a large list of random numbers."""
        large_list = [random.randint(-100, 100) for _ in range(100)]
        result = quicksort(large_list)
        expected = sorted(large_list)
        self.assertEqual(result, expected)

    def test_original_list_unchanged(self):
        """Test that the original list is not modified (immutability)."""
        original = [3, 1, 4, 1, 5, 9, 2, 6]
        original_copy = original.copy()
        quicksort(original)
        self.assertEqual(original, original_copy)

    def test_strings(self):
        """Test sorting lists of strings."""
        self.assertEqual(quicksort(['dog', 'cat', 'elephant', 'ant']),
                        ['ant', 'cat', 'dog', 'elephant'])


class TestQuicksortInplace(unittest.TestCase):
    """Test cases for the in-place quicksort function."""

    def test_empty_list(self):
        """Test that in-place quicksort handles empty lists correctly."""
        arr = []
        quicksort_inplace(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        """Test that in-place quicksort handles single-element lists."""
        arr = [1]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1])

    def test_two_elements_sorted(self):
        """Test in-place sorting of two elements that are already sorted."""
        arr = [1, 2]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2])

    def test_two_elements_unsorted(self):
        """Test in-place sorting of two elements that need to be swapped."""
        arr = [2, 1]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2])

    def test_multiple_elements(self):
        """Test in-place sorting of a list with multiple elements."""
        arr = [3, 6, 8, 10, 1, 2, 1]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 6, 8, 10])

    def test_already_sorted(self):
        """Test that in-place quicksort handles already sorted lists."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = arr.copy()
        quicksort_inplace(arr)
        self.assertEqual(arr, expected)

    def test_reverse_sorted(self):
        """Test in-place sorting of a reverse sorted list."""
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_all_duplicates(self):
        """Test in-place sorting where all elements are identical."""
        arr = [5, 5, 5, 5, 5]
        quicksort_inplace(arr)
        self.assertEqual(arr, [5, 5, 5, 5, 5])

    def test_some_duplicates(self):
        """Test in-place sorting with some duplicate values."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_negative_numbers(self):
        """Test in-place sorting with negative numbers."""
        arr = [-5, -1, -3, 0, 2]
        quicksort_inplace(arr)
        self.assertEqual(arr, [-5, -3, -1, 0, 2])

    def test_large_list(self):
        """Test in-place sorting of a large random list."""
        arr = [random.randint(-100, 100) for _ in range(100)]
        expected = sorted(arr)
        quicksort_inplace(arr)
        self.assertEqual(arr, expected)

    def test_list_is_modified_inplace(self):
        """Verify that the function modifies the list in-place."""
        arr = [3, 1, 4, 1, 5]
        original_id = id(arr)
        quicksort_inplace(arr)
        # Verify it's the same list object
        self.assertEqual(id(arr), original_id)
        # Verify it's sorted
        self.assertEqual(arr, [1, 1, 3, 4, 5])


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios."""

    def test_very_large_values(self):
        """Test sorting with very large integer values."""
        arr = [10**9, -10**9, 10**8, -10**8, 0]
        result = quicksort(arr)
        self.assertEqual(result, [-10**9, -10**8, 0, 10**8, 10**9])

    def test_many_duplicates_scattered(self):
        """Test with many duplicates scattered throughout."""
        arr = [5, 1, 5, 2, 5, 3, 5, 4, 5]
        result = quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 5, 5, 5, 5])

    def test_alternating_pattern(self):
        """Test with alternating high-low pattern."""
        arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
        result = quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_consistency_between_implementations(self):
        """Verify both implementations produce the same results."""
        test_cases = [
            [3, 6, 8, 10, 1, 2, 1],
            [5, 4, 3, 2, 1],
            [1, 1, 1, 1],
            [-5, 3, -1, 0, 8],
            []
        ]

        for test_case in test_cases:
            # Test standard implementation
            result1 = quicksort(test_case.copy())

            # Test in-place implementation
            arr = test_case.copy()
            quicksort_inplace(arr)
            result2 = arr

            # Both should produce the same sorted result
            self.assertEqual(result1, result2,
                           f"Implementations differ for input: {test_case}")


class TestRandomizedData(unittest.TestCase):
    """Test with multiple random datasets to ensure robustness."""

    def test_random_integers_small(self):
        """Test with small random integers."""
        for _ in range(10):
            arr = [random.randint(0, 50) for _ in range(20)]
            result = quicksort(arr)
            expected = sorted(arr)
            self.assertEqual(result, expected)

    def test_random_integers_large_range(self):
        """Test with integers from a large range."""
        for _ in range(5):
            arr = [random.randint(-1000, 1000) for _ in range(50)]
            result = quicksort(arr)
            expected = sorted(arr)
            self.assertEqual(result, expected)

    def test_inplace_random_consistency(self):
        """Test in-place sorting with random data matches expected results."""
        for _ in range(10):
            arr = [random.randint(-100, 100) for _ in range(30)]
            expected = sorted(arr)
            quicksort_inplace(arr)
            self.assertEqual(arr, expected)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
