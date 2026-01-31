strings = ["Data", "Science", "Python", "Programming", "Class"] # List of test strings
length_and_parityDict = {} # Create dictionary

for string in strings: # for each string in the list, set the string as the key and its value to its length and parity
    length_and_parityDict[string] = {
        "length": len(string),
        "parity": "even" if len(string) % 2 == 0 else "odd"
    }

print(length_and_parityDict) # Return final dictionary