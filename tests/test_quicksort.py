import unittest

from quicksort import quicksort


class QuickSortTests(unittest.TestCase):
    def test_handles_varied_inputs(self) -> None:
        cases = [
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 1, 3, 3, 2], [1, 2, 3, 3, 5]),
            ([-5, 4, 0, -1], [-5, -1, 0, 4]),
        ]

        for values, expected in cases:
            with self.subTest(values=values):
                self.assertEqual(quicksort(values), expected)

    def test_does_not_mutate_original_list(self) -> None:
        data = [3, 1, 2]
        snapshot = list(data)

        result = quicksort(data)

        self.assertEqual(data, snapshot)
        self.assertEqual(result, [1, 2, 3])
        self.assertIsNot(result, data)

    def test_accepts_sequences_not_just_lists(self) -> None:
        data = (4, 2, 5, 1, 3)

        self.assertEqual(quicksort(data), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
