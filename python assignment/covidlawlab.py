from tkinter import *
import webbrowser

def reset_entry():
    name_tf.delete(0,'end')


def go_to_lab():
    root = Tk()
    new = 1
    url = "https://covidlawlab.org/"
    def openweb():
        webbrowser.open(url,new=new)
    Btn = Button(root, text = "Continue",command=openweb)
    Btn.pack()
    root.mainloop()
        
    
ws = Tk()
ws.title('Your Companion')
ws.geometry('1000x600+10+10')
ws.config(bg='#1E90FF')

f1 = Frame(ws, borderwidth = 9, bg = "white", relief=SUNKEN)
f1.pack(padx = 5, pady = 100)

text = Label(f1, text = '''WELCOME! GET A DIRECT LINK TO 
THE COVID LAW LAB''', font = "Helvetica 20 bold")
text.pack(padx = 5, pady = 5)


var = StringVar()

frame = Frame(
    ws,
    padx=60,
    pady= 60
)
frame.pack(expand=True)


name_lb = Label(
    frame,
    text="Enter your name",
    font = "Merriweather 10 bold"
)
name_lb.grid(row=1, column=1)

name_tf = Entry(
    frame, 
)
name_tf.grid(row=1, column=2, pady=5)

covid_lb = Label(
    frame,
    text='Are you vaccinated?',
    font = "Merriweather 10 bold"    
)
covid_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

yes_rb = Radiobutton(
    frame2,
    text = 'Yes',
    variable = var,
    value = 1
)
yes_rb.pack(side=LEFT)

no_rb = Radiobutton(
    frame2,
    text = 'No',
    variable = var,
    value = 2
)
no_rb.pack(side=RIGHT)


frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

lab_btn = Button(
    frame3,
    text='Go to the Covid Law Lab',
    font = "Merriweather 8 bold",
    command=go_to_lab
)
lab_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    font = "Merriweather 8 bold",
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    font = "Merriweather 8 bold",
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
