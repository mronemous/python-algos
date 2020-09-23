from pythonalgos.max_container_water import find_max_container_area


def test_basic():
    data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert find_max_container_area(data) == 49
