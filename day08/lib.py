import re
import numpy as np

WIDTH = 50
HEIGHT = 6


def part1(rows: list[str]) -> int:
    screen = np.zeros((HEIGHT, WIDTH), dtype=object)
    for row in rows:
        fields = re.split(r"[ xy=]+", row)
        match fields:
            case ["rect", width, height]:
                screen[:int(height), :int(width)] = 1
            case [_, "row", y, _, shift]:
                screen[int(y), :] = np.roll(screen[int(y), :], int(shift))
            case [_, "column", x, _, shift]:
                screen[:, int(x)] = np.roll(screen[:, int(x)], int(shift))
    return screen.sum()


def part2(rows: list[str]) -> int:
    pass
