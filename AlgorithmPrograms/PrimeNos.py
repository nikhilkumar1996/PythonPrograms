"""
Program 7 : Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
"""


def prime_numbers_range(lower, upper):
    """
    Prime numbers in a given range - lower to upper.
    :param lower: lower value of given range
    :param upper: upper value of given range
    :return: A list of prime numbers in given range
    """
    prime_nos = []
    # Traversing though the range
    for num in range(lower, upper + 1):
        # Checking if every number is divisible by their previous all the numbers
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_nos.append(num)
    return prime_nos


if __name__ == "__main__":
    low = 0
    high = 1000
    # print(prime_numbers_range(low, high))
    print(prime_numbers_range(low, high))



