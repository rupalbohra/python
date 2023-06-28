import os
os.chdir('C:\\Languages\\Python\\Chapter 9')

#  write mode:

# f = open('another.txt', 'w')
# f.write("Please write this to the file")
# f.write("Please write this to the file")  # this writes two times
# f.close()

#  append mode:

f = open('another.txt', 'a')
f.write("I am appending")  # the number of times you run the program, it gets printed.
f.close()

