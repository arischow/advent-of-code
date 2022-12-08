import numpy as np


def multiply(*args):
    product = 1
    for a in args:
        product *= a

    return product


class Grid:
    def __init__(self, data):
        self.data = data
        self.max_scenic_score = 0

    def validate_inside_if_visible(self, row, column, tree_height):
        neighbours = {
            "left": self.data[row][column - 1 :: -1],  # left
            "right": self.data[row][column + 1 :],  # right
            "up": self.data.T[column][row - 1 :: -1],  # up
            "down": self.data.T[column][row + 1 :],  # down
        }
        can_be_seen_from = {}
        scenic_score = {}
        for direction, array in neighbours.items():
            visible = all(tree_height > n for n in array)
            can_be_seen_from[direction] = visible
            if visible:
                scenic_score[direction] = len(array)
            else:
                scenic_score[direction] = self.blocked_by(tree_height, array)

        self.max_scenic_score = max(
            self.max_scenic_score, multiply(*scenic_score.values())
        )
        return any(can_be_seen_from.values())

    def blocked_by(self, tree_height, direction_array):
        score = 0
        for other_tree_height in direction_array:
            score += 1
            if tree_height <= other_tree_height:
                break
        return score

    def visible_count(self):
        count = 0
        for index, row in enumerate(self.data):
            last = len(self.data) - 1
            if index in (0, last):
                count += len(row)
            else:
                for idx, tree_height in enumerate(row):
                    last = len(row) - 1
                    if idx in (0, last):
                        count += 1
                    else:
                        visible = self.validate_inside_if_visible(
                            index, idx, tree_height
                        )
                        if visible:
                            count += 1
        return count


if __name__ == "__main__":
    lst = []
    f = open("treetop_tree_house.txt")
    count = 0
    for line in f:
        line = line.strip()
        result = [int(number_str) for number_str in line]
        lst.append(result)
        count += 1

    g_array = np.array(lst)

    mapping = {}

    g = Grid(g_array)
    print(g.visible_count())
    print(g.max_scenic_score)
