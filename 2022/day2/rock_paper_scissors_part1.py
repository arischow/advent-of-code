from typing import Union


class HandShape:
    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return True
        return False


class Rock(HandShape):
    SCORE: int = 1


class Paper(HandShape):
    SCORE: int = 2


class Scissor(HandShape):
    SCORE: int = 3


class Game:
    WIN = 6
    DRAW = 3
    LOSE = 0

    def __init__(
        self, elf: Union[Rock, Paper, Scissor], me: Union[Rock, Paper, Scissor]
    ):
        self._elf = elf
        self._me = me

    def play(self) -> int:
        if self._elf == self._me:
            return self.DRAW
        if isinstance(self._me, Rock):
            if isinstance(self._elf, Scissor):
                return self.WIN
            elif isinstance(self._elf, Paper):
                return self.LOSE
        if isinstance(self._me, Scissor):
            if isinstance(self._elf, Rock):
                return self.LOSE
            elif isinstance(self._elf, Paper):
                return self.WIN
        if isinstance(self._me, Paper):
            if isinstance(self._elf, Rock):
                return self.WIN
            elif isinstance(self._elf, Scissor):
                return self.LOSE

    def calc(self):
        result = self.play()
        return result + self._me.SCORE


def main():
    MAPPING = {
        "X": Rock,
        "Y": Paper,
        "Z": Scissor,
        "A": Rock,
        "B": Paper,
        "C": Scissor,
    }
    f = open("rock_paper_scissors.txt")
    count = 0
    for line in f:
        lst = line.strip().split()
        elf, me = MAPPING[lst[0]], MAPPING[lst[1]]
        g = Game(elf(), me())
        count += g.calc()

    return count


if __name__ == "__main__":
    print(main())
