"""A minimal quicksort implementation for demo purposes.

The module exposes a single `quicksort` function that returns a new sorted list
so that callers can see the effect of the algorithm without mutating the
original input. When executed as a script it prints a short demonstration.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def quicksort(values: Sequence[T]) -> list[T]:
    """Return a sorted copy of *values* using the quicksort algorithm.

    Args:
        values: Any finite sequence of orderable items (lists, tuples, etc.).

    Returns:
        A new list containing the sorted items from *values*.
    """
    items = list(values)
    if len(items) <= 1:
        return items

    pivot = items[0]
    left_partition = [item for item in items[1:] if item <= pivot]
    right_partition = [item for item in items[1:] if item > pivot]
    return quicksort(left_partition) + [pivot] + quicksort(right_partition)


def _demo() -> None:
    """Print an example showing the algorithm in action."""
    sample = [8, 3, 1, 7, 0, 10, 2]
    print("Quick sort demonstration")
    print("Original:", sample)
    print("Sorted:  ", quicksort(sample))


if __name__ == "__main__":
    _demo()
