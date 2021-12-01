from collections import Counter


def part1(rows):
    return decode(rows, 1)


def part2(rows):
    return decode(rows, None)


def decode(rows, number):
    result = ""
    transposed = list(zip(*rows))
    for column in transposed:
        counter = Counter(column)
        letter = counter.most_common(number)[-1][0]
        result += letter
    return result
