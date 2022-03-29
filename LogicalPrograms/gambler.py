import random
""" Program 1: Simulates a gambler who start with $stake and place fair $1 bets until
    he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
    times he/she wins and the number of bets he/she makes. Run the experiment N
    times, averages the results, and prints them out.
"""


def gamble(stake, goal, number_of_trails):
    """
    :param stake: Amount of $money Person has to bet in game
    :param goal: Desired Price Money by Person
    :param number_of_trails: Total number of times User can bet in game
    :return: Winning percentage and losing percentage
    """

    win = 0
    loss = 0
    win_count = 1
    while win + loss < number_of_trails and 0 < stake < goal:
        result = random.randint(1, 2)
        if result == win_count:
            win += 1
            stake += 1
        else:
            loss += 1
            stake -= 1

    if win + loss == number_of_trails:
        print("out of trails")

    elif stake == goal:
        print("Goal reached")

    win_percentage = (win * 100)/number_of_trails
    loss_percentage = (loss * 100)/number_of_trails
    return "win_percentage =" + str(win_percentage)+"\t" + "loss_percentage =" + str(loss_percentage)


if __name__ == "__main__":
    g = gamble(40, 100, 15)
    print(g)







