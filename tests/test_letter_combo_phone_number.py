from pythonalgos.letter_combo_phone_number import letter_combo_phone_number


def test_basic():
    input = "23"
    assert letter_combo_phone_number(input) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
