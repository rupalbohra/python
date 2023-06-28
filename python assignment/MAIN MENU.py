def m1():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\ACADEMIC.py").read())
def m2():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\HEALTH.py").read())
def m3():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\CALENDAR.py").read())

import tkinter as tk
from tkinter import *
window=Tk()

lb_1=Label(window, text="HELP TO ACHIEVE YOUR DAILY GOALS AND PRESENT THERE FOR YOU EVERYTIME ", fg='Black',font=("Comic Sans MS", 14),bg='#FEFBEA')
lb_1.place(x=120, y=50)

button = Button(window, text="ACADEMIC MANAGER", fg="blue",command=m1)
button.place(x=200, y=350)

button1 = Button(window, text="HEALTH MANAGER", fg="blue",command=m2)
button1.place(x=460, y=350)

button2 = Button(window, text="TASK MANAGER", fg="blue",command=m3)
button2.place(x=700, y=350)

window.configure(bg="#FEFBEA")
window.title('YOUR COMPANION')

window.geometry("1000x600+10+10")

window.mainloop()

#img = PhotoImage(file="C:\Users\Sunita Verma\Desktop\Python")
#ll1=Label(window,image=img)
#ll1.place(x=50,y=150)

