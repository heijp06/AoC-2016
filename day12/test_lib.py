import pytest
from lib import part1, part2


def test_part1():
    assert part1(data) == 42


def test_part2():
    pass


data = [
    "cpy 41 a",
    "inc a",
    "inc a",
    "dec a",
    "jnz a 2",
    "dec a"
]
