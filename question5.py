import math

def circleAreaComparer(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0: # Validate both areas are positive
        print("One or both of the radii are negative and area cannot be calculated with a negative radius. Try again with positive numbers")

    else:
        areaOfCircle1 = math.pi * (radiusOfCircle1 ** 2) # Calculate each area
        areaOfCircle2 = math.pi * (radiusOfCircle2 ** 2)
        if areaOfCircle1 >= areaOfCircle2: # Return ratios of circles
            print("Circle 2 covers", (areaOfCircle2 / areaOfCircle1 * 100), "% of circle 1")
        else:
            print("Circle 1 covers", (areaOfCircle1 / areaOfCircle2 * 100), "% of circle 2")

circleAreaComparer(3, 7)
circleAreaComparer(-1, 4)
circleAreaComparer(2, 3)