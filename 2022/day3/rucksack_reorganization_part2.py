import string
import itertools


def find_shared_item_type(elves_group: list) -> str:
    s = None
    for rucksack in elves_group:
        rucksack_set = set(rucksack)
        if s is None:
            s = rucksack_set
        else:
            s = s & rucksack_set
    return s.pop()


MAPPING = {
    k: v for k, v in zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53))
}


def main():
    count = 0
    with open("rucksack_reorganization.txt") as f:
        while True:
            elves_group = list(itertools.islice(f, 3))
            if not elves_group:
                break
            elves_group = [rucksack.strip() for rucksack in elves_group]
            badge = find_shared_item_type(elves_group)
            count += MAPPING[badge]
    return count


if __name__ == "__main__":
    print(main())
