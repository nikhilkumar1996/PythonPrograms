import pytest

import BinaryNo
import MonthlyPayment
import SquareRoot
import TempConversion
import VendingMachine
import DaysOfWeek


def test_cal_vending_machine():
    """
    verify the output of vending_machine function
    :return: 2 {NoOfNotes}
    """
    output = VendingMachine.vending_machine(2000)
    expected = 2
    assert output == expected


def test_cal_days_of_week():
    """
    verify the output of day_of_week function
    :return: day of week
    """
    output = DaysOfWeek.day_of_week(3, 29, 2022)
    expected = "Tuesday"
    assert output == expected


def test_cal_temp_conversion():
    """
    verify the output of temp_conversion function
    :return: (104.9, 19.056) {cel_to_fah , fah_to_cel}
    """
    output = TempConversion.temp_conversion(40.5, 66.3)
    expected = 104.9, 19.056
    assert output == expected


def test_cal_monthly_payment():
    """
    verify the output of monthly_payment function
    :return: payment interest
    """
    output = MonthlyPayment.monthly_payment(30000, 4, 5)
    expected = 124.181
    assert output == expected


def test_cal_square_root():
    """
    Verify the output of square_root function
    :return: square_root of number
    """
    output = SquareRoot.square_root(250)
    expected = 15.811
    assert output == expected


@pytest.mark.parametrize("param, expected", [(25.75, [1, 0, 0, 1, 1])])
def test_cal_binary_no(param, expected):
    """
    verify the output of to_binary function
    :return: binary number of a decimal number
    """
    output = BinaryNo.to_binary(param)
    assert output == expected


