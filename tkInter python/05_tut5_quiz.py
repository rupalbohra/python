from tkinter import *
from PIL import Image, ImageTK
import os

root = Tk()
root.geometry("1200x1200")

photo1 = PhotoImage(file = "break up.png")
label1 = Label(image = photo1)
label1.pack()

dirs = os.listdir()
label2 = Label(text =dirs)
label2.pack()


root.mainloop()
