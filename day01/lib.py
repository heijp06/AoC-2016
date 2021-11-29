def part1(rows):
    (dx, dy) = (0, 1)
    (x, y) = (0, 0)
    for row in rows:
        turn = row[0]
        steps = int(row[1:])
        (dx, dy) = (dy, -dx) if turn == "R" else (-dy, dx)
        (x, y) = (x + steps * dx, y + steps * dy)
    return abs(x) + abs(y)


def part2(rows):
    (dx, dy) = (0, 1)
    (x, y) = (0, 0)
    locations = {(x, y)}
    for row in rows:
        turn = row[0]
        steps = int(row[1:])
        (dx, dy) = (dy, -dx) if turn == "R" else (-dy, dx)
        for _ in range(steps):
            (x, y) = (x + dx, y + dy)
            if (x, y) in locations:
                return abs(x) + abs(y)
            locations.add((x, y))
    return None
