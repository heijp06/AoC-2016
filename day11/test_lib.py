import pytest
from column import Column, parse
from lib import part1, part2


def test_part1():
    pass


def test_part2():
    pass


def test_parse():
    column = parse(data)

    assert column.elevator == 0
    assert len(column.floors) == 4

    assert column[0].microchips == frozenset(["hydrogen", "lithium"])
    assert not column[0].generators

    assert not column[1].microchips
    assert column[1].generators == frozenset(["hydrogen"])

    assert not column[2].microchips
    assert column[2].generators == frozenset(["lithium"])

    assert not column[3].microchips
    assert not column[3].generators

def test_move():
    column = parse(data)
    columns = column.move()

    assert len(columns) == 1
    
    moved = columns[0]

    assert moved.elevator == 1
    assert len(moved.floors) == 4

    assert moved[0].microchips == frozenset(["lithium"])
    assert not moved[0].generators

    assert moved[1].microchips == frozenset(["hydrogen"])
    assert moved[1].generators == frozenset(["hydrogen"])

    assert moved[2] == column[2]

    assert moved[3] == column[3]

def test_microchip_up():
    column = parse(data)
    new_column = column.microchip_up("hydrogen")

    assert len(new_column) == 4
    assert new_column[0].microchips == frozenset(["lithium"])
    assert new_column[1].microchips == frozenset(["hydrogen"])



data = [
    "The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.",
    "The second floor contains a hydrogen generator.",
    "The third floor contains a lithium generator.",
    "The fourth floor contains nothing relevant."
]
