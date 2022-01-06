from __future__ import annotations
from collections.abc import Iterable
from itertools import chain, combinations, product
from copy import copy
import re
from functools import total_ordering

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
    for item in re.split(r",? and |, ", data):
        match re.split(r"[ -]", item):
            case ["a", element, "compatible", "microchip"]:
                microchips.append(element)
            case ["a", element, "generator"]:
                generators.append(element)
    return Floor(microchips, generators)


@total_ordering
class Column:
    def __init__(self, floors: Iterable[Floor]) -> None:
        self.elevator = 0
        self.floors = tuple(floors)
        self.parent = None

    def _key(self) -> tuple[int, tuple(Floor, ...)]:
        return self.elevator, self.floors

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Column) and self._key() == other._key()

    def __hash__(self) -> int:
        return hash(self._key())

    def __lt__(self, other: Column) -> bool | NotImplemented:
        if not isinstance(other, Column):
            return NotImplemented
        return self.elevator < other.elevator or self.floors < other.floors

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
        return chain(
            self.move_microchips(1),
            self.move_microchips(2),
            self.move_generators(1),
            self.move_generators(2),
            self.move_both()
        )
    
    def move_both(self) -> Iterable[Column]:
        for microchip in self.here.microchips:
            if microchip not in self.here.generators:
                continue
            if self.up:
                up = self.microchips_and_generators_up([microchip], [microchip])
                if up.valid:
                    up.parent = self
                    yield up
            if self.down:
                down = self.microchips_and_generators_down([microchip], [microchip])
                if down.valid:
                    down.parent = self
                    yield down

    def move_microchips(self, number: int) -> Iterable[Column]:
        if self.up:
            for microchips in combinations(self.here.microchips, number):
                up = self.microchips_and_generators_up(
                    microchips, [])
                if up.valid:
                    up.parent = self
                    yield up
        if self.down:
            for microchips in combinations(self.here.microchips, number):
                down = self.microchips_and_generators_down(
                    microchips, [])
                if down.valid:
                    down.parent = self
                    yield down
    
    def move_generators(self, number: int) -> Iterable[Column]:
        if self.up:
            for generators in combinations(self.here.generators, number):
                up = self.microchips_and_generators_up(
                    [], generators)
                if up.valid:
                    up.parent = self
                    yield up
        if self.down:
            for generators in combinations(self.here.generators, number):
                down = self.microchips_and_generators_down(
                    [], generators)
                if down.valid:
                    down.parent = self
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
        up = self.up.add_microchip(microchip)
        column = Column((*self[:self.elevator], here,
                        up, *self[self.elevator+2:]))
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

    def min_steps_left(self) -> int:
        elevator = self.elevator
        cost = 0
        items = [
            len(floor.microchips) + len(floor.generators)
            for floor in self.floors
        ]
        if elevator < 3:
            items[elevator] -= 1
            other = None
            for i in range(3):
                if items[i]:
                    other = i
                    break
            if other is None:
                cost += 3 - elevator
            else:
                items[other] -= 1
                if other < elevator:
                    cost += elevator - other
                    cost += 3 - other
                else:
                    cost += 3 - elevator
        for i in range(3):
            cost += 2 * (3 - i) * items[i]
        return cost
