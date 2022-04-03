"""
Program 10 : Takes a command-line argument N, asks you to think of a number
between 0 and N-1, where N = 2^n, and always guesses the answer with n
questions.
"""


def binary_guess(_limit):
    """
    Uses Binary search to get the number guessed by the user.
    :param _limit: Number from 0 till which user has to guess the number.
    :return: Number guessed by the user.
    """
    lower_limit = 0
    higher_limit = _limit
    while lower_limit != higher_limit:
        mid_value = (lower_limit + higher_limit) // 2
        print("Enter 1 if number is between ", lower_limit, " - ", mid_value,
              "\n Enter 2 if number is between ", (mid_value + 1), " - ", higher_limit)
        choice = int(input())
        if choice == 1:
            higher_limit = mid_value
        else:
            lower_limit = mid_value + 1
    return lower_limit


if __name__ == "__main__":
    limit = int(input("Enter a number: "))
    print("The number you guessed is ", binary_guess(limit))