def reverse(input: str) -> str:
    # return input[::-1]

    result = ''
    for i in range(len(input), 0, -1):
        result += input[i - 1]
    return result
