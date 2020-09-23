from pythonalgos.mountain_array import is_mountain_array


def test_basic():
    data = [0, 3, 2, 1]
    assert is_mountain_array(data) == True


def test_hump():
    data = [2, 1, 5, 6, 2, 1]
    assert is_mountain_array(data) == True


def test_length_less_3():
    data = [2, 1]
    assert is_mountain_array(data) == False


def test_no_mountain_increase():
    data = [1, 3, 4, 5]
    assert is_mountain_array(data) == False


def test_no_mountain_decrease():
    data = [5, 4, 3, 1]
    assert is_mountain_array(data) == False
