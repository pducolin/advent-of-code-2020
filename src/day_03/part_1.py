from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def next_cell(map_length, current_point):
    next_point = Point(current_point.x + 3, current_point.y + 1)
    if next_point.x >= map_length:
        next_point = Point(next_point.x - map_length, next_point.y)
    return next_point


TREE = '#'


def solution():
    trees_counter = 0
    with open('input.txt') as f:
        rows = [x for x in f.read().split('\n')]
        map_length = len(rows[0])
        map_height = len(rows)
        current_point = Point(0, 0)
        while current_point.y < map_height:
            if rows[current_point.y][current_point.x] == TREE:
                trees_counter += 1
            current_point = next_cell(map_length, current_point)
    print('🎉 Result is {}'.format(trees_counter))


if __name__ == "__main__":
    solution()
