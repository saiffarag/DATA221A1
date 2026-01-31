pairs = [[5, 2], [3, -1], [4, 3], [2, 0]] # List of test pairs

def computePower(x, y): # Compute power given x and y
    return x ** y

resultList = []
for x, y in pairs: # Unpack the pairs
    if y < 0: # Skip any pairs that have a negative y value
        continue
    resultList.append(computePower(x, y)) # Add valid results to the final list

print("The final result list is:", resultList)
