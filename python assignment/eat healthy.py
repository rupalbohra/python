from tkinter import *
import webbrowser

def reset_entry():
    name_tf.delete(0,'end')
    age_tf.delete(0, 'end')


def eat_healthy():
    root = Tk()
    new = 1
    url = "https://www.heartandstroke.ca/healthy-living/healthy-eating/healthy-eating-basics"
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

text = Label(f1, text = '''BE A PART OF  
A HEALTHY WORLD''', font = "Helvetica 20 bold")
text.pack(padx = 5, pady = 5)


var = StringVar()

frame = Frame(
    ws,
    padx=60,
    pady= 60
)
frame.pack(fill = Y)


name_lb = Label(
    frame,
    text="Enter Your Name",
    font = "Merriweather 10 bold"
)
name_lb.grid(row=1, column=7)

name_tf = Entry(
    frame, 
)
name_tf.grid(row=1, column=9, pady=5)


age_lb = Label(
    frame,
    text="Enter Your Age",
    font = "Merriweather 10 bold"
)
age_lb.grid(row=3, column=7)

age_tf = Entry(
    frame,
)
age_tf.grid(row=3, column=9, pady=5)




fit_lb = Label(
    frame,
    text='Do you wanna get fit?',
    font = "Merriweather 10 bold"    
)
fit_lb.grid(row=2, column=7)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=9, pady=5)

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
frame3.grid(row=5, columnspan=13, pady=10)

lab_btn = Button(
    frame3,
    text='Get healthy eating habits',
    font = "Merriweather 8 bold",
    command=eat_healthy
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
