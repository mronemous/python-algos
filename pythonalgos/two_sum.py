"""
Time O(N^2)
Space O(1)
"""


def two_sum_brute_force(data: [int], target: int) -> bool:
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            a = data[i]
            b = data[j]
            # print("{0} {1},".format(a, b))

            if a + b == target:
                print("{0} + {1} = {2}".format(a, b, target))
                return True
    return False


"""
Time O(N)
Space O(N)
"""


def two_sum_hash(data: [int], target: int) -> bool:
    pairs = dict()

    for i in range(len(data)):
        value = data[i]
        if value in pairs:
            print("{0} + {1} = {2}".format(value, pairs[value], target))
            return True
        else:
            pairs[target - value] = value
    return False


"""
Requires the numbers be sorted.

Time O(N)
Space O(1)
"""


def two_sum(data: [int], target: int) -> bool:
    i: int = 0
    j: int = len(data) - 1

    while i <= j:
        a = data[i]
        b = data[j]
        if a + b == target:
            print("{0} + {1} = {2}".format(a, b, target))
            return True
        elif a + b < target:
            i += 1
        else:
            j -= 1
    return False
