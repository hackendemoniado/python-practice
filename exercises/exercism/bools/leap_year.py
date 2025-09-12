def leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(leap_year(1999))
print(leap_year(1997))
print(leap_year(2000))



