"""Demonstration script for the quicksort sorting algorithm."""

from __future__ import annotations

from typing import List, Sequence, TypeVar

T = TypeVar("T")


def quicksort(values: Sequence[T]) -> List[T]:
    """Return a new list containing ``values`` in ascending order.

    This is a simple functional quicksort that never mutates the input sequence.
    It chooses the first element as the pivot and recursively sorts the items
    smaller and larger than the pivot. This approach keeps the code compact for
    demonstration purposes, even though it is not optimized for production use.
    """

    items = list(values)
    if len(items) <= 1:
        return items

    pivot = items[0]
    smaller = [value for value in items[1:] if value <= pivot]
    greater = [value for value in items[1:] if value > pivot]
    return quicksort(smaller) + [pivot] + quicksort(greater)


def main() -> None:
    """Showcase the quicksort implementation with an example list."""

    sample = [10, 7, 3, 8, 9, 1, 5]
    print("Original:", sample)
    sorted_sample = quicksort(sample)
    print("Sorted:", sorted_sample)


if __name__ == "__main__":
    main()
