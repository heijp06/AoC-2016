import csv
import pyperclip
from lib import part1, part2
from datetime import datetime


def read_rows(**kwargs):
    with open('data.txt', newline='') as csv_file:
        # return list(csv.reader(csv_file, **kwargs))
        return csv_file.read().strip()
        # return csv_file.read().splitlines()


def clip(x):
    if not x:
        return
    pyperclip.copy(x)


row = read_rows()
t0 = datetime.now()
x = part1(row)
t1 = datetime.now()
print(f"Part 1: {x}")
clip(x)

t2 = datetime.now()
x = part2(row)
t3 = datetime.now()
print(f"Part 2: {x}")
print(t1 - t0)
print(t3 - t2)
print((t1 - t0) + (t3 - t2))
clip(x)
