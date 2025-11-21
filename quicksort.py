"""Educational in-place quicksort implementation with example usage.

The quicksort algorithm recursively partitions a list around a pivot so that
smaller values are placed to the left of the pivot and larger values to the
right. Average time complexity is O(n log n) with O(log n) auxiliary stack
space due to recursion; worst case is O(n^2) when the partitioning is highly
unbalanced.
"""

from __future__ import annotations


def quicksort(values: list[int]) -> list[int]:
    """Sort ``values`` in place using Lomuto partition quicksort.

    Args:
        values: Mutable sequence of integers to sort.

    Returns:
        The sorted list (the same reference as ``values`` for convenience).

    This function mutates the input list directly so the caller can either rely
    on the return value or simply inspect ``values`` after invocation.
    """

    if len(values) < 2:
        # Lists with zero or one element are already sorted.
        return values

    _quicksort(values, 0, len(values) - 1)
    return values


def _quicksort(values: list[int], low: int, high: int) -> None:
    """Recursively partition the array and sort the partitions in place."""

    if low >= high:
        # When the region has one or zero elements there is nothing to sort.
        return

    pivot_index = _partition(values, low, high)

    # Recursively sort elements smaller than the pivot.
    _quicksort(values, low, pivot_index - 1)
    # Recursively sort elements greater than the pivot.
    _quicksort(values, pivot_index + 1, high)


def _partition(values: list[int], low: int, high: int) -> int:
    """Partition the list and return the pivot's final index.

    This implementation uses the Lomuto partition scheme: it selects the last
    element as the pivot and walks the range [low, high) swapping elements so
    that anything <= pivot is moved toward the front.
    """

    pivot = values[high]
    # ``store_index`` tracks where the next smaller-or-equal value belongs.
    store_index = low

    for current in range(low, high):
        if values[current] <= pivot:
            # Swap current value into the "smaller or equal" region.
            values[store_index], values[current] = values[current], values[store_index]
            store_index += 1

    # Move the pivot between the two partitions so it is in its final position.
    values[store_index], values[high] = values[high], values[store_index]
    return store_index


if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    print(f"Original: {sample}")
    quicksort(sample)
    print(f"Sorted:   {sample}")
