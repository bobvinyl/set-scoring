# set-scoring

Scores a collection of sets by how common their items are across all the sets.

## How it works

[set_scoring.py](set_scoring.py) does the following:

1. Reads every file in the `input/` directory (relative to where you run the script). Each file is one set, with one item per line.
2. Normalizes each line by stripping surrounding whitespace and converting it to uppercase, so `a123` and ` A123 ` are the same item. Blank lines are skipped. Duplicate lines within a file collapse, since each file becomes a Python `set`.
3. Counts how many sets each item appears in, using a `collections.Counter`.
4. Scores each set three ways (see [Scores](#scores)).
5. Prints the scores, writes them to a timestamped CSV in `output/`, and prints the elapsed run time.

Counting and scoring are both linear in the total number of items, so the script handles files with 100k+ lines each quickly.

## Scores

Let `count(i)` be the number of sets that contain item `i`.

| Column | Formula | Meaning |
|--------|---------|---------|
| `Raw` | sum of `count(i)` over the set's items | Total item popularity. Every item contributes at least 1, so large sets score high even if they share nothing. |
| `Overlap` | sum of `count(i) - 1` over the set's items | How many times the set's items also appear in other sets. Items unique to the set contribute 0, which removes the bias toward large sets. |
| `Typical` | `Overlap` / number of items in the set | Average number of other sets that share each item. Ranges from 0 (all items unique) to (number of sets - 1) (every item is in every set). Use it to compare sets of different sizes. |

## Usage

Put your input files in `input/` and make sure the `output/` directory exists (the script does not create it), then run from the repository root:

```
python set_scoring.py
```

Example input file (`input/set1.txt`):

```
1
2
3
```

Example console output (one dictionary per input file):

```
[   {'File': 'set1.txt', 'Overlap': 9, 'Raw': 14, 'Typical': 1.8},
    {'File': 'set2.txt', 'Overlap': 7, 'Raw': 13, 'Typical': 1.4}]
Completed in 0:00:00.123456 seconds.
```

The same rows are written to `output/set_scores_YYYYMMDD_HHMMSS.csv` with the columns `File`, `Raw`, `Overlap`, `Typical`. Each run creates a new file, so earlier results are kept.

## Notes

- Every file in `input/` is treated as a set, so remove files you don't want scored.
- The `input/` and `output/` directories are listed in `.gitignore`.
- Blank lines (and lines containing only whitespace) are skipped.
- Items are compared as text, so `1` and `01` are different items.
