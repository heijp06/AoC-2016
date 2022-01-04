from __future__ import annotations
from typing import Iterable

ATOMS = {
    "hydrogen": "H",
    "lithium": "Li",
    "cobalt": "Co",
    "curium": "Cm",
    "plutonium": "Pu",
    "promethium": "Pm",
    "ruthenium": "Ru",
    "elerium": "El",
    "dilithium": "Di"
}


class Floor:
    def __init__(self, microchips: Iterable[str], generators: Iterable[str]) -> None:
        self.microchips = frozenset(microchips)
        self.generators = frozenset(generators)

    def _key(self) -> tuple[frozenset, frozenset]:
        return self.microchips, self.generators
    
    def __hash__(self) -> int:
        return hash(self._key())

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Floor) and self._key() == other._key()

    def __repr__(self) -> str:
        microchips = {ATOMS[microchip] for microchip in self.microchips}
        generators = {ATOMS[generator] for generator in self.generators}
        return f"Chips: {microchips or '{}'}, Generators: {generators or '{}'}"

    @property
    def valid(self) -> bool:
        return not self.generators or self.microchips.issubset(self.generators)

    def add_microchip(self, microchip: str) -> Floor:
        microchips = set(self.microchips)
        microchips.add(microchip)
        return Floor(microchips, self.generators)

    def add_generator(self, generator: str) -> Floor:
        generators = set(self.generators)
        generators.add(generator)
        return Floor(self.microchips, generators)

    def remove_microchip(self, microchip: str) -> Floor:
        microchips = set(self.microchips)
        microchips.remove(microchip)
        return Floor(microchips, self.generators)

    def remove_generator(self, generator: str) -> Floor:
        generators = set(self.generators)
        generators.remove(generator)
        return Floor(self.microchips, generators)
