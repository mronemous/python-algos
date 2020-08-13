def find_bad_version(versions: [int], is_bad_version):
    l: int = 0
    r: int = len(versions)-1
    bad: int = -1

    while l < r:
        mid = (r + l) // 2

        if is_bad_version(versions[mid]):
            r = mid
        else:
            l = mid + 1

    return l



