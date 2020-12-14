from datetime import date

from importlib import import_module

import click


def load_input(filename):
    with open(filename) as f:
        return f.read()


@click.command()
@click.option('--day', default=date.today().day, help='Day to execute.')
def execute_day(day):
    """Execute Advent of code solution for a specific day."""
    part_1 = import_module('src.day_{:02d}.part_1'.format(day))
    part_2 = import_module('src.day_{:02d}.part_2'.format(day))
    data = load_input('src/day_{:02d}/input.txt'.format(day))
    print('🎉 Result for day {}, part 1 is {}'.format(day, part_1.solution(data)))
    print('🎉 Result for day {}, part 2 is {}'.format(day, part_2.solution(data)))


if __name__ == '__main__':
    execute_day()
