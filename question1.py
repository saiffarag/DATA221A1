threshold = 100 # Provided threshold we are using to test
product = 1 # Variable that holds our product
currentNumber = 1 # Variable that holds the current number we are multiplying by

for i in range(1, threshold): # Run a for loop that starts at 1 and increments by 1 multiplying it to our product
    currentNumber = i 
    product = product * currentNumber
    if product > threshold: # Break from the loop once threshold is exceeded
        break

print("The final product is", product, "and the number that tipped it over is ", currentNumber)