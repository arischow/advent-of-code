#!/usr/bin/env python3


def main():
    f = open("calorie_counting.txt", "r")
    result = []
    count = 0
    for line in f:
        line = line.strip()
        print(line)
        if line == "":
            result.append(count)
            count = 0
        else:
            count += int(line)

    result.sort(reverse=True)
    return sum(x for x in result[:3])


if __name__ == "__main__":
    print(main())
