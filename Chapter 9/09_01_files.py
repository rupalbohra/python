import os
os.chdir('C:\\Languages\\Python\\Chapter 9')
# f = open('sample.txt', 'r')
# f = open('sample.txt', 'rt')  #rt=read in text mode
f = open('sample.txt')   # By default the mode is r and text form is read
# data = f.read()
data = f.read(5)   #reads 1st 5 characters
print(data)
f.close()