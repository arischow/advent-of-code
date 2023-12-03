from utils.text import read_from_file, read_from_variable

example_1 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

BAGS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def read_from_variable(string: str) -> list[str]:
    return [line.strip() for line in string.splitlines() if line.strip()]


def playable(cubes):
    for line in cubes:
        cubes = line.split(", ")
        for cube in cubes:
            count, color = cube.split()
            # print("count:", count, "color:", color)
            if BAGS[color] < int(count):
                return False
    return True


def fewest(cubes):
    result = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for line in cubes:
        cubes = line.split(", ")
        for cube in cubes:
            count, color = cube.split()
            if result[color] < int(count):
                result[color] = int(count)
    return result.values()


def read_from_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line for line in f.readlines() if line.strip()]


def main(data):
    result = 0
    for line in data:

        game, cubes = line.split(": ")
        game_id = int(game.split()[-1])
        cubes = cubes.split("; ")
        if playable(cubes):
            result += game_id
    return result


def main2(data):
    result = 0
    for line in data:
        game, cubes = line.split(": ")
        cubes = cubes.split("; ")
        fewest_numbers = fewest(cubes)
        power = 1
        for number in fewest_numbers:
            power *= number
        result += power
    return result


if __name__ == "__main__":
    assert main(read_from_variable(example_1)) == 8
    print("part 1:", main(read_from_file("input.txt")))
    assert main2(read_from_variable(example_1)) == 2286
    print("part 2:", main2(read_from_file("input.txt")))
