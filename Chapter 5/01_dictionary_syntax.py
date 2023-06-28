myDict = {
    "Fast": "In a quick manner",
    "Harry": "A coder",
    "Marks": [1, 2, 3],
    "Marks": [1, 2, 3],
    "anotherdict": {'harry': 'Player'},
    1: 2
}

# print(myDict['Fast'])
# print(myDict['Harry'])
# print(myDict['Marks'])
# print(myDict[1])
print(myDict['anotherdict']['harry'])

# properties:

# 1) It is unordered
# 2) It is mutable:
myDict['Marks'] = [45, 75]
print(myDict['Marks'])

