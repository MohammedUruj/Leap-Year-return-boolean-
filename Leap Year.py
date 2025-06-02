def is_leap_year(year):
    # Write your code here.
    if year % 4 != 0:
        return False
    elif year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    # Don't change the function name.
leap=int(input("Please enter the year to find out the leap"))
is_leap_year(leap)