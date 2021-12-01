import re
from itertools import groupby
from operator import itemgetter


def part1(rows):
    result = 0
    for row in rows:
        _, id, real = id_if_real(row)
        if real:
            result += id
    return result


def part2(rows):
    for row in rows:
        name, id, real = id_if_real(row)
        if real:
            print(decrypt(name, id), id)
        

def id_if_real(room):
    match = re.match(r"([a-z-]+)(\d+)\[(\w+)]", room)
    name, id, checksum = match.groups()
    groups = groupby(char for char in sorted(name) if char != "-")
    counts = [(key, len(list(group))) for key, group in groups]
    sorted_on_char = sorted(counts, key=itemgetter(0))
    sorted_on_count_and_char = sorted(
        sorted_on_char, key=itemgetter(1), reverse=True)
    first_five = "".join(char for char, _ in sorted_on_count_and_char[:5])
    return name, int(id), checksum == first_five

def decrypt(name, id):
    return "".join(rotate(char, id) for char in name)

def rotate(char, id):
    if char == "-":
        return " "
    return chr(ord('a') + (ord(char) - ord('a') + id) % 26)