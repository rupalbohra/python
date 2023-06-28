def m1():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\ACADEMIC.py").read())
def m2():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\HEALTH.py").read())
def m3():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\TASK.py").read())

import tkinter as tk
from tkinter import *
window=Tk()

lb_1=Label(window, text="HELP TO ACHIEVE YOUR DAILY GOALS AND PRESENT", fg='Black',font=("impack 25 bold"),bg='#89CFF0')
lb_1.place(x=60, y=50)

lb_1=Label(window, text="THERE FOR YOU EVERYTIME !", fg='Black',font=("impack 20 bold"),bg='#89CFF0')
lb_1.place(x=280, y=120)

button = Button(window, text="ACADEMIC MANAGER", fg="black",command=m1)
button.place(x=200, y=350)

button1 = Button(window, text="HEALTH MANAGER", fg="black",command=m2)
button1.place(x=460, y=350)

button2 = Button(window, text="TASK MANAGER", fg="black",command=m3)
button2.place(x=700, y=350)

window.configure(bg="#89CFF0")
window.title('YOUR COMPANION')

window.geometry("1000x600+10+10")

window.mainloop()



