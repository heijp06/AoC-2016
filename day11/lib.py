from column import parse

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
                    return steps
                seen.add(new_column)
                new_columns.add(new_column)
        columns = new_columns
    return -1

def part2(rows: list[str]) -> int:
    pass
