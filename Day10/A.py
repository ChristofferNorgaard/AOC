import math
import itertools
from collections import namedtuple, defaultdict

Point = namedtuple("Point", "x y")


def read(file):
    with open(file, "r") as f:
        return [
            Point(x, y)
            for y, line in enumerate(f.readlines())
            for x, c in enumerate(line) if c == "#"
        ]


def get_angle(p1, p2):
    return math.degrees(math.atan2(p1.x - p2.x, p1.y - p2.y) % (2 * math.pi))


def get_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def part_one():
    asteroids = read("input.txt")
    angles = defaultdict(set)

    for a1 in asteroids:
        for a2 in asteroids:
            if a1 == a2:
                continue

            angles[a1].add(get_angle(a1, a2))
        
    print(angles)
    a = len(max(angles.values(), key=len))
    for element in angles.keys():
        if(len(angles[element]) == a):
            print(element)
    return a
print(part_one())
