for i in range(10):
    print(i)
    if i == 5:
        break

else:
    print("Thes is inside else of for")
    # this else will print only after successful termination of loop. not after break
    # this is the difference in using else and break
    