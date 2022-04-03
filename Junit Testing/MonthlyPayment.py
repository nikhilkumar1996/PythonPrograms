"""
Program : calculate monthlyPayment that reads in three
command-line arguments P, Y, and R and calculates the monthly payments you
would have to make over Y years to pay off a P principal loan amount at R per cent
interest compounded monthly.
"""
import math


def monthly_payment(principal_loan, year, rate):
    """
    :param principal_loan: Loan took by person
    :param year: Duration of years for paying loan amount
    :param rate: rate percent Interest
    :return: payment required to pay monthly
    """
    n = 12 * year
    r = rate/(12 * 100)
    payment = (principal_loan * r) / 1 - math.pow((1 + r), -n)  # Formula
    return round(payment, 3)


if __name__ == "__main__":
    amount_required = monthly_payment(30000, 4, 5)
    print(amount_required)

