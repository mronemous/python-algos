def binarysearch(sortedData: [int], target: int) -> int:
    left: int = 0
    right: int = len(sortedData) - 1

    while left <= right:
        mid: int = (left + right) // 2

        if sortedData[mid] < target:
            left = mid + 1
        elif sortedData[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1
