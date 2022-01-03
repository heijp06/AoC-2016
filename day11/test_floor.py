from floor import Floor


def test_add_microchip():
    MICROCHIP = "hydrogen"
    floor = Floor([], [])

    result = floor.add_microchip(MICROCHIP)

    assert result == Floor([MICROCHIP], [])


def test_add_generator():
    GENERATOR = "hydrogen"
    floor = Floor([], [])

    result = floor.add_generator(GENERATOR)

    assert result == Floor([], [GENERATOR])

def test_remove_microchip():
    MICROCHIP = "hydrogen"
    floor = Floor([MICROCHIP], [])

    result = floor.remove_microchip(MICROCHIP)

    assert result == Floor([], [])


def test_remove_generator():
    GENERATOR = "hydrogen"
    floor = Floor([], [GENERATOR])

    result = floor.remove_generator(GENERATOR)

    assert result == Floor([], [])
