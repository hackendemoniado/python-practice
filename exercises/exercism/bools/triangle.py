def is_valid_triangle(sides: list[int]) -> bool:
    a, b,c = sorted(sides)
    return a > 0 and a + b > c

def equilateral(sides: list[int]) -> bool:
    a, b, c = sides
    return is_valid_triangle(sides=sides) and a == b == c


def isosceles(sides: list[int]) -> bool:
    a, b, c = sides
    return is_valid_triangle(sides=sides) and (a == b or b == c or a == c)


def scalene(sides: list[int]) -> bool:
    a, b, c = sides
    return is_valid_triangle(sides=sides) and (a != b and b != c and a != c)