from tkinter import *

root = Tk()
root.geometry("655x333")

def hello():
    print("Hello Tkinter Button")

frame = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN)
frame.pack(side = LEFT, anchor = 'nw')

b1 = Button(frame, fg = "red", text = "print now", command = hello)
b1.pack(side = LEFT, padx = 10, pady = 10)

b2 = Button(frame, fg = "red", text = "print now")
b2.pack(side = LEFT, padx = 10, pady = 10)

b3 = Button(frame, fg = "red", text = "print now")
b3.pack(side = LEFT, padx = 10, pady = 10)

root.mainloop()