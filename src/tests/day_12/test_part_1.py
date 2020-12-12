from src.day_12.part_1 import solution

EXAMPLE = """F10
N3
F7
R90
F11"""


def test_solution():
    assert solution(EXAMPLE) == 25
