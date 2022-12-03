import string


def split_compartments(rucksack: str) -> (str, str):
    middle = len(rucksack) // 2
    return rucksack[:middle], rucksack[middle:]


def find_shared_item_type(rucksack1: str, rucksack2: str) -> str:
    for item in rucksack1:
        if item in rucksack2:
            return item


MAPPING = {
    k: v for k, v in zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53))
}


def main():
    f = open("rucksack_reorganization.txt")
    count = 0
    for line in f:
        rucksack = line.strip()
        rucksack1, rucksack2 = split_compartments(rucksack)
        item = find_shared_item_type(rucksack1, rucksack2)
        count += MAPPING[item]
    return count


if __name__ == "__main__":
    print(main())
