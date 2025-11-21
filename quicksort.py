"""
Quicksort Algorithm Implementation

This module provides an efficient implementation of the quicksort algorithm,
a divide-and-conquer sorting algorithm with average time complexity O(n log n).
"""


def quicksort(arr):
    """
    Sort a list using the quicksort algorithm.

    Quicksort works by selecting a 'pivot' element and partitioning the array
    into elements less than the pivot and elements greater than the pivot,
    then recursively sorting the partitions.

    Args:
        arr (list): The list to be sorted. Can contain integers, floats,
                   or any comparable elements.

    Returns:
        list: A new sorted list in ascending order.

    Examples:
        >>> quicksort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
        >>> quicksort([])
        []
        >>> quicksort([5])
        [5]

    Time Complexity:
        - Average case: O(n log n)
        - Worst case: O(n^2) - occurs when pivot is always smallest/largest
        - Best case: O(n log n)

    Space Complexity:
        O(n) - creates new lists for partitions
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choose the middle element as pivot to handle sorted/reverse sorted cases better
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    # Partition the array into three parts:
    # - left: elements less than pivot
    # - middle: elements equal to pivot (handles duplicates)
    # - right: elements greater than pivot
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

    # Recursively sort left and right partitions, combine with middle
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    Sort a list in-place using the quicksort algorithm.

    This is a more memory-efficient version that sorts the array in-place
    rather than creating new lists.

    Args:
        arr (list): The list to be sorted in-place.
        low (int): Starting index of the partition to sort (default: 0).
        high (int): Ending index of the partition to sort (default: len(arr)-1).

    Returns:
        None: The list is sorted in-place.

    Examples:
        >>> arr = [3, 6, 8, 10, 1, 2, 1]
        >>> quicksort_inplace(arr)
        >>> arr
        [1, 1, 2, 3, 6, 8, 10]
    """
    # Initialize high on first call
    if high is None:
        high = len(arr) - 1

    # Base case: partition has 1 or fewer elements
    if low >= high:
        return

    # Partition the array and get the pivot index
    pivot_index = _partition(arr, low, high)

    # Recursively sort elements before and after partition
    quicksort_inplace(arr, low, pivot_index - 1)
    quicksort_inplace(arr, pivot_index + 1, high)


def _partition(arr, low, high):
    """
    Partition helper function for in-place quicksort.

    Rearranges elements so that elements less than the pivot are on the left,
    and elements greater than the pivot are on the right.

    Args:
        arr (list): The list to partition.
        low (int): Starting index of the partition.
        high (int): Ending index of the partition.

    Returns:
        int: The final index of the pivot element.
    """
    # Choose middle element as pivot
    mid = (low + high) // 2
    pivot = arr[mid]

    # Move pivot to end temporarily
    arr[mid], arr[high] = arr[high], arr[mid]

    # Partition index tracks where to place next small element
    partition_index = low

    # Move all elements smaller than pivot to the left
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1

    # Move pivot to its final position
    arr[partition_index], arr[high] = arr[high], arr[partition_index]

    return partition_index


if __name__ == "__main__":
    # Demo usage
    import random

    print("Quicksort Algorithm Demo\n" + "=" * 50)

    # Example 1: Random list
    test_list = [3, 6, 8, 10, 1, 2, 1]
    print(f"\nOriginal list: {test_list}")
    print(f"Sorted list:   {quicksort(test_list)}")

    # Example 2: Already sorted
    sorted_list = [1, 2, 3, 4, 5]
    print(f"\nAlready sorted: {sorted_list}")
    print(f"Result:         {quicksort(sorted_list)}")

    # Example 3: Reverse sorted
    reverse_list = [5, 4, 3, 2, 1]
    print(f"\nReverse sorted: {reverse_list}")
    print(f"Result:         {quicksort(reverse_list)}")

    # Example 4: Duplicates
    dup_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"\nWith duplicates: {dup_list}")
    print(f"Result:          {quicksort(dup_list)}")

    # Example 5: Large random list
    large_list = [random.randint(1, 100) for _ in range(20)]
    print(f"\nLarge random list: {large_list}")
    print(f"Sorted:            {quicksort(large_list)}")

    # Example 6: In-place sorting
    inplace_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nIn-place sorting: {inplace_list}")
    quicksort_inplace(inplace_list)
    print(f"Result:           {inplace_list}")
