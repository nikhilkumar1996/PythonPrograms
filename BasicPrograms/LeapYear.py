def leap_year(year):
    """Program 3 : Find the leap Year with user input"""
    if year % 100 != 0 and year % 4 == 0:   # Condition to find a non century leap year
        print("{} is a leap year".format(year))
    elif year % 100 == 0 and year % 400 == 0:   # Condition to find a century leap year
        print("{} is century leap year".format(year))
    else:
        print("{} is not a leap year".format(year))


if __name__ == '__main__':
    input_year = int(input("Enter year :"))
    leap_year(input_year)