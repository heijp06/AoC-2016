from __future__ import annotations, generators
from collections.abc import Iterable
from itertools import combinations, product
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

    def __getitem__(self, index: int) -> Floor:
        return self.floors[index]
    
    def __len__(self) -> int:
        return len(self.floors)

    @property
    def up(self) -> Floor | None:
        level = self.elevator
        return None if level == len(self.floors) else self.floors[level + 1]

    @property
    def down(self) -> Floor | None:
        level = self.elevator
        return None if level == 0 else self.floors[level - 1]

    @property
    def here(self) -> Floor:
        return self.floors[self.elevator]

    def move(self) -> list[Column]:
        pass
        # result = []

        # # take 1 or 2 microchips
        # for microchip in self.here.microchips:
        #     new_microchips = set(self.here.microchips).remove(microchip)
        #     new_this_floor = Floor(new_microchips, self.here.generators)
        #     if self.up:
        #         new_up = Floor({microchip}.union(self.up.microchips), self.up.generators)
        #         if new_up.valid:
        #             result.append(Column([])

        # # take 1 or 2 generators

        # # take a microchip and a generator

    def microchip_up(self, microchip: str) -> Column:
        microchips_here = set(self.here.microchips)
        microchips_here.remove(microchip)
        here = Floor(microchips_here, self.here.generators)
        microchips_up = set(self.up.microchips)
        microchips_up.add(microchip)
        up = Floor(microchips_up, self.here.generators)
        # return Column(self[self.elevator:] + here + up + self[:self.elevator+2])
        return Column((*self[:self.elevator], here, up, *self[self.elevator+2:]))
