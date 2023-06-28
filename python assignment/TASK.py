def m1():
    import NOTEPAD
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\NOTEPAD.py").read())
def m2():
    import ALARM_CLOCK
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\ALARM_CLOCK.py").read())
def m3():
    import CALENDAR
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\CALENDAR.py").read())
def m4():
    import TO_DO_LIST
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\TO_DO_LIST.py").read())
def m5():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\MAIN_MENU.py").read())
    

import tkinter as tk
from tkinter import *
window=Tk()

lb_1=Label(window, text="WELCOME TO YOUR", fg='Black', font=("Comic Sans MS bold",20),bg="#89CFF0")
lb_1.place(x=325,y=50)

lb_1=Label(window, text="TASK MANAGER !", fg='Black', font=("Comic Sans MS bold",28),bg="#89CFF0")
lb_1.place(x=300,y=100)


button = Button(window, text="NOTEPAD", fg="Black",command=m1)
button.place(x=210, y=350)

button1 = Button(window, text="ALARM CLOCK", fg="Black",command=m2)
button1.place(x=200, y=450)

button2 = Button(window, text="CALENDAR", fg="Black",command=m3)
button2.place(x=650, y=450)

button3 = Button(window, text="TO DO LIST", fg="Black",command=m4)
button3.place(x=650, y=350)

button4 = Button(window, text="GO TO MAIN MENU", fg="Black",command=m5)
button4.place(x=425, y=525)

window.configure(bg="#89CFF0")
window.title('YOUR COMPANION')

window.geometry("1000x600+10+10")

window.mainloop()
