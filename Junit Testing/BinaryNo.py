"""
Write a function toBinary that outputs the binary (base 2) representation of
the decimal number typed as the input.
"""
import math


def to_binary(number):
    """
    :param number: A decimal Number
    :return: Convert decimal to Binary No
    """
    binary_no = []
    count = 0
    while number > 0:
        binary_no.append(math.floor(number % 2))  # list stores binary_no
        number = math.floor(number / 2)  # reduce number by division
        count += 1

    for data in binary_no:
        print(data)  # Display elements in List

    return binary_no


if __name__ == "__main__":
    binary = to_binary(25.75)
    print(binary)

