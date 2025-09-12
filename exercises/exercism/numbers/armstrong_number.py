def is_armstrong_number(number: int) -> bool:
    return number == 0 or number == (sum(int(d)**len(str(number)) for d in str(number)))

print(is_armstrong_number(5))