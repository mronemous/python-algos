from pythonalgos.first_bad_version import find_bad_version


def is_bad_version(version: int) -> bool:
    if version <= 3:
        return False
    else:
        return True


def test_basic():
    assert find_bad_version([1, 2, 3, 4, 5], is_bad_version) == 3


def test_bad_first():
    assert find_bad_version([4, 5, 6, 7, 8], is_bad_version) == 0


def test_bad_last():
    assert find_bad_version([1, 2, 3, 4], is_bad_version) == 3
