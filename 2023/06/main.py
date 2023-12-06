import math
from collections import defaultdict
from utils.text import read_from_file, read_from_variable

example_1 = """
Time:      7  15   30
Distance:  9  40  200
"""


class Boat:
    def __init__(self, time, speed=0, distance=0):
        self.time = time
        self.speed = speed
        self.distance = distance

    def charge(self, count):
        self.speed += count
        self.time -= count

    def travel(self):
        self.distance += self.speed * self.time
        self.time -= self.time


def parse_current_record_part1(data):
    current_record = {}
    time, distance = data
    time = [int(x) for x in time.split(":")[1].split()]
    distance = [int(x) for x in distance.split(":")[1].split()]

    for k, v in zip(time, distance):
        current_record[k] = v

    return current_record


def parse_current_record_part2(data):
    current_record = {}
    time, distance = data
    time = int("".join([str(x) for x in time.split(":")[1].split()]))
    distance = int("".join([str(x) for x in distance.split(":")[1].split()]))

    current_record[time] = distance

    return current_record


def main(parse_func, data):
    current_record = parse_func(data)

    ways = defaultdict(int)
    for k, v in current_record.items():
        for i in (x for x in range(k + 1)):
            boat = Boat(k)
            boat.charge(i)
            boat.travel()
            if boat.distance > v:
                ways[k] += 1

    return math.prod(ways.values())


if __name__ == "__main__":
    assert main(parse_current_record_part1, read_from_variable(example_1)) == 288
    print(main(parse_current_record_part1, read_from_file("input.txt")))
    assert main(parse_current_record_part2, read_from_variable(example_1)) == 71503
    # print(main(parse_current_record_part2, read_from_file("input.txt")))
