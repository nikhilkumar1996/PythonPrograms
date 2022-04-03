"""
Program : Create temperatureConversion static function, given the temperature
in fahrenheit as input outputs the temperature in Celsius or vice versa using the
formula
"""


def temp_conversion(celsius, fahrenheit):
    """
    :param celsius: Temperature in celsius
    :param fahrenheit: Temperature in fahrenheit
    :return: conversion of cel -->fah and fah --> cel
    """
    cel_to_fah = (celsius * 9 / 5) + 32
    fah_to_cel = (fahrenheit - 32) * 5 / 9
    return round(cel_to_fah, 3), round(fah_to_cel, 3)


if __name__ == "__main__":
    degrees = temp_conversion(40.5, 66.3)
    print(degrees)
