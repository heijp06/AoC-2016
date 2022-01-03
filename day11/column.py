from __future__ import annotations
from collections.abc import Iterable
from itertools import combinations
from copy import copy
import re

from floor import Floor


def parse(rows: list[str]) -> Column:
    floors = []
    marker = "contains "
    for row in rows:
        index = row.find(marker)
        data = row[index + len(marker):-1]
        floors.append(parse_floor(data))
    return Column(floors)


def parse_floor(data: str) -> Floor:
    microchips = []
    generators = []
    for item in re.split(r", |,? and ", data):
        match re.split(r"[ -]", item):
            case ["a", element, "compatible", "microchip"]:
                microchips.append(element)
            case ["a", element, "generator"]:
                generators.append(element)
    return Floor(microchips, generators)


class Column:
    def __init__(self, floors: Iterable[Floor]) -> None:
        self.elevator = 0
        self.floors = tuple(floors)

    def _key(self) -> tuple[int, tuple(Floor, ...)]:
        return self.elevator, self.floors

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Column) and self._key() == other._key()

    def __hash__(self) -> int:
        return hash(self._key())

    def __repr__(self) -> str:
        return f"Elevator: {self.elevator}, Floors: {self.floors}"

    def __getitem__(self, index: int) -> Floor:
        return self.floors[index]

    def __len__(self) -> int:
        return len(self.floors)

    @property
    def up(self) -> Floor | None:
        level = self.elevator
        return None if level == len(self.floors) - 1 else self.floors[level + 1]

    @property
    def down(self) -> Floor | None:
        level = self.elevator
        return None if level == 0 else self.floors[level - 1]

    @property
    def here(self) -> Floor:
        return self.floors[self.elevator]

    @property
    def valid(self) -> bool:
        return all(floor.valid for floor in self.floors)

    @property
    def final(self) -> bool:
        return all(not floor.microchips and not floor.generators for floor in self.floors[:-1])

    def move(self) -> Iterable[Column]:
        choices = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
        for number_of_microchips, number_of_generators in choices:
            if number_of_microchips > len(self.here.microchips) and number_of_generators > len(self.here.generators):
                continue
            if self.up:
                for microchips in combinations(self.here.microchips, number_of_microchips):
                    for generators in combinations(self.here.generators, number_of_generators):
                        up = self.microchips_and_generators_up(microchips, generators)
                        if up.valid:
                            yield up
            if self.down:
                for microchips in combinations(self.here.microchips, number_of_microchips):
                    for generators in combinations(self.here.generators, number_of_generators):
                        down = self.microchips_and_generators_down(microchips, generators)
                        if down.valid:
                            yield down

    def microchips_and_generators_up(self, microchips: Iterable[str], generators: Iterable[str]) -> Column:
        assert self.up
        up = self.elevator_up()
        for microchip in microchips:
            up = up.elevator_down()
            up = up.microchip_up(microchip)
        for generator in generators:
            up = up.elevator_down()
            up = up.generator_up(generator)
        return up

    def microchips_and_generators_down(self, microchips: Iterable[str], generators: Iterable[str]) -> Column:
        assert self.down
        down = self.elevator_down()
        for microchip in microchips:
            down = down.elevator_up()
            down = down.microchip_down(microchip)
        for generator in generators:
            down = down.elevator_up()
            down = down.generator_down(generator)
        return down

    def microchip_up(self, microchip: str) -> Column:
        assert self.up
        here = self.here.remove_microchip(microchip)
        up1 = self.up.add_microchip(microchip)
        column = Column((*self[:self.elevator], here,
                        up1, *self[self.elevator+2:]))
        column.elevator = self.elevator + 1
        return column

    def microchip_down(self, microchip: str) -> Column:
        assert self.down
        here = self.here.remove_microchip(microchip)
        down = self.down.add_microchip(microchip)
        column = Column((*self[:self.elevator-1], down,
                        here, *self[self.elevator+1:]))
        column.elevator = self.elevator - 1
        return column

    def generator_up(self, generator: str) -> Column:
        assert self.up
        here = self.here.remove_generator(generator)
        up = self.up.add_generator(generator)
        column = Column((*self[:self.elevator], here,
                        up, *self[self.elevator+2:]))
        column.elevator = self.elevator + 1
        return column

    def generator_down(self, generator: str) -> Column:
        assert self.down
        here = self.here.remove_generator(generator)
        down = self.down.add_generator(generator)
        column = Column((*self[:self.elevator-1], down,
                        here, *self[self.elevator+1:]))
        column.elevator = self.elevator - 1
        return column

    def elevator_up(self) -> Column:
        assert self.up
        column = copy(self)
        column.elevator = self.elevator + 1
        return column

    def elevator_down(self) -> Column:
        assert self.down
        column = copy(self)
        column.elevator = self.elevator - 1
        return column
