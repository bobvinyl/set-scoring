# set-scoring

Scores a collection of sets by how common their items are across all the sets.

## How it works

[set_scoring.py](set_scoring.py) does the following:

1. Reads every file in the `input/` directory (relative to where you run the script). Each file is one set, with one item per line.
2. Normalizes each line by stripping surrounding whitespace and converting it to uppercase, so `a123` and ` A123 ` are the same item. Blank lines are skipped. Duplicate lines within a file collapse, since each file becomes a Python `set`.
3. Counts how many sets each item appears in, using a `collections.Counter`.
4. Scores each set as the sum of those counts over its items. A set made of items shared by many sets scores high. A set made of unique items scores low (each unique item contributes 1).
5. Prints a list of `(filename, score)` tuples and the elapsed run time.

Counting and scoring are both linear in the total number of items, so the script handles files with 100k+ lines each quickly.

## Usage

Put your input files in `input/`, then run from the repository root:

```
python set_scoring.py
```

Example input file (`input/set1.txt`):

```
1
2
3
```

Example output:

```
[   ('set1.txt', 14),
    ('set2.txt', 13)]
Completed in 0:00:00.123456 seconds.
```

## Notes

- Every file in `input/` is treated as a set, so remove files you don't want scored.
- Blank lines (and lines containing only whitespace) are skipped.
- Items are compared as text, so `1` and `01` are different items.
