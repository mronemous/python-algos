from pythonalgos.boat_rescue import optimize_boats


def test_basic():
    people: [int] = [1, 2, 2, 3, 3]
    assert optimize_boats(people=people, limit=3) == 4


def test_all_under_limit():
    people: [int] = [1, 1, 2, 2, 2]
    assert optimize_boats(people=people, limit=3) == 3


def test_no_elements():
    people: [int] = []
    assert optimize_boats(people=people, limit=3) == 0


def test_zero():
    people: [int] = [0, 2, 2, 3, 3]
    assert optimize_boats(people=people, limit=3) == 4
