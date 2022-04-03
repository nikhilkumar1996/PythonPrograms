"""
Program 1: Write functions to return all permutations of a String using
Recursion method.
"""


def permutations(remaining, candidate=''):
    """
    Using Recursive function to generate all permutation  of a string
    :param remaining: input String
    :param candidate: empty string to add possible permutations
    :return: possible permutations
    """
    if len(remaining) == 0:
        print(candidate)

    for i in range(len(remaining)):
        new_candidate = candidate + remaining[i]  # current char in remaining gets added to the candidate
        new_remaining = remaining[0:i] + remaining[i + 1:]  # next remaining char adds to new_remaining

        permutations(new_remaining, new_candidate)


if __name__ == '__main__':
    string = 'abc'
    permutations(string)