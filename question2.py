strings = ["Data", "Science", "Python", "Programming", "Class"]
myDict = {}

for string in strings:
    myDict[string] = {
        "length": len(string),
        "parity": "even" if len(string) % 2 == 0 else "odd"
    }

print(myDict)