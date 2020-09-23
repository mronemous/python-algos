def get_value(digits: str, i: int):
    return int(digits[i])


def binary_add(a: str, b: str) -> str:
    # zero pad to line up
    maxLen: int = max(len(a), len(b))
    a = a.rjust(maxLen, '0')
    b = b.rjust(maxLen, '0')

    result: [int] = [0] * maxLen
    carry: int = 0

    for i in range(maxLen - 1, -1, -1):
        bit_a = get_value(a, i)
        bit_b = get_value(b, i)

        sum = bit_a + bit_b + carry
        if sum == 3:
            result[i] = 1
            carry = 1
        elif sum == 2:
            result[i] = 0
            carry = 1
        elif sum == 1:
            result[i] = 1
            carry = 0
        elif sum == 0:
            result[i] = 0
            carry = 0

    if carry == 1:
        result.insert(0, 1)

    return ''.join(map(str, result))
