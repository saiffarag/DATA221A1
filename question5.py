import math

def circleAreaComparer(radius1, radius2):
    if radius1 <= 0 or radius2 <= 0:
        print("Error Message")

    else:
        area1 = math.pi * (radius1 ** 2)
        area2 = math.pi * (radius2 ** 2)
        print(min(area1, area2) / max(area1, area2) * 100)

circleAreaComparer(3, 7)
circleAreaComparer(-1, 4)
circleAreaComparer(2, 3)