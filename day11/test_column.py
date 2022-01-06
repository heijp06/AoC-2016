from data_for_testing import data
from column import Column, parse
from floor import Floor
import pytest


HYDROGEN = "hydrogen"
LITHIUM = "lithium"


def test_parse():
    actual = parse(data)

    expected = Column([
        Floor([HYDROGEN, LITHIUM], []),
        Floor([], [HYDROGEN]),
        Floor([], [LITHIUM]),
        Floor([], [])
    ])

    assert actual == expected


def test_move():
    column = parse(data)
    columns = list(column.move())

    assert len(columns) == 1

    expected = Column([
        Floor([LITHIUM], []),
        Floor([HYDROGEN], [HYDROGEN]),
        Floor([], [LITHIUM]),
        Floor([], [])
    ]).elevator_up()

    assert columns[0] == expected


def test_move2():
    column = Column([
        Floor([], []),
        Floor([HYDROGEN, LITHIUM], [HYDROGEN, LITHIUM]),
        Floor([], []),
        Floor([], [])
    ]).elevator_up()
    actual = set(column.move())

    expected = {
        column.microchip_up(HYDROGEN),
        column.microchip_down(HYDROGEN),
        column.microchip_up(LITHIUM),
        column.microchip_down(LITHIUM),
        column.microchip_up(HYDROGEN).elevator_down().microchip_up(LITHIUM),
        column.microchip_down(HYDROGEN).elevator_up().microchip_down(LITHIUM),
        column.microchip_up(HYDROGEN).elevator_down().generator_up(HYDROGEN),
        column.microchip_down(HYDROGEN).elevator_up().generator_down(HYDROGEN),
        column.microchip_up(LITHIUM).elevator_down().generator_up(LITHIUM),
        column.microchip_down(LITHIUM).elevator_up().generator_down(LITHIUM),
        column.generator_up(HYDROGEN).elevator_down().generator_up(LITHIUM),
        column.generator_down(HYDROGEN).elevator_up().generator_down(LITHIUM),
    }

    assert actual == expected


def test_microchip_up():
    column = parse(data)
    new_column = column.microchip_up(HYDROGEN)

    assert len(new_column) == 4
    assert new_column[0].microchips == frozenset([LITHIUM])
    assert new_column[1].microchips == frozenset([HYDROGEN])


@pytest.mark.parametrize("column,steps", [
    (Column([
        Floor([HYDROGEN], [HYDROGEN, LITHIUM]),
        Floor([LITHIUM], []),
        Floor([], []),
        Floor([], []),
    ]), 13),
    (Column([
        Floor([HYDROGEN], [HYDROGEN, LITHIUM]),
        Floor([LITHIUM], []),
        Floor([], []),
        Floor([], []),
    ]).elevator_up(), 16),
    (Column([
        Floor([HYDROGEN], [HYDROGEN]),
        Floor([LITHIUM], []),
        Floor([], [LITHIUM]),
        Floor([], []),
    ]).elevator_up(), 12),
    (Column([
        Floor([HYDROGEN], [HYDROGEN]),
        Floor([LITHIUM], []),
        Floor([], [LITHIUM]),
        Floor([], []),
    ]).elevator_up().elevator_up(), 15),
])
def test_min_steps_left(column: Column, steps: int) -> None:
    assert column.min_steps_left() == steps
