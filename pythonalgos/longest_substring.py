def length_of_longest_substring(s: str):
    length: int = 0
    last_index = {}
    n: int = len(s)
    l: int = 0
    r: int = 0

    while l < n and r < n:
        c = s[r]
        if c in last_index:
            l = max(l, last_index[c] + 1)
        last_index[c] = r
        length = max(length, r - l + 1)
        r += 1

    # i: int = 0
    # for j, value in enumerate(s):
    #     if value in last_index:
    #         i = max(last_index[value], i)
    #     length = max(length, j - i + 1)
    #     last_index[value] = j + 1

    return length
