pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

def computePower(pair):
    result = pair[0] ** pair[1]
    return result

resultList = []
for pair in pairs:
    if pair[1] < 0:
        continue
    resultList.append(computePower(pair))

print(resultList)
