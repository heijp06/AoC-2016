import csv
import pyperclip    # type: ignore
from lib import part1, part2
from data_for_testing import data


def read_rows(**kwargs):
    with open('data.txt', newline='') as csv_file:
        # return list(csv.reader(csv_file, **kwargs))
        # return csv_file.read().strip()
        return csv_file.read().splitlines()


def clip(x):
    if x is None:
        return
    pyperclip.copy(x)


rows = read_rows()
x = part1(data)
print(f"Part 1: {x}")
clip(x)

x = part2(rows)
print(f"Part 2: {x}")
clip(x)
