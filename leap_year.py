def leap_year(year):
    if year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a leap year"


y = int(input("Enter the year: "))
print(leap_year(y))
