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


class Win:
    SCORE: int = 6


class Draw:
    SCORE: int = 3


class Lose:
    SCORE: int = 0


class Game:
    def __init__(
        self, elf: Union[Rock, Paper, Scissor], result: Union[Win, Draw, Lose]
    ):
        self._elf = elf
        self._result = result

    def play(self) -> int:
        if isinstance(self._result, Draw):
            return self._result.SCORE + self._elf.SCORE
        return self._result.SCORE + self.corresponding_hand_shape_score

    @property
    def corresponding_hand_shape_score(self) -> int:
        """
        No draw. Only win or lose.
        """
        print(self._elf, self._result)
        if isinstance(self._elf, Rock):
            if isinstance(self._result, Win):
                return Paper.SCORE
            if isinstance(self._result, Lose):
                return Scissor.SCORE
        if isinstance(self._elf, Paper):
            if isinstance(self._result, Win):
                return Scissor.SCORE
            if isinstance(self._result, Lose):
                return Rock.SCORE
        if isinstance(self._elf, Scissor):
            if isinstance(self._result, Win):
                return Rock.SCORE
            if isinstance(self._result, Lose):
                return Paper.SCORE


def main():
    MAPPING = {
        "X": Lose,
        "Y": Draw,
        "Z": Win,
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
        count += g.play()

    return count


if __name__ == "__main__":
    print(main())
