import pytest
from lib import part1, part2


@pytest.mark.parametrize("file,length", [
    ("ADVENT", 6),
    ("A(1x5)BC", 7),
    ("(3x3)XYZ", 9),
    ("A(2x2)BCD(2x2)EFG", 11),
    ("(6x1)(1x3)A", 6),
    ("X(8x2)(3x3)ABCY", 18)
])
def test_part1(file: str, length: int) -> None:
    assert part1(file) == length


def test_part2():
    pass
