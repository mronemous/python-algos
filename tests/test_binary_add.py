from pythonalgos.binary_add import binary_add

def test_carry_over_end():
    assert binary_add(a = "1010", b = "1011") == "10101"

def test_b_shorter():
    assert binary_add(a = "11", b = "1") == "100"

def test_a_shorter():
    assert binary_add(a = "1", b = "11") == "100"