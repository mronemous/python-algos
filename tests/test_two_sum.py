from pythonalgos.two_sum import two_sum_brute_force, two_sum_hash, two_sum


def test_two_sum_brute_force_valid():
    data = [-2, 1, 2, 4, 7, 11]
    target = 13
    assert two_sum_brute_force(data, target) is True


def test_two_sum_brute_force_invalid():
    data = [-2, 1, 2, 4, 7, 11]
    target = 100
    assert two_sum_brute_force(data, target) is False


def test_two_sum_hash_valid():
    data = [-2, 1, 2, 4, 7, 11]
    target = 13
    assert two_sum_hash(data, target) is True


def test_two_sum_hash_invalid():
    data = [-2, 1, 2, 4, 7, 11]
    target = 100
    assert two_sum_hash(data, target) is False


def test_two_sum_valid():
    data = [-2, 1, 2, 4, 7, 11]
    target = 13
    assert two_sum(data, target) is True


def test_two_sum_invalid():
    data = [-2, 1, 2, 4, 7, 11]
    target = 100
    assert two_sum(data, target) is False
