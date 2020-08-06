# TRY Filter function
import csv
import itertools as it
from collections import Counter

# read through file and get counts per date
with open('C:\GIT\Labs.Python\TransformCsv\Example.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    dates = it.chain.from_iterable(
        [date for _ in ids.split()]
        for date, ids in ((x[0].split(':')[0], x[1]) for x in reader))
    counts = Counter(dates)

# read through file again, and output as individual records with counts
with open('C:\GIT\Labs.Python\TransformCsv\Example.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    records = it.chain.from_iterable(
        [(l[0], d) for d in l[1].split()] for l in reader)
    new_lines = (l + (str(counts[l[0].split(':')[0]]), ) for l in records)

    with open("test2.csv", 'w') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(header)
        writer.writerows(new_lines)

with open("test2.csv", 'r') as new_f:
    reader = csv.reader(new_f)
    for line in reader:
        print(line)

