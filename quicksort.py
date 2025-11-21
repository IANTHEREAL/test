"""
Quicksort Algorithm Implementation

This module provides a clean implementation of the quicksort algorithm,
a divide-and-conquer sorting algorithm with O(n log n) average time complexity.
"""


def quicksort(arr):
    """
    Sort a list using the quicksort algorithm.

    Quicksort works by:
    1. Selecting a 'pivot' element from the array
    2. Partitioning other elements into two sub-arrays:
       - Elements less than the pivot
       - Elements greater than the pivot
    3. Recursively sorting the sub-arrays

    Args:
        arr (list): The list to be sorted. Can contain any comparable elements.

    Returns:
        list: A new sorted list containing all elements from the input.

    Time Complexity:
        - Best/Average: O(n log n)
        - Worst: O(n^2) when the pivot is always the smallest or largest element

    Space Complexity:
        O(n) due to creating new lists for partitioning

    Examples:
        >>> quicksort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
        >>> quicksort([])
        []
        >>> quicksort([1])
        [1]
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choose the middle element as pivot to handle sorted/reverse sorted cases better
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    # Partition the array into three parts:
    # - Elements less than pivot
    # - Elements equal to pivot (handles duplicates)
    # - Elements greater than pivot
    left = []
    middle = []
    right = []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            middle.append(element)
        else:
            right.append(element)

    # Recursively sort the left and right partitions and combine
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    Sort a list in-place using the quicksort algorithm.

    This is a more memory-efficient version that modifies the input array
    directly rather than creating new lists.

    Args:
        arr (list): The list to be sorted in-place.
        low (int): Starting index of the portion to sort (default: 0).
        high (int): Ending index of the portion to sort (default: len(arr) - 1).

    Returns:
        list: The same list, sorted in-place.

    Time Complexity:
        - Best/Average: O(n log n)
        - Worst: O(n^2)

    Space Complexity:
        O(log n) due to recursion stack

    Examples:
        >>> arr = [3, 6, 8, 10, 1, 2, 1]
        >>> quicksort_inplace(arr)
        [1, 1, 2, 3, 6, 8, 10]
    """
    # Initialize high on first call
    if high is None:
        high = len(arr) - 1

    # Base case: if the range has 1 or fewer elements, it's sorted
    if low < high:
        # Partition the array and get the pivot's final position
        pivot_index = _partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)

    return arr


def _partition(arr, low, high):
    """
    Partition the array around a pivot element.

    This helper function selects the last element as pivot and rearranges
    the array so that all elements smaller than the pivot come before it,
    and all elements greater come after it.

    Args:
        arr (list): The array to partition.
        low (int): Starting index of the range to partition.
        high (int): Ending index of the range to partition.

    Returns:
        int: The final position of the pivot element.
    """
    # Choose the last element as pivot
    pivot = arr[high]

    # Index of smaller element, indicates the position where we'll place the pivot
    i = low - 1

    # Move all elements smaller than pivot to the left
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


if __name__ == "__main__":
    # Demo usage
    print("Quicksort Demo")
    print("=" * 50)

    # Test with various input types
    test_cases = [
        [3, 6, 8, 10, 1, 2, 1],
        [5, 2, 8, 1, 9],
        [],
        [42],
        [3, 3, 3, 3],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]

    for i, arr in enumerate(test_cases, 1):
        original = arr.copy()
        sorted_arr = quicksort(arr)
        print(f"\nTest {i}:")
        print(f"  Original: {original}")
        print(f"  Sorted:   {sorted_arr}")
