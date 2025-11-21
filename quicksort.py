"""Educational quicksort implementation with detailed commentary.

This module exposes :func:`quicksort`, which sorts a mutable sequence in
place using the classic Lomuto partition scheme. The helper returns the same
list so it can be used fluently:

>>> numbers = [3, 1, 4, 1, 5]
>>> quicksort(numbers)
[1, 1, 3, 4, 5]
>>> numbers
[1, 1, 3, 4, 5]
"""

from __future__ import annotations

from typing import MutableSequence, TypeVar

T = TypeVar("T")


def quicksort(values: MutableSequence[T] | None) -> MutableSequence[T] | None:
    """Sort ``values`` in place using quicksort and return the same object.

    Args:
        values: A mutable sequence of comparable items to be reordered.

    Returns:
        The same sequence instance, now sorted. ``None`` inputs are returned
        unchanged to make the function easier to call conditionally.
    """

    if values is None:
        return None

    if len(values) < 2:
        # Lists with fewer than two elements are already sorted.
        return values

    _quicksort(values, 0, len(values) - 1)
    return values


def _quicksort(values: MutableSequence[T], low: int, high: int) -> None:
    """Recursively quicksort the inclusive ``[low, high]`` slice of ``values``.

    Splits the segment around a pivot and sorts the sub-slices independently.
    """

    if low >= high:
        # Base case: zero or one element in the slice means it is sorted.
        return

    # Partition the slice so the pivot lands in its final position.
    # Everything to the left of the pivot will be <= pivot, everything to the
    # right > pivot.
    pivot_index = _partition(values, low, high)

    # Recursively sort the left and right partitions created above.
    _quicksort(values, low, pivot_index - 1)
    _quicksort(values, pivot_index + 1, high)


def _partition(values: MutableSequence[T], low: int, high: int) -> int:
    """Partition ``values[low:high+1]`` using ``values[high]`` as the pivot."""

    pivot = values[high]

    # ``i`` tracks the boundary between elements <= pivot and elements > pivot.
    i = low - 1

    for j in range(low, high):
        # Whenever we find an element that belongs on the left (<= pivot)
        # we advance the boundary and swap the element into position.
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]

    # Finally, slide the pivot into the gap directly after the <= partition.
    values[i + 1], values[high] = values[high], values[i + 1]
    return i + 1


if __name__ == "__main__":
    sample_values = [8, 3, 1, 7, 0, 10, 2]
    print("Before:", sample_values)
    quicksort(sample_values)
    print("After: ", sample_values)
