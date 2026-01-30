from random import random

values = [random() for i in range(20)]
print(values)
x = random()

values.sort()
indexList = []

for i in range (0, len(values) - 1):
    if values[i] >= x:
        indexList.append(i)
    
print(values, x, indexList[0])