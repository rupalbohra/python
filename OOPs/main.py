class Employee:

    increment = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

harry = Employee('harry', 'jackson', 44000)
rohan = Employee('rohan', 'das', 44000)


print(harry.fname, rohan.fname)