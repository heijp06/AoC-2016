import re
import string


def part1(rows):
    abbas = [
        a + b + b + a
        for a in string.ascii_lowercase
        for b in string.ascii_lowercase
        if a != b
    ]
    result = 0
    for row in rows:
        fields = re.split(r"[][]", row)
        evens = " ".join(fields[0::2])
        odds = " ".join(fields[1::2])
        result += any(abba in evens for abba in abbas) and all(
            abba not in odds for abba in abbas
        )
    return result


def part2(rows):
    abas = [
        (a + b + a, b + a + b)
        for a in string.ascii_lowercase
        for b in string.ascii_lowercase
        if a != b
    ]
    result = 0
    for row in rows:
        fields = re.split(r"[][]", row)
        evens = " ".join(fields[0::2])
        odds = " ".join(fields[1::2])
        result += any(aba in evens and bab in odds for (aba, bab) in abas)
    return result
