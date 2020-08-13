from pythonalgos.binarysearch import binarysearch

def createBigData() -> [int]:
    data: [int] = []
    for i in range(0, 1000000):
        data.append(i)
    return data

def createData() -> [int]:
    return [1, 3, 5, 6, 7, 9, 13, 14, 16, 17]

def test_target_found():
    data: [int] = createData()
    assert binarysearch(data, 7) == 4

def test_target_notfound():
    data: [int] = createData()
    assert binarysearch(data, 1000) == -1

def test_performance():
    data: [] = createBigData()
    assert binarysearch(data, 7) == 7



