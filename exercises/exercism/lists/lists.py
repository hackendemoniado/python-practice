"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

from typing import List, Union, overload, cast


def get_rounds(number: int) -> List[int]:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: List[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds


def card_average(hand: List[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def check_single(hand: List[int]) -> bool:
    """Check if the average can be approximated by first+last or middle card."""
    avg = card_average(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle = hand[len(hand) // 2]
    return avg in (first_last_avg, middle)


def is_list_of_lists(hand: Union[List[int], List[List[int]]]) -> bool:
    """Return True if 'hand' is really a List[List[int]]."""
    return all(isinstance(one_hand, list) for one_hand in hand)


@overload
def approx_average_is_average(hand: List[int]) -> bool: ...
@overload
def approx_average_is_average(hand: List[List[int]]) -> List[bool]: ...


def approx_average_is_average(
    hand: Union[List[int], List[List[int]]]
) -> Union[bool, List[bool]]:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Works with:
    - A single hand (List[int]) -> returns bool
    - A list of hands (List[List[int]]) -> returns List[bool]
    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    if is_list_of_lists(hand):
        hand_lists = cast(List[List[int]], hand)
        return [check_single(h) for h in hand_lists]
    elif isinstance(hand, list) and all(isinstance(x, int) for x in hand):
        hand_single = cast(List[int], hand)
        return check_single(hand_single)
    else:
        raise TypeError("Parameter 'hand' should be List[int] or List[List[int]]")


def average_even_is_average_odd(hand: List[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even = hand[0::2]
    odd = hand[1::2]
    average_even = sum(even) / len(even)
    average_odd = sum(odd) / len(odd)
    return average_even == average_odd


def maybe_double_last(hand: List[int]) -> List[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    return hand[:-1] + [hand[-1] * 2 if hand[-1] == 11 else hand[-1]]
