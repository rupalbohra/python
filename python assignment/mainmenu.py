# def m1():
#     exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\ACADEMIC.py").read())
# def m2():
#     exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\HEALTH.py").read())
# def m3():
#     exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\CALENDAR.py").read())

# import tkinter as tk
from tkinter import *
window=Tk()



photo = PhotoImage(file = "goals.png")
photo_label = Label(image = photo, padx = 10, pady = 10)
photo_label.place(x=100, y=120)

lb_1=Label(window, text="HELP TO ACHIEVE YOUR DAILY GOALS AND PRESENT THERE FOR YOU EVERYTIME ", fg='Black',font=("Comic Sans MS", 14),bg='#89CFF0')
lb_1.place(x=120, y=50)

# button = Button(window, text="ACADEMIC MANAGER", fg="blue")
# button.place(x=200, y=350)

# button1 = Button(window, text="HEALTH MANAGER", fg="blue")
# button1.place(x=460, y=350)

# button2 = Button(window, text="TASK MANAGER", fg="blue")
# button2.place(x=700, y=350)

window.configure(bg="#89CFF0")
window.title('YOUR COMPANION')

window.geometry("1000x600+10+10")

window.mainloop()


