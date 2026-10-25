from collections import Counter
from pprint import PrettyPrinter
from pathlib import Path
from datetime import datetime
import csv

pp = PrettyPrinter(indent=4)

start = datetime.now()

sets = []

dir_path = Path('input')

for file_path in dir_path.iterdir():
    if file_path.is_file():  # Ensure it is a file and not a folder
        with open(file_path, 'r', encoding='utf-8') as file:
            sets.append((file_path.name, set(s for line in file if (s := line.strip().upper()))))

set_items = [s[1] for s in sets]


counts = Counter(item for s in set_items for item in s)

scored_sets = []
for s in sets:
    scored_sets.append({"File": s[0], "Raw": sum(counts[i] for i in s[1]), 
                        "Overlap": sum(counts[i]-1 for i in s[1]),
                        "Typical": sum(counts[i]-1 for i in s[1]) / len(s[1])
                        })

pp.pprint(scored_sets)

with open(f"output/set_scores_{start.strftime('%Y%m%d_%H%M%S')}.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=['File', 'Raw', 'Overlap', 'Typical'])
    w.writeheader()
    w.writerows(scored_sets)

print(f'Completed in {datetime.now() - start} seconds.')