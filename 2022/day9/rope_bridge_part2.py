from dataclasses import dataclass
from typing import Optional
from operator import itemgetter


@dataclass
class Coordination:
    x: int
    y: int
    next: Optional["Coordination"] = None
    previous: Optional["Coordination"] = None

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    @property
    def overlapped(self):
        if not self.next and self.previous:
            return True
        return self.x == self.next.x and self.y == self.next.y

    @property
    def vertically_adjacent(self):
        if not self.next and self.previous:
            return True
        return self.x == self.next.x and abs(abs(self.y) - abs(self.next.y)) == 1

    @property
    def horizontally_adjacent(self):
        if not self.next and self.previous:
            return True
        return self.y == self.next.y and abs(abs(self.x) - abs(self.next.x)) == 1

    @property
    def diagonally_adjacent(self):
        if not self.next and self.previous:
            return True
        return (
            abs(abs(self.x) - abs(self.next.x)) == 1
            and abs(abs(self.y) - abs(self.next.y)) == 1
        )

    @property
    def adjacent(self):
        return (
            self.overlapped
            or self.horizontally_adjacent
            or self.vertically_adjacent
            or self.diagonally_adjacent
        )

    def move(self, direction):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1

    def readjacent(self, direction):
        if self.adjacent:
            return
        if not self.next and self.previous:
            return
        # if self.adjacent:
        #     print("adjacent", self, self.next)
        #     return
        # else:
        #     print("non adjacent", self, self.next)
        if direction == "U":
            self.next.y = self.y - 1
            self.next.x = self.x
        elif direction == "D":
            self.next.y = self.y + 1
            self.next.x = self.x
        elif direction == "L":
            self.next.x = self.x + 1
            self.next.y = self.y
        elif direction == "R":
            self.next.x = self.x - 1
            self.next.y = self.y


class Rope:
    def __init__(self, length):
        self.knots = [Coordination(0, 0) for _ in range(length)]
        for index, tail in enumerate(self.knots):
            if index >= 1:
                self.knots[index].previous = self.knots[index - 1]
            if index == len(self.knots) - 1:
                break
            self.knots[index].next = self.knots[index + 1]
        self.records = set()

    @property
    def head(self):
        return self.knots[0]

    @property
    def overlapped(self):
        return all(knot.overlapped for knot in self.knots)

    @property
    def vertically_adjacent(self):
        return all(knot.vertically_adjacent for knot in self.knots)

    @property
    def horizontally_adjacent(self):
        return all(knot.horizontally_adjacent for knot in self.knots)

    @property
    def diagonally_adjacent(self):
        return all(knot.diagonally_adjacent for knot in self.knots)

    @property
    def adjacent(self):
        return all(knot.adjacent for knot in self.knots)

    def readjacent(self, direction):
        for knot in self.knots:
            knot.readjacent(direction)

    def move(self, direction):
        self.head.move(direction)
        self.readjacent(direction)
        print(self.knots)
        self.record()

    def record(self):
        for knot in self.knots[1:]:
            self.records.add((knot.x, knot.y))


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
    rope = Rope(2)
    main(rope)
    print(len(rope.records))
