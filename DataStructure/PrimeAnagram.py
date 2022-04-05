"""
Extend the Prime Number Program and store only the numbers in that range that are
Anagrams. For e.g. 17 and 71 are both Prime and Anagrams in the 0 to 1000 range.
Further store in a 2D Array the numbers that are Anagram and numbers that are not
Anagram
"""


def prime_list(num1, num2):
    list_ = []
    for i in range(num1, num2):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count >= 2:  # Not a PrimeNo
            continue
        if count < 2:  # PrimeNo
            list_.append(i)
    return list_


def anagram(num1, num2):
    list_ = []
    prime_ = prime_list(num1, num2)

    for i in range(len(prime_)):
        for j in range(i+1, len(prime_)):
            if sorted(str(prime_[i])) == sorted(str(prime_[j])):
                list_.append(prime_[i])
                list_.append(prime_[j])
    return list_


if __name__ == "__main__":
    array = []
    a = 1
    b = 100
    while b < 1000:
        out_list = anagram(a, b)
        array.append(out_list)
        a += 100
        b += 100

    print(array)