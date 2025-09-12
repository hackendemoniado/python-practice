def steps(number: int) -> int:
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:
        number = number // 2 if number %2 == 0 else number * 3 + 1
        steps += 1
    return steps

print(steps(12))