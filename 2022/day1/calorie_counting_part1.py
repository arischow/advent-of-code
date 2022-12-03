#!/usr/bin/env python3


def main():
    f = open("calorie_counting.txt", "r")
    final_result = 0
    count = 0
    for line in f:
        line = line.strip()
        if line == "":
            final_result = max(final_result, count)
            count = 0
        else:
            count += int(line)

    return final_result


if __name__ == "__main__":
    print(main())
