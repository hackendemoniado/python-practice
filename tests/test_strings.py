import pytest
from exercises.exercism.strings.strings import add_prefix, add_prefix_un, make_word_groups, remove_suffix_ness, adjective_to_verb

# ---------------------------------------------------------------------------
# add_prefix_un
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "word, expected",
    [
        ("happy",  "unhappy"),
        ("fold",   "unfold"),
        ("",       "un"),        # palabra vacía
        ("real", "unreal"),  # ya comienza con 'un'
    ],
)
def test_add_prefix_un(word, expected):
    assert add_prefix_un(word) == expected


# ---------------------------------------------------------------------------
# add_prefix
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "prefix, word, expected",
    [
        ("en",   "joy",       "enjoy"),
        ("pre",  "view",      "preview"),
        ("auto", "pilot",     "autopilot"),
        ("",     "nothing",   "nothing"),  # prefijo vacío
    ],
)
def test_add_prefix(prefix, word, expected):
    assert add_prefix(word, prefix) == expected


# ---------------------------------------------------------------------------
# make_word_groups
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "vocab_words, expected",
    [
        (["en",  "close",  "joy",  "lighten"],
         "en :: enclose :: enjoy :: enlighten"),
        (["pre", "serve",  "dispose", "position"],
         "pre :: preserve :: predispose :: preposition"),
        (["auto", "pilot", "immune"],
         "auto :: autopilot :: autoimmune"),
        ([], ""),                           # lista vacía
        (["sub", "merge"], ""),             # prefijo no permitido (fuera de check_prefix)
    ],
)
def test_make_word_groups(vocab_words, expected):
    assert make_word_groups(vocab_words) == expected


# ---------------------------------------------------------------------------
# remove_suffix_ness
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "word, expected",
    [
        ("heaviness",  "heavy"),   # termina en 'i' después de quitar 'ness'
        ("sadness",    "sad"),
        ("shyness",    "shy"),
        ("irateness",  "irate"),   # sin cambio ortográfico extra
        ("kind",       "kind"),    # no contiene 'ness'
    ],
)
def test_remove_suffix_ness(word, expected):
    assert remove_suffix_ness(word) == expected


# ---------------------------------------------------------------------------
# adjective_to_verb
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "sentence, index, expected",
    [
        ("It got dark as the sun set.",          2, "darken"),
        ("The skies are bright.",                3, "brighten"),
        ("He spoke loud, and everyone heard.",   2, "louden"),
        ("That is a quick, smart fox!",          4, "smarten"),
    ],
)
def test_adjective_to_verb(sentence, index, expected):
    assert adjective_to_verb(sentence, index) == expected


def test_adjective_to_verb_out_of_range():
    """Comprobar que lanza IndexError si el índice no existe."""
    with pytest.raises(IndexError):
        adjective_to_verb("Short sentence.", 5)