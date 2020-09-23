from pythonalgos.generators import BigFileReader


def test_basic():
    reader = BigFileReader("../tests/data/USCensus1990_sm.txt")
    reader.read()


def test_filter():
    reader = BigFileReader("../tests/data/USCensus1990_sm.txt", 0, "10004")
    reader.read()


def test_empty_file():
    reader = BigFileReader("../tests/data/USCensus1990_empty.txt")
    reader.read()


def test_no_file():
    reader = BigFileReader("../tests/data/USCensus1990_missing.txt")
    reader.read()


