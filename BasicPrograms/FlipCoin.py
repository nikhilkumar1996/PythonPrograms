import random


def coinflip(flips):
    """Program 2 : Flip a coin using Random function and find percentage of Heads and Tails"""
    head = 0
    tail = 0
    num = 0.5
    for count in range(1, flips+1):
        rand = random.random()
        if rand < num:
            tail += 1
        else:
            head += 1
    print("No of Heads=", head)
    print("No of Tails=", tail)

    headpercentage = (head * 100)/flips
    tailpercentage = (tail * 100)/flips
    print("Heads Percenatge=", headpercentage)
    print("Tails Percentage=", tailpercentage)


if __name__ == '__main__':
    flipcount = int(input("Enter no of coin flips"))
    coinflip(flipcount)