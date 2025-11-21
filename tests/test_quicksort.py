import unittest

from quicksort import quicksort


class QuicksortTests(unittest.TestCase):
    def test_empty_list(self):
        values = []
        result = quicksort(values)
        self.assertEqual(result, [])
        self.assertEqual(values, [])

    def test_single_element(self):
        values = [42]
        result = quicksort(values)
        self.assertEqual(result, [42])
        self.assertEqual(values, [42])

    def test_duplicates(self):
        values = [5, 1, 3, 1, 5, 2, 2]
        result = quicksort(values)
        self.assertEqual(result, [1, 1, 2, 2, 3, 5, 5])
        self.assertEqual(values, [1, 1, 2, 2, 3, 5, 5])

    def test_already_sorted(self):
        values = [1, 2, 3, 4, 5]
        result = quicksort(values)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(values, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        values = [5, 4, 3, 2, 1]
        result = quicksort(values)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(values, [1, 2, 3, 4, 5])

    def test_unsorted_random_values(self):
        values = [12, 3, 7, 1, 9, 8, 2]
        result = quicksort(values)
        self.assertEqual(result, [1, 2, 3, 7, 8, 9, 12])
        self.assertEqual(values, [1, 2, 3, 7, 8, 9, 12])


if __name__ == "__main__":
    unittest.main()
