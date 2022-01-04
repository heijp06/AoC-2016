from column import Column, parse
from floor import ATOMS

def part1(rows: list[str]) -> int:
    column = parse(rows)
    if column.final:
        return 0
    columns = {column}
    seen = {column}
    steps = 0
    while columns:
        print(len(columns))
        steps += 1
        new_columns = set()
        for column in columns:
            for new_column in column.move():
                if new_column in seen:
                    continue
                if new_column.final:
                    dump_history(new_column)
                    return steps
                seen.add(new_column)
                new_columns.add(new_column)
        columns = new_columns
    return -1

def part2(rows: list[str]) -> int:
    pass

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
