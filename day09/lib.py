import re

def part1(rows: list[str]) -> int:
    file = "".join(rows)
    pos = 0
    length = 0
    regex = re.compile(r"\((\d+)x(\d+)\)")
    while pos < len(file):
        match = regex.search(file, pos=pos)
        if not match:
            length += len(file) - pos
            break
        number = int(match[1])
        repeat = int(match[2])
        length += match.start() - pos + number * repeat
        pos = match.end() + number
    return length


def part2(rows: list[str]) -> int:
    pass
