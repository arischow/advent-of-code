example_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

example_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def convert_to_digit(line: str, index: int, possible_strings: list[str]) -> str:
    for string in possible_strings:
        if line[index : index + len(string)] == string:
            answer = str(mapping[string])
            return answer
    return ""


def read_from_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line for line in f.readlines() if line.strip()]


def read_from_string(string: str) -> list[str]:
    return [line.strip() for line in string.splitlines() if line.strip()]


def main(data):
    result = 0
    for line in data:
        final = "0"
        s = ""
        if line[0].isdigit() and line[-1].isdigit():
            final = line[0] + line[-1]
        else:
            for index, element in enumerate(line.strip()):
                if element.isdigit():
                    s += element
                if element.isalpha():
                    possibilities = [
                        key for key in list(mapping.keys()) if key.startswith(element)
                    ]
                    digit = convert_to_digit(line, index, possibilities)
                    s += digit
                if len(s) == 1:
                    final = s[0] + s[0]
                elif len(s) > 1:
                    final = s[0] + s[-1]
        result += int(final)
    return result


if __name__ == "__main__":
    assert main(read_from_string(example_1)) == 142
    assert main(read_from_string(example_2)) == 281
    assert main(read_from_file("input.txt")) == 55218
