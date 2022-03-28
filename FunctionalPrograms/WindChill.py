import math


def temprature(temp, windspeed):
    """Program 5: Given the
    temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
    find WindChill:"""
    if temp < 50 and 3 < windspeed < 120:
        windchill = 35.75 + 0.6215 + (0.4275 * temp - 35.75) * math.pow(windspeed, 2)
        return "windchill=" + str(windchill)
    else:
        print("Cannot comply with temperature or windspeed values")
        return 0


if __name__ == '__main__':
    t = int(input("Enter temperature value:"))
    w = int(input("Enter windspeed value:"))
    print(temprature(t, w))

