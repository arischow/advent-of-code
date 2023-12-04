from collections import defaultdict
from utils.text import read_from_file, read_from_variable

example_1 = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def score(set):
    if not set:
        return 0
    if len(set) == 1:
        return 1
    result = 1
    for _ in range(len(set) - 1):
        result *= 2
    return result


def part1(data):
    result = 0
    for line in data:
        card, numbers = line.split(": ")
        elf, me = numbers.split(" | ")
        elf = [x for x in elf.split()]
        me = [x for x in me.split()]
        s = set(elf) & set(me)
        result += score(s)
    return result


def part2(data):
    mapping = {}
    counts = defaultdict(int)
    for line in data:
        card, numbers = line.split(": ")
        card_id = int(card.split()[-1])
        elf, me = numbers.split(" | ")
        elf = [x for x in elf.split()]
        me = [x for x in me.split()]
        s = len(set(elf) & set(me))
        counts[card_id] += 1
        card_ranges = list(range(card_id + 1, card_id + s + 1))
        mapping[card_id] = card_ranges
        for x in card_ranges:
            # The original card itself + copies of it
            counts[x] += counts[card_id]
        print(
            f"Card {card_id} has {s} matching numbers, so can get the next {s} cards: {card_ranges}, so now I have cards: {counts}"
        )
    return sum(counts.values())


if __name__ == "__main__":
    assert part1(read_from_variable(example_1)) == 13
    print(part1(read_from_file("input.txt")))
    assert part2(read_from_variable(example_1)) == 30
    print(part2(read_from_file("input.txt")))
