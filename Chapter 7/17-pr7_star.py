n = int(input("Enter the height: "))

for i in range(n):
    print(" " * (n-i-1), "*" * ((2*i)+1), " " * (n-i-1))
    