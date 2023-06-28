def table(n):
    for i in range(1, 11):
        print(n, "X", i, "=", n*i)
    return 0

n = int(input("Enter number: "))
table(n)
