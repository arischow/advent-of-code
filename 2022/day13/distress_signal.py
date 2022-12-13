import ast
import itertools
from functools import cmp_to_key

# parse
f = open("distress_signal.txt")
lines = f.read().splitlines()
packets = [ast.literal_eval(line) for line in lines if line]
f.close()


def chunks(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i : i + n]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, list) and isinstance(right, list):
        for l, r in itertools.zip_longest(left, right, fillvalue=None):
            if l is None:
                return -1
            if r is None:
                return 1

            cmp = compare(l, r)
            if cmp != 0:
                return cmp
        return 0

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    return compare(left, right)


# processing
def part1():
    count = 0
    for index, (left, right) in enumerate(chunks(packets, 2), start=1):
        if compare(left, right) < 0:
            count += index
    return count


def part2():
    dividers = [[[2]], [[6]]]

    p = sorted(packets + dividers, key=cmp_to_key(compare))
    a = p.index(dividers[0]) + 1
    b = p.index(dividers[1]) + 1
    return a * b


print(part1())
print(part2())
