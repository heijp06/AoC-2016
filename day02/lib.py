def part1(rows):
    (x, y) = (1, 1)
    code = ""
    for row in rows:
        for move in row:
            if move == "U" and y > 0:
                y -= 1
            if move == "D" and y < 2:
                y += 1
            if move == "L" and x > 0:
                x -= 1
            if move == "R" and x < 2:
                x += 1
        number = 3 * y + x + 1
        code += str(number)
    return code


def part2(rows):
    (x, y) = (0, 2)
    code = ""
    for row in rows:
        for move in row:
            if move == "U" and (x, y) not in [(0, 2), (1, 1), (2, 0), (3, 1), (4, 2)]:
                y -= 1
            if move == "D" and (x, y) not in [(0, 2), (1, 3), (2, 4), (3, 3), (4, 2)]:
                y += 1
            if move == "L" and (x, y) not in [(2, 0), (1, 1), (0, 2), (1, 3), (2, 4)]:
                x -= 1
            if move == "R" and (x, y) not in [(2, 0), (3, 1), (4, 2), (3, 3), (2, 4)]:
                x += 1
        number = [
            (2, 0), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2),
            (3, 2), (4, 2), (1, 3), (2, 3), (3, 3), (2, 4)
        ].index((x, y))
        code += "123456789ABCD"[number]
    return code
