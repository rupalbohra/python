dict = {
    "billi": "Cat",
    "kutta": "Dog",
    "haath": "Hand",
    "baal": "Hair",
}
print("Options are:", dict.keys())
a = input("Enter the Hindi word:")
# print("The meaning of your word is :", dict[a])

# The below key will not give error if the key is not present in the dictionary
print("The meaning of your word is :", dict.get(a))