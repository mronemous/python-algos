from pythonalgos.fizzbuzz import fizzbuzz


def test_multiple_of_3():
    assert fizzbuzz(3) == "Fizz"


def test_multiple_of_5():
    assert fizzbuzz(5) == "Buzz"


def test_multiple_of_15():
    assert fizzbuzz(30) == "FizzBuzz"


def test_zero():
    assert fizzbuzz(0) == "0"


def test_negative_multiple_of_3():
    assert fizzbuzz(-9) == "Fizz"


def test_pass_value():
    assert fizzbuzz(4) == "4"
