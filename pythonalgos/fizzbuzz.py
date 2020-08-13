def fizzbuzz(number: int) -> str:
    result: str = None

    if number == 0:
        result = str(number)
    elif number % 3 == 0 and number % 5 == 0:
        result = "FizzBuzz"
    elif number % 3 == 0:
        result = "Fizz"
    elif number % 5 == 0:
        result = "Buzz"
    else:
        result = str(number)

    return result
