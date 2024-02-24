import math
def area_of_polygon():
    x = int(input())
    y = int(input())
    area = (x * (pow(y, 2)) / (4 * math.tan(math.pi / x)))
    print(math.floor(area))  #math.floor -> rounds a number down to the nearest integer


area_of_polygon()
