from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from quicksort import quicksort


def test_quicksort_empty_list():
    data = []
    assert quicksort(data) == []
    assert data == []


def test_quicksort_single_element():
    data = [42]
    assert quicksort(data) == [42]
    assert data == [42]


def test_quicksort_with_duplicates():
    data = [5, 3, 5, 2, 2, 5]
    expected = sorted(data)
    assert quicksort(data) == expected
    assert data == expected


def test_quicksort_already_sorted():
    data = [1, 2, 3, 4, 5]
    assert quicksort(data) == data
    assert data == [1, 2, 3, 4, 5]


def test_quicksort_reverse_sorted():
    data = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert quicksort(data) == expected
    assert data == expected


def test_quicksort_mixed_integers():
    data = [3, -1, 0, 8, -5, 2]
    expected = sorted(data)
    assert quicksort(data) == expected
    assert data == expected
