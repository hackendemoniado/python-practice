import pytest
from exercises.exercism.lists.lists import (
    get_rounds,
    concatenate_rounds,
    list_contains_round,
    card_average,
    check_single,
    is_list_of_lists,
    approx_average_is_average,
    average_even_is_average_odd,
    maybe_double_last,
)


# ---------------------------
# Tests for get_rounds
# ---------------------------
def test_get_rounds_basic():
    assert get_rounds(5) == [5, 6, 7]


def test_get_rounds_zero():
    assert get_rounds(0) == [0, 1, 2]


def test_get_rounds_negative():
    assert get_rounds(-3) == [-3, -2, -1]


# ---------------------------
# Tests for concatenate_rounds
# ---------------------------
def test_concatenate_rounds_basic():
    assert concatenate_rounds([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_concatenate_rounds_empty():
    assert concatenate_rounds([], [1, 2]) == [1, 2]
    assert concatenate_rounds([1, 2], []) == [1, 2]


# ---------------------------
# Tests for list_contains_round
# ---------------------------
def test_list_contains_round_true():
    assert list_contains_round([1, 2, 3], 2)


def test_list_contains_round_false():
    assert not list_contains_round([1, 2, 3], 5)


# ---------------------------
# Tests for card_average
# ---------------------------
def test_card_average_basic():
    assert card_average([2, 4, 6]) == pytest.approx(4.0)


def test_card_average_single_card():
    assert card_average([10]) == 10.0


# ---------------------------
# Tests for check_single
# ---------------------------
def test_check_single_true_middle_match():
    # avg == middle
    assert check_single([2, 4, 6]) is True


def test_check_single_true_first_last_avg_match():
    # avg == (first + last) / 2
    assert check_single([2, 5, 8]) is True


def test_check_single_false():
    assert check_single([1, 2, 3, 9]) is False


# ---------------------------
# Tests for is_list_of_lists
# ---------------------------
def test_is_list_of_lists_true():
    assert is_list_of_lists([[1, 2], [3, 4]])


def test_is_list_of_lists_false():
    assert not is_list_of_lists([1, 2, 3])


# ---------------------------
# Tests for approx_average_is_average
# ---------------------------
def test_approx_average_is_average_single_true_middle():
    assert approx_average_is_average([2, 4, 6]) is True


def test_approx_average_is_average_single_true_first_last():
    assert approx_average_is_average([1, 5, 9]) is True


def test_approx_average_is_average_single_false():
    assert approx_average_is_average([1, 2, 3, 9]) is False


def test_approx_average_is_average_multiple_hands():
    hands = [[2, 4, 6], [1, 2, 3, 9]]
    result = approx_average_is_average(hands)
    assert result == [True, False]


def test_approx_average_is_average_invalid_type():
    with pytest.raises(TypeError):
        approx_average_is_average("not a list")


# ---------------------------
# Tests for average_even_is_average_odd
# ---------------------------
def test_average_even_is_average_odd_true():
    assert average_even_is_average_odd([2, 4, 6, 8, 10]) is True


def test_average_even_is_average_odd_false():
    assert not average_even_is_average_odd([1, 2, 3, 10])


# ---------------------------
# Tests for maybe_double_last
# ---------------------------
def test_maybe_double_last_with_jack():
    assert maybe_double_last([5, 11]) == [5, 22]


def test_maybe_double_last_without_jack():
    assert maybe_double_last([5, 10]) == [5, 10]


def test_maybe_double_last_longer_hand():
    assert maybe_double_last([2, 3, 11]) == [2, 3, 22]
