import pytest

from exercises.exercism.comparisons.black_jack import (can_double_down,
                                                       can_split_pairs,
                                                       higher_card,
                                                       is_blackjack,
                                                       is_valid_card,
                                                       value_of_ace,
                                                       value_of_card)


# ----------------------------------------------------------
# Test for is_valid_card
# ----------------------------------------------------------
def test_valid_cards():
    for card in ["2", "10", "J", "Q", "K", "A"]:
        assert is_valid_card(card)


def test_invalid_cards():
    for card in ["1", "11", "Z", "", "joker"]:
        assert not is_valid_card(card)


# ----------------------------------------------------------
# Test for value_of_card
# ----------------------------------------------------------
def test_value_of_number_cards():
    assert value_of_card("2") == 2
    assert value_of_card("10") == 10


def test_value_of_face_cards():
    assert value_of_card("J") == 10
    assert value_of_card("Q") == 10
    assert value_of_card("K") == 10


def test_value_of_ace_both_options():
    assert value_of_ace("A", "2") == 1
    assert value_of_ace("5", "5") == 11


def test_value_of_invalid_card_returns_none():
    assert value_of_card("joker") is None


# ----------------------------------------------------------
# Test for higher_card
# ----------------------------------------------------------
def test_higher_card_with_different_values():
    assert higher_card("2", "5") == "5"
    assert higher_card("K", "3") == "K"


def test_higher_card_with_equal_values():
    assert higher_card("8", "8") == ("8", "8")
    assert higher_card("Q", "K") == "Q" or "K"


# ----------------------------------------------------------
# Test for value_of_ace
# ----------------------------------------------------------
def test_value_of_ace_returns_1_if_ace_present():
    assert value_of_ace("A", "10") == 1
    assert value_of_ace("5", "A") == 1


def test_value_of_ace_returns_11_if_safe():
    assert value_of_ace("5", "3") == 11


def test_value_of_ace_returns_1_if_not_safe():
    assert value_of_ace("10", "9") == 1


# ----------------------------------------------------------
# Test for is_blackjack
# ----------------------------------------------------------
def test_is_blackjack_true():
    assert is_blackjack("A", "K")
    assert is_blackjack("10", "A")


def test_is_blackjack_false():
    assert not is_blackjack("9", "A")
    assert not is_blackjack("8", "8")


# ----------------------------------------------------------
# Test for can_split_pairs
# ----------------------------------------------------------
def test_can_split_pairs_true():
    assert can_split_pairs("8", "8")
    assert can_split_pairs("K", "Q")
    assert can_split_pairs("A", "A")


def test_can_split_pairs_false():
    assert not can_split_pairs("8", "9")
    assert not can_split_pairs("10", "A")


# ----------------------------------------------------------
# Test for can_double_down
# ----------------------------------------------------------
def test_can_double_down_true():
    assert can_double_down("5", "4")
    assert can_double_down("6", "5")


def test_can_double_down_false():
    assert not can_double_down("10", "10")
    assert not can_double_down("2", "3")
