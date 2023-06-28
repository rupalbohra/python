def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)

a = int(input("Enter a positive integer:"))
sum(a)
print("The sum of first", a, "natural numbers is:", sum(a))
