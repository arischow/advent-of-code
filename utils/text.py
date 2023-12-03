def read_from_variable(string: str) -> list[str]:
    return [line.strip() for line in string.splitlines() if line.strip()]


def read_from_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]
