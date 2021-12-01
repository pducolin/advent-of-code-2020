from src.y2021.day_01.part_2 import solution

EXAMPLE = """199
200
208
210
200
207
240
269
260
263
"""


def test_solution():
    assert solution(EXAMPLE) == 5
