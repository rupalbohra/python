def temp(cel):
    return ((9/5)*cel) + 32

cel = eval(input("Enter temperature in celcius: "))
temp(cel)
print("Temperature in fahrenhiet is:", temp(cel))