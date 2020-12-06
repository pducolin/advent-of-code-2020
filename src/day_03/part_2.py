from collections import namedtuple
from functools import reduce

Point = namedtuple("Point", ["x", "y"])


def next_cell(map_length, current_point, to_the_right=3, to_the_bottom=1):
    next_point = Point(current_point.x + to_the_right, current_point.y + to_the_bottom)
    if next_point.x >= map_length:
        next_point = Point(next_point.x - map_length, next_point.y)
    return next_point


TREE = '#'

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
PATHS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def solution():
    trees_counter = [0 for x in range(len(PATHS))]
    with open('input.txt') as f:
        rows = [x for x in f.read().split('\n')]
        map_length = len(rows[0])
        map_height = len(rows)
        for i in range(len(PATHS)):
            to_the_right, to_the_bottom = PATHS[i]
            current_point = Point(0, 0)
            while current_point.y < map_height:
                if rows[current_point.y][current_point.x] == TREE:
                    trees_counter[i] += 1
                current_point = next_cell(map_length, current_point, to_the_right, to_the_bottom)
    print('🎉 Result is {}'.format(reduce((lambda x, y: x * y), trees_counter)))


if __name__ == "__main__":
    solution()
