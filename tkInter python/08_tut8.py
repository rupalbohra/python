from tkinter import *
root = Tk()

root.geometry("655x333")
f1 = Frame(root, bg= "grey", borderwidth = 6, relief = SUNKEN)
f1.pack(side = LEFT, fill = "y")

l = Label(f1, text = "Project Tkinter- Pycharm")
l.pack(pady = 42)

f2 = Frame(root, borderwidth = 8, bg = "grey", relief = SUNKEN)
f2.pack(side = TOP, fill = 'x')

l = Label(f2, text = "Welcome To Sublime Text", font = "Helvetica 12 bold")
l.pack(pady = 5)

root.mainloop()