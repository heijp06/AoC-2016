def part1(rows):
    result = 0
    for x, y, z in rows:
        a, b, c = int(x), int(y), int(z)
        result += a + b > c and b + c > a and c + a > b
    return result


def part2(rows):
    result = 0
    for index in range(0, len(rows), 3):
        for column in range(3):
            a, b, c = int(rows[index][column]), int(
                rows[index+1][column]), int(rows[index+2][column])
            result += a + b > c and b + c > a and c + a > b
    return result

