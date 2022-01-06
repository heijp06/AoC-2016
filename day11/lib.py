from queue import PriorityQueue
from column import Column, parse
from floor import Floor, ATOMS


def part1(rows: list[str]) -> int:
    column = parse(rows)
    return go(column)


def part2(rows: list[str]) -> int:
    parsed_column = parse(rows)
    ELERIUM = "elerium"
    DILITHIUM = "dilithium"
    microchips = list(parsed_column[0].microchips)
    microchips += [ELERIUM, DILITHIUM]
    generators = list(parsed_column[0].generators)
    generators += [ELERIUM, DILITHIUM]
    column = Column([
        Floor(microchips, generators),
        parsed_column[1],
        parsed_column[2],
        parsed_column[3],
    ])
    return go(column)


def go(column: Column) -> int:
    if column.final:
        return 0
    columns = PriorityQueue()
    min_steps = None
    columns.put((column.min_steps_left(), column))
    steps_by_column = {column: 0}
    progress = 0
    shortest = None
    while columns.qsize():
        min_total_steps_left, column = columns.get()
        if progress != min_total_steps_left:
            progress = min_total_steps_left
            print(progress)
        if min_steps and min_steps <= min_total_steps_left:
            break
        steps = steps_by_column[column] + 1
        if min_steps and steps >= min_steps:
            continue
        for new_column in column.move():
            if new_column.final and (not min_steps or steps < min_steps):
                shortest = new_column
                min_steps = steps
            if new_column in steps_by_column and steps >= steps_by_column[new_column]:
                continue
            steps_by_column[new_column] = steps
            columns.put((steps + new_column.min_steps_left(), new_column))
    dump_history(shortest)
    return min_steps


def dump_history(column: Column) -> None:
    history = []
    while column:
        history.insert(0, column)
        column = column.parent
    for i, column in enumerate(history):
        print("Step", i)
        dump(column)


def dump(column: Column) -> None:
    elements = frozenset()
    for i in range(4):
        elements = elements.union(column[i].microchips)
    elements = sorted(list(elements))
    for i in range(4, 0, -1):
        floor = column[i - 1]
        print(f"F{i} ", end='')
        dump_item(column.elevator == i - 1, "E")
        for element in elements:
            symbol = ATOMS[element]
            dump_item(element in floor.generators, f"{symbol}G")
            dump_item(element in floor.microchips, f"{symbol}M")
        print()
    print()


def dump_item(condition: bool, symbol: str) -> None:
    if condition:
        print(f"{symbol:4}", end="")
    else:
        print(".   ", end="")
