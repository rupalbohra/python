# Concatinating two strings


# greeting = "Good morning"
# name = " Harry"
# c = greeting + name
# print(c)




name = "Harry"
print(name[0])  # Indexing starts from 0 i.e. 0 --> H, 1 --> A, and so on...
# name[3] = d  --> doesn't work. We can just assess the value of string but cannot change it.

#String slicing: A string in python can be sliced for getting a part of the string.

# print(name[0:3])  # --> i.e. 0 to 2, 3 would be excluded.
# print(name[:4])   --> it is same as name[0:4]
# print(name[0:])   --> this will give entire length. same as name[0:5]
# print(name[0:5])

print(name[-4:-1])   #same as name[0:4]

#reverse of the string:
print(name[::-1])