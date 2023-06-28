myDict = {
    "fast": "In a quick manner",
    "harry": "A coder",
    "marks": [1, 2, 3],
    "marks": [1, 2, 3],
    "anotherdict": {'harry': 'Player'},
    1: 2
}

#  Dictionary Methods:
print(myDict.keys())    # --> prints the keys of dictionary
print(list(myDict.keys()))  

print(myDict.values())  # --> prints the values of dictionary
print(list(myDict.values()))  

print(myDict.items())   # --> prints the (key, value) for all contents of dictionary
print(list(myDict.items()))  


updateDict = {              # --> adds new item in the dictionary
    "Lovish": "Friend",     # --> adds new item in the dictionary
    "harry": "A Dancer"     # --> changes the value of pre-existing
}                               # item in the dictionary

print(myDict) 
myDict.update(updateDict)
print(myDict)

print(myDict.get("harry2"))  # --> Returns none if the word is not found in myDict 
# print(myDict['harry2'])      # --> gives error

# --> therefore get is preffered


# There are many other methods of dictionary. YOu can get them on python.org