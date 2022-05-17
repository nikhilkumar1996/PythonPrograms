def harmonic_number(number):
    """Program 5: Find Harmonic Number
     [1/n]+[1/(n+1)]+[1/(n+2)]........."""
    inital = 1
    sum = 0

    while inital < number:
        print("1/{} +".format(inital), end=" ")
        sum += 1 / inital
        inital += 1
    print("1/{}={}".format(inital, sum))


if __name__ == '__main__':
    num = int(input("Enter range of numbers"))
    harmonic_number(num)