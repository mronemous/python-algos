def optimize_boats(people: [int], limit: int) -> int:
    left: int = 0
    right: int = len(people)-1
    boats: int = 0

    while left <= right:
        if left == right:
            boats += 1
            break

        #can we pair them?
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats



