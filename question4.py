from random import random

values = [random() for i in range(20)]
x = random()

values.sort() # Sort the list of numbers
indicesGreaterThanX = [] # Create list for indices of values greater than x

for i in range (len(values)): # Loop through values and add indices of values greater than x
    if values[i] >= x:
        indicesGreaterThanX.append(i)
if indicesGreaterThanX:
    firstIndex = indicesGreaterThanX[0]
else:
    firstIndex = None
    
print("The Sorted List of random numbers is:", values, ", The x value is:", x, ", The first matching index is:", firstIndex)