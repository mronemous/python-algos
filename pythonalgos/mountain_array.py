"""
Array must have length > 3
It must have increasing subarray followed by decreasing subarray.
"""
def is_mountain_array(data: [int]) -> bool:
    if len(data) < 3:
        return False

    i = 1
    #check for decreasing
    while i < len(data) and data[i] < data[i-1]:
        i += 1

    #check for increasing
    while i < len(data) and data[i] > data[i-1]:
        i += 1

    if i == 0 or i == len(data):
        i += 1

    #followed by decreasing
    while i < len(data) and data[i] < data[i-1]:
        i += 1

    return i == len(data)


