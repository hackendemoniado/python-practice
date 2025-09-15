import pytest
from exercises.exercism.bools import leap_year, triangle

# ----------------------------------------------------------
# Test for leap_year.py
# ----------------------------------------------------------
@pytest.mark.parametrize("year,expected", [
    (1996, True),
    (2000, True),
    (1900, False),
    (1999, False),
    (1997, False),
])
def test_leap_year(year: int, expected: bool) -> None:
    assert leap_year.leap_year(year) == expected


# ----------------------------------------------------------
# Test for triangle.py
# ----------------------------------------------------------
@pytest.mark.parametrize("sides,expected", [
    ([3, 3, 3], True),
    ([5, 5, 8], True),
    ([0, 1, 1], False),
    ([1, 2, 3], False),
])
def test_triangle(sides: list[int], expected: bool) -> None:
    assert triangle.is_valid_triangle(sides) == expected

@pytest.mark.parametrize("sides,expected", [
    ([3, 3, 3], True),
    ([5, 5, 8], False),
    ([2, 3, 4], False),
])
def test_equilateral(sides: list[int], expected: bool) -> None:
    assert triangle.equilateral(sides) == expected

@pytest.mark.parametrize("sides,expected", [
    ([5, 5, 8], True),
    ([3, 3, 3], True),
    ([2, 3, 4], False),
])
def test_isosceles(sides: list[int], expected: bool) -> None:
    assert triangle.isosceles(sides) == expected

@pytest.mark.parametrize("sides,expected", [
    ([2, 3, 4], True),
    ([3, 3, 3], False),
    ([5, 5, 8], False),
])
def test_scalene(sides: list[int], expected: bool) -> None:
    assert triangle.scalene(sides) == expected