from pythonalgos.longest_substring import length_of_longest_substring


def test_basic():
    s: str = "abcabcbb"
    assert length_of_longest_substring(s) == 3


def test_all_same():
    s: str = "bbbbb"
    assert length_of_longest_substring(s) == 1


def test_harder():
    s: str = "pwwkew"
    assert length_of_longest_substring(s) == 3
