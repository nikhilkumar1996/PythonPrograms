"""
Program : There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
returned by Vending Machine. Write a Program to calculate the minimum number
of Notes as well as the Notes to be returned by the Vending Machine as a
Change
"""
import math


def vending_machine(amount):
    """
       Prints the least number of currency notes available for the given amount
       :param amount: Total Amount entered by the user.
       :return: Count of Notes for required change
    """

    list1 = [1000, 500, 100, 50, 10, 5, 2, 1]
    count = 0
    note = 0  # notes present in list1
    money = amount
    while amount > 1:
        if amount/list1[note] >= 1:
            a = amount/list1[note]
            print("{} {} Rupee Notes".format(math.floor(a), list1[note]))  # change of rupees
            amount = amount - math.floor(a) * list1[note]
            count = count + math.floor(a)  # store change of rupees

        else:
            note += 1

    return count


if __name__ == "__main__":
    cash = vending_machine(2000)
    print(cash)

