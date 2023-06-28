def m1():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\MAIN_MENU.py").read())
import tkinter as tk
from tkinter import *
window=Tk()

photo = PhotoImage(file = "LOGO.png")
photo_label = Label(image = photo, relief=SUNKEN)
photo_label.place(x=350, y=200)

button = Button(window, text="MAIN MENU !", fg="black",command=m1)
button.place(x=478, y=520)

lb_1=Label(window, text="YOUR COMPANION :)", fg='black',font=("Comic Sans MS", 44),bg='#89CFF0')
lb_1.place(x=225, y=50)
lb2=Label(window, text="There for You Everytime", fg='black',font=("Helvetica 23 underline"),bg='#89CFF0')
lb2.place(x=350, y=150)


window.configure(bg="#89CFF0")
window.title('YOUR COMPANION')

window.geometry("1000x600+10+10")

window.mainloop()



