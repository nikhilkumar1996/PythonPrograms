
import math


def distance(coordinate1, coordinate2):
    """Progeam 3: Find Euclidean Distance """
    result = math.sqrt(math.pow(coordinate1, 2) + math.pow(coordinate2, 2))
    return result


if __name__ == '__main__':
    x = int(input("Enter Xcordinate value :"))
    y = int (input("Enter Ycoordinate value:"))
    print(distance(x, y))
