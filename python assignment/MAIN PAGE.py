def m1():
    exec(open("C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\HOMEPAGE.py").read())
import tkinter as tk
from tkinter import *
window=Tk()

button = Button(window, text="MAIN MENU !", fg="blue",command=m1)
button.place(x=460, y=500)

lb_1=Label(window, text="YOUR COMPANION :)", fg='Black',font=("Comic Sans MS", 44),bg='#FEFBEA')
lb_1.place(x=225, y=50)
lb2=Label(window, text="There for You Everytime", fg='black',font=("Helvetica 23 underline"),bg='#FEFBEA')
lb2.place(x=350, y=150)
lb3=Label(window, text="", fg='red',font=("Comic Sans MS", 24),bg='#FEFBEA')
lb3.place(x=145, y=150)

'''img = PhotoImage(file='LOGO.png')
Label( 
    window,
    image=img
).pack()'''

window.configure(bg="#FEFBEA")
window.title('YOUR COMPANION')

window.geometry("1000x600+10+10")

window.mainloop()

img = '''PhotoImage(file="C:\\Users\\sanya\\Desktop\\Python\\Your Companion\\LOGO.png")
ll1=Label(window,image=img)
ll1.place(x=50,y=150)'''

