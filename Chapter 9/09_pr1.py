import os
os.chdir('C:\\Languages\\Python\\Chapter 9')

f = open("poems.txt")
t = f.read()
    
if 'Twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
# f.close()