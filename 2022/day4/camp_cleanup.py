def destruct_to_section_id_list(section: str) -> set:
    start, end = [int(s) for s in section.split("-")]
    return set(number for number in range(start, end + 1))


def destruct_elves_pair(sections: str) -> list[str]:
    return sections.split(",")


def is_fully_contained(s1: set, s2: set) -> bool:
    union = s1 | s2
    return union == s1 or union == s2


def is_overlapped(s1: set, s2: set) -> bool:
    overlap = s1 & s2
    return len(overlap) > 0


def main_part1():
    f = open("camp_cleanup.txt")
    count = 0
    for line in f:
        line = line.strip()
        s1_str, s2_str = destruct_elves_pair(line)
        s1, s2 = destruct_to_section_id_list(s1_str), destruct_to_section_id_list(
            s2_str
        )
        contained = is_fully_contained(s1, s2)
        if contained:
            count += 1
    return count


def main_part2():
    f = open("camp_cleanup.txt")
    count = 0
    for line in f:
        line = line.strip()
        s1_str, s2_str = destruct_elves_pair(line)
        s1, s2 = destruct_to_section_id_list(s1_str), destruct_to_section_id_list(
            s2_str
        )
        overlapped = is_overlapped(s1, s2)
        if overlapped:
            count += 1
    return count


if __name__ == "__main__":
    print(main_part1())
    print(main_part2())
