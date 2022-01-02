from typing import Iterable


class Floor:
    def __init__(self, microchips: Iterable[str], generators: Iterable[str]) -> None:
        self.microchips = frozenset(microchips)
        self.generators = frozenset(generators)

    @property
    def valid(self) -> bool:
        return not self.generators or self.microchips.issubset(self.generators)
