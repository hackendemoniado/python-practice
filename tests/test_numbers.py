import pytest
from exercises.exercism.numbers import armstrong_number, collatz_conjeture

# ----------------------------------------------------------
# Test for armstrong_number.py
# ----------------------------------------------------------
@pytest.mark.parametrize("number,expected", [
    (0, True),
    (1, True),
    (5, True),
    (153, True),
    (9474, True),
    (10, False),
    (123, False),
])
def test_is_armstrong_number(number: int, expected: bool) -> None:
    assert armstrong_number.is_armstrong_number(number) == expected

# ----------------------------------------------------------
# Tests para collatz_conjeture.py
# ----------------------------------------------------------
@pytest.mark.parametrize("number,expected", [
    (1, 0),
    (2, 1),
    (3, 7),
    (6, 8),
    (12, 9),
])
def test_steps(number, expected):
    assert collatz_conjeture.steps(number) == expected

def test_steps_invalid():
    with pytest.raises(ValueError):
        collatz_conjeture.steps(0)
    with pytest.raises(ValueError):
        collatz_conjeture.steps(-5)