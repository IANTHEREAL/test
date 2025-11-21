# test

## Quicksort demo

This repository now includes a heavily documented quicksort implementation in
`quicksort.py`. The module exposes a single helper, `quicksort`, which sorts a
list in place and returns the same list for convenience.

### Example usage

```bash
python3 quicksort.py
```

You should see the unsorted and sorted sample lists printed to the console.

To call the helper from another script or a REPL:

```python
from quicksort import quicksort

numbers = [8, 3, 1, 7, 0, 10, 2]
quicksort(numbers)
print(numbers)
```

### Running the tests

The project uses Python's built-in `unittest` runner. Execute the suite with:

```bash
python3 -m unittest discover -s tests
```
