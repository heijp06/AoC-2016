import pytest
from lib import part1, part2, id_if_real

testdata = [
    ("aaaaa-bbb-z-y-x-123[abxyz]", 123),
    ("a-b-c-d-e-f-g-h-987[abcde]", 987),
    ("not-a-real-room-404[oarel]", 404),
    ("totally-real-room-200[decoy]", 0)
]


@pytest.mark.parametrize("name,real", testdata)
def test_lib(name, real):
    assert id_if_real(name) == real
