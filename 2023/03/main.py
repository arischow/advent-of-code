from collections import defaultdict
from utils.text import read_from_file, read_from_variable

example_1 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def is_adjacent_to_symbol(data, line_no, char_no):
    def is_symbol(s: str or None) -> int:
        if s is None:
            return False
        return not s.isdigit() and not s.isalpha() and s != "."

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dy, dx in directions:
        y, x = line_no + dy, char_no + dx
        if 0 <= y < len(data) and 0 <= x < len(data[y]) and is_symbol(data[y][x]):
            return True
    return False


def is_adjacent_to_gear(data, line_no, char_no):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dy, dx in directions:
        y, x = line_no + dy, char_no + dx
        if 0 <= y < len(data) and 0 <= x < len(data[y]) and data[y][x] == "*":
            return [y, x]
    return []


def part1(data):
    result = 0
    for line_no, line in enumerate(data):
        num = ""
        for char_no, char in enumerate(line):
            if char.isdigit():
                num += char
                if char_no == len(line) - 1 or not line[char_no + 1].isdigit():
                    if any(
                        is_adjacent_to_symbol(data, line_no, i)
                        for i in range(char_no - len(num) + 1, char_no + 1)
                    ):
                        result += int(num)
                    num = ""
    return result


def part2(data):
    gear = defaultdict(list)
    for line_no, line in enumerate(data):
        num = ""
        for char_no, char in enumerate(line):
            if char.isdigit():
                num += char
                if char_no == len(line) - 1 or not line[char_no + 1].isdigit():
                    for i in range(char_no - len(num) + 1, char_no + 1):
                        coord = is_adjacent_to_gear(data, line_no, i)
                        if coord:
                            gear[tuple(coord)].append(int(num))
                            break
                    num = ""

    return sum([coord[0] * coord[1] for coord in gear.values() if len(coord) == 2])


if __name__ == "__main__":
    assert part1(read_from_variable(example_1)) == 4361
    print("part 1:", part1(read_from_file("input.txt")))
    assert part2(read_from_variable(example_1)) == 467835
    print("part 2:", part2(read_from_file("input.txt")))
