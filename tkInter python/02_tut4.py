from tkinter import *

root = Tk()

# width x height
root.geometry("400x400")

# width, height
root.minsize(200,100)
root.maxsize(500,500)


a = Label(text = "Rupal is a good girl and this is her GUI")
a.pack()

root.mainloop()

