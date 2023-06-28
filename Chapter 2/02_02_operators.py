# In python the output of operations done in integers or float is always a float

a = 3
b = 4

print("The value of 3+4 is", 3+4)
print("The value of 3-4 is", 3-4)
print("The value of 3*4 is", 3*4)
print("The value of 3/4 is", 3/4)

# Assignment operators

a = 34
a *= 12
a -= 12     # this will give the value of a + 2
a /= 12
print(a)

# Comparison operator

# b = (4>7)
# b = (4<=7)
# b = (4!=7)
b = (4==7)
print(b)

# Logical operators

bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))
