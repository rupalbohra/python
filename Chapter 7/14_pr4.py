num = int(input("Enter any number: "))
prime = True
for i in range(2, num):
    if(num % i == 0):
        prime = False
        break

if prime == True:
    print("This number is prime")
else:
    print("This number is not prime")