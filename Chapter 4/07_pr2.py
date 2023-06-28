m1 = input("Enter the marks of student 1: ")
m2 = input("Enter the marks of student 2: ")
m3 = input("Enter the marks of student 3: ")
m4 = input("Enter the marks of student 4: ")
m5 = input("Enter the marks of student 5: ")
m6 = input("Enter the marks of student 6: ")

m1 = int(m1)
m2 = int(m2)
m3 = int(m3)
m4 = int(m4)
m5 = int(m5)
m6 = int(m6)


listOfMarks = [m1, m2, m3, m4, m5, m6]
listOfMarks.sort()
print(listOfMarks)