"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

VALID_CARDS = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
def is_valid_card(card: str) -> bool:
    """Verifica si la carta es válida en Blackjack."""
    return card.upper() in VALID_CARDS

def value_of_card(card: str, ace_card_eleven: bool = False) -> int | None:
    """Determine the scoring value of a card.

    :param ace_card_eleven: return 1 in case of False and 11 in case of True
    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if not is_valid_card(card):
        return None

    face_cards = {'J': 10, 'Q': 10, 'K': 10}
    if card in face_cards:
        return face_cards[card]
    if card == 'A':
        return 11 if ace_card_eleven else 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == value_of_card(card_two) and value_of_card(card_two) == 10 or value_of_card(card_one) == 1:
        return card_one, card_two
    elif card_one == card_two and card_one.isdigit():
        return card_one, card_two
    if card_one != card_two and value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else:
        return card_two

def value_of_ace(card_one, card_two) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one == 'A' or card_two == 'A':
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 <= 21:
        return 11
    else:
        return 1

def is_blackjack(card_one, card_two) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if ((value_of_card(card_one) == 10 or value_of_card(card_one, True) == 11)
            and (value_of_card(card_two) == 10 or value_of_card(card_two, True) == 11) and
            value_of_card(card_one, True) + value_of_card(card_two, True) == 21):
        return True
    else:
        return False

def can_split_pairs(card_one, card_two) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if ((value_of_card(card_one) == 10 and value_of_card(card_two) == 10 or
            value_of_card(card_one) == 6 and value_of_card(card_two) == 6) or
            value_of_card(card_one, True) == 11 and value_of_card(card_two, True) == 11):
        return True
    else:
        return False

print(can_split_pairs('A','A'))
def can_double_down(card_one, card_two) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    total = value_of_card(card_one) + value_of_card(card_two)
    if 9 <= total <= 11:
        return True
    else:
        return False
