from computer import Computer


def part1(rows: list[str]) -> int:
    computer = Computer(rows)
    computer.run()
    return computer.a


def part2(rows: list[str]) -> int:
    computer = Computer(rows)
    computer.c = 1
    computer.run()
    return computer.a
