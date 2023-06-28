import os
os.chdir('C:\\Languages\\Python\\Chapter 9')
f = open('sample.txt')  
# reads 1st line
data = f.readline()
print(data)
# reads 2nd line
data = f.readline()
print(data)
# Reads 3rd line and so on...
data = f.readline()
print(data)

a = f.readlines()
print(a)
f.close()