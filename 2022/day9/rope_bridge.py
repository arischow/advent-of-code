from dataclasses import dataclass
from typing import Optional


@dataclass
class Coordination:
    x: int
    y: int


class Rope:
    def __init__(self):
        self.head = Coordination(0, 0)
        self.tail = Coordination(0, 0)
        self.records = set()

    @property
    def overlapped(self):
        return self.head.x == self.tail.x and self.head.y == self.tail.y

    @property
    def vertically_adjacent(self):
        return (
            self.head.x == self.tail.x and abs(abs(self.head.y) - abs(self.tail.y)) == 1
        )

    @property
    def horizontally_adjacent(self):
        return (
            self.head.y == self.tail.y and abs(abs(self.head.x) - abs(self.tail.x)) == 1
        )

    @property
    def diagonally_adjacent(self):
        return (
            abs(abs(self.head.x) - abs(self.tail.x)) == 1
            and abs(abs(self.head.y) - abs(self.tail.y)) == 1
        )

    @property
    def adjacent(self):
        return (
            self.overlapped
            or self.horizontally_adjacent
            or self.vertically_adjacent
            or self.diagonally_adjacent
        )

    def readjacent(self, direction):
        if self.adjacent:
            return
        if direction == "U":
            self.tail.y = self.head.y - 1
            self.tail.x = self.head.x
        elif direction == "D":
            self.tail.y = self.head.y + 1
            self.tail.x = self.head.x
        elif direction == "L":
            self.tail.x = self.head.x + 1
            self.tail.y = self.head.y
        elif direction == "R":
            self.tail.x = self.head.x - 1
            self.tail.y = self.head.y

    def move(self, direction):
        if direction == "U":
            self.head.y += 1
        elif direction == "D":
            self.head.y -= 1
        elif direction == "L":
            self.head.x -= 1
        elif direction == "R":
            self.head.x += 1
        self.readjacent(direction)
        self.record()

    def record(self):
        self.records.add((self.tail.x, self.tail.y))


def parse(command: str):
    direction, value = command.split()
    return direction, int(value)


def main(rope):
    f = open("rope_bridge.txt")

    for command in f:
        command = command.strip()
        direction, value = parse(command)
        for _ in range(value):
            rope.move(direction)

    f.close()


if __name__ == "__main__":
    rope = Rope()
    main(rope)
    assert len(rope.records) == 6037
