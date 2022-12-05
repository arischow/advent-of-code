STACKS = {
    "1": ["Q", "M", "G", "C", "L"],
    "2": ["R", "D", "L", "C", "T", "F", "H", "G"],
    "3": ["V", "J", "F", "N", "M", "T", "W", "R"],
    "4": ["J", "F", "D", "V", "Q", "P"],
    "5": ["N", "F", "M", "S", "L", "B", "T"],
    "6": ["R", "N", "V", "H", "C", "D", "P"],
    "7": ["H", "C", "T"],
    "8": ["G", "S", "J", "V", "Z", "N", "H", "P"],
    "9": ["Z", "F", "H", "G"],
}


def move_p1(
    from_: str,
    to: str,
    quantity: int,
) -> None:
    from_stack, to_stack = STACKS[from_], STACKS[to]

    for _ in range(quantity):
        crate = from_stack.pop()
        to_stack.append(crate)


def pickup(from_stack, to_stack, quantity):
    pass


def move_p2(
    from_: str,
    to_: str,
    quantity: int,
) -> None:
    from_stack, to_stack = STACKS[from_], STACKS[to_]
    crate_mover = []
    for _ in range(quantity):
        crate = from_stack.pop()
        crate_mover.insert(0, crate)

    to_stack += crate_mover


def move_ast(sentence: str) -> (str, str, int):
    sentence_list = sentence.split()
    from_ = sentence_list[3]
    to = sentence_list[5]
    quantity = int(sentence_list[1])
    return from_, to, quantity


def main_p1():
    f = open("move.txt")
    for line in f:
        line = line.strip()
        from_, to, quantity = move_ast(line)
        move_p1(from_, to, quantity)

    result = ""
    for i in range(len(STACKS)):
        result += STACKS[str(i + 1)][-1]

    return result


def main_p2():
    f = open("move.txt")
    for line in f:
        line = line.strip()
        from_, to, quantity = move_ast(line)
        move_p2(from_, to, quantity)

    result = ""
    for i in range(len(STACKS)):
        result += STACKS[str(i + 1)][-1]

    return result


if __name__ == "__main__":
    # TODO: stack ast

    # Get the result one at a time as we are manipulating mutable objects here
    # print(main_p1())
    print(main_p2())
