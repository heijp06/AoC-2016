import pytest
from lib import part1, part2


def test_part1():
    part1(data, low=2, high=5) == 2


def test_part2():
    pass


data = [
    "value 5 goes to bot 2",
    "bot 2 gives low to bot 1 and high to bot 0",
    "value 3 goes to bot 1",
    "bot 1 gives low to output 1 and high to bot 0",
    "bot 0 gives low to output 2 and high to output 0",
    "value 2 goes to bot 2"
]
