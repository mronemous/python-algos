phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}

def backtrack(combo: str, next_digits: [str], result: [str]):

    if len(next_digits) == 0:
        result.append(combo)
    else:
        for letter in phone[next_digits[0]]:
            backtrack(combo + letter, next_digits[1:], result)

def letter_combo_phone_number(digits: str) -> [str]:

    result = []
    if digits:
        backtrack("", digits, result)

    return result

