threshold = 100
product = 1
currentNumber = 1

for i in range(1, threshold):
    currentNumber = i
    product = product * currentNumber
    if product > threshold:
        break

print("Product is ", product, "number that tipped it is ", currentNumber)