
# the best way to open and close a file is with statement. Here we do not need to close the file once opened.

import os
os.chdir('C:\\Languages\\Python\\Chapter 9')
with open("another.txt", "r") as f:
    a = f.read()
    print(a)

with open("another.txt", "w") as f:
    a = f.write("me")
    print(a)
