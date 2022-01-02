import re
import numpy as np
import matplotlib.pyplot as plt

WIDTH = 50
HEIGHT = 6


def part1(rows: list[str]) -> int:
    return int(go(rows).sum())


def go(rows: list[str]) -> np.array:
    screen = np.zeros((HEIGHT, WIDTH))
    for row in rows:
        fields = re.split(r"[ xy=]+", row)
        match fields:
            case ["rect", width, height]:
                screen[:int(height), :int(width)] = 1
            case [_, "row", y, _, shift]:
                screen[int(y), :] = np.roll(screen[int(y), :], int(shift))
            case [_, "column", x, _, shift]:
                screen[:, int(x)] = np.roll(screen[:, int(x)], int(shift))
    return screen


def part2(rows: list[str]) -> None:
    screen = go(rows)

    plt.gca().invert_yaxis()
    plt.pcolormesh(screen)
    fig = plt.gcf()
    fig.set_size_inches(1, 1)
    plt.show()
