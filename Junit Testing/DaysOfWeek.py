"""
Program : Create dayOfWeek static function that takes a date as input and
prints the day of the week that date falls on.
"""
import math


def day_of_week(m, d, y):
    """
    :param m: month
    :param d: date
    :param y: year
    :return:  day of week
    """
    list1 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    y0 = y - (14 - m) / 12  # year
    x = y0 + y0 / 4 - y0 / 100 + y0 / 400
    m0 = m + 12 * ((14 - m) / 12) - 2  # month
    d0 = (d + x + 31 * m0 / 12) % 7  # day

    return list1[math.floor(d0)]


if __name__ == "__main__":
    date = day_of_week(3, 29, 2022)
    print(date)