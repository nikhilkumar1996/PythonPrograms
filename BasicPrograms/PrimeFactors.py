def prime_factor(number):
    """Program 6:  Find Prime Factors """
    divisor = 2
    num = number
    while num > 1:
        if num % divisor == 0:
            print("Prime Factors of {}={}".format(number, divisor))
            num = num / divisor
            continue
        else:
            divisor += 1


if __name__ == '__main__':
    user_input = int(input("Enter number:"))
    prime_factor(user_input)