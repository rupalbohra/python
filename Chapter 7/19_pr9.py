n = int(input("Enter any number: "))


print(" *" * n)
a = " "* ((2*n)-4)
for i in range(1, ((n-2)+1)):
    print(f" * {a}*")

print(" *" * n)    
    