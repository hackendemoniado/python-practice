import pytest
from exercises.exercism.conditionals.conditionals import (
    is_criticality_balanced,
    reactor_efficiency,
    fail_safe
)

# ----------------------------------------------------------
# Tests para is_criticality_balanced
# ----------------------------------------------------------
@pytest.mark.parametrize("temperature,neutrons,expected", [
    (750, 600, True),
    (800, 600, False),
    (750, 500, False),
    (1000, 1000, False),
])
def test_is_criticality_balanced(temperature, neutrons, expected):
    assert is_criticality_balanced(temperature, neutrons) == expected


# ----------------------------------------------------------
# Tests para reactor_efficiency
# ----------------------------------------------------------
@pytest.mark.parametrize("voltage,current,max_power,expected", [
    (80, 1, 100, 'green'),      # 80% efficiency
    (70, 1, 100, 'orange'),     # 70%
    (50, 1, 100, 'red'),        # 50%
    (20, 1, 100, 'black'),      # 20%
])
def test_reactor_efficiency(voltage, current, max_power, expected):
    assert reactor_efficiency(voltage, current, max_power) == expected


# ----------------------------------------------------------
# Tests para fail_safe
# ----------------------------------------------------------
@pytest.mark.parametrize("temp,neutrons,threshold,expected", [
    (10, 5, 100, 'LOW'),       # 50 < 90
    (9, 11, 100, 'NORMAL'),    # 99 within ±10%
    (10, 10, 100, 'NORMAL'),   # 100 exactly
    (11, 10, 100, 'NORMAL'),   # 110 upper limit
    (12, 10, 100, 'DANGER'),   # 120 > 110
])
def test_fail_safe(temp, neutrons, threshold, expected):
    assert fail_safe(temp, neutrons, threshold) == expected

