from data_for_testing import data
from column import Column, parse
from floor import Floor


def test_parse():
    actual = parse(data)

    expected = Column([
        Floor(["hydrogen", "lithium"], []),
        Floor([], ["hydrogen"]),
        Floor([], ["lithium"]),
        Floor([], [])
    ])

    assert actual == expected


def test_move():
    column = parse(data)
    columns = list(column.move())

    assert len(columns) == 1

    expected = Column([
        Floor(["lithium"], []),
        Floor(["hydrogen"], ["hydrogen"]),
        Floor([], ["lithium"]),
        Floor([], [])
    ]).elevator_up()

    assert columns[0] == expected

def test_move2():
    HYDROGEN = "hydrogen"
    LITHIUM = "lithium"

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
    new_column = column.microchip_up("hydrogen")

    assert len(new_column) == 4
    assert new_column[0].microchips == frozenset(["lithium"])
    assert new_column[1].microchips == frozenset(["hydrogen"])
