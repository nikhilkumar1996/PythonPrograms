import time
"""
Program 3:Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
"""


def stopwatch_calculation(start_time, end_time):
    """
    Returns elapsed time between start time and end time provided by user
    :param start_time: Start time provided by user
    :param end_time: End time provided by user
    :return : End time minus start time rounded to seconds
    """

    #  Measuring the elapsed time between start and end
    time_elapsed = end_time - start_time
    return round(time_elapsed, 4)


if __name__ == "__main__":
    start = input("Press Enter to Start")
    start = time.time()
    end = input("Press Enter to Stop")
    end = time.time()
    elapsed_time = stopwatch_calculation(start, end)
    print(elapsed_time, " seconds")