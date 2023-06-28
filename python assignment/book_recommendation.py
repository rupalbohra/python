from tkinter import *
from tkinter import messagebox
import webbrowser

def reset_entry():
    name_tf.delete(0,'end')
    rollnumber_tf.delete(0,'end')
    course_tf.delete(0,'end')

def select_course():
    course = str(course_tf.get())
    bmi_index(course)

def bmi_index(course):
    
    if course == "BTech":
        root = Tk()
        root.geometry("300x100")
        new = 1
        url = "https://www.ncertbooks.guru/b-tech-books/"
        def openweb():
            webbrowser.open(url,new=new)
        Btn = Button(root, text = "Know recommendations", bg = '#1E90FF', fg = 'white',command=openweb)
        Btn.place(x = 20, y = 20 )
        root.mainloop()

    elif course == "BBA":
        root = Tk()
        new = 1
        url = "https://www.ncertbooks.guru/bba-books/"
        def openweb():
            webbrowser.open(url,new=new)
        Btn = Button(root, text = "Know recommendations", bg = '#1E90FF', fg = 'white',command=openweb)
        Btn.pack(padx = 15, pady = 30)
        root.mainloop()
        
    elif course == "BCom":
        root = Tk()
        new = 1
        url = "https://www.ncertbooks.guru/b-com-reference-books/"
        def openweb():
            webbrowser.open(url,new=new)
        Btn = Button(root, text = "Know recommendations", bg = '#1E90FF', fg = 'white',command=openweb)
        Btn.pack(padx = 15, pady = 30)
        root.mainloop()

    elif course == "BSc":
        root = Tk()
        new = 1
        url = "https://www.ncertbooks.guru/b-sc-books/"
        def openweb():
            webbrowser.open(url,new=new)
        Btn = Button(root, text = "Know recommendations", bg = '#1E90FF', fg = 'white',command=openweb)
        Btn.pack(padx = 15, pady = 30)
        root.mainloop()

    elif course == "LLB":
        root = Tk()
        new = 1
        url = "https://www.ncertbooks.guru/llb-books/"
        def openweb():
            webbrowser.open(url,new=new)
        Btn = Button(root, text = "Know recommendations", bg = '#1E90FF', fg = 'white',command=openweb)
        Btn.pack(padx = 15, pady = 30)
        root.mainloop()

    else:
        messagebox.showerror('BMI-Your Companion', 'something went wrong!')   

ws = Tk()
ws.title('Your Companion')
ws.geometry('600x400')
ws.config(bg='#1E90FF')

f1 = Frame(ws, borderwidth = 9, bg = "white", relief=SUNKEN)
f1.pack(padx = 5, pady = 5)

text = Label(f1, text = '''Get best eBook recommendations 
for your course''', font = "Helvetica 20 bold")
text.pack(padx = 5, pady = 5)

var = StringVar()

frame = Frame(
    ws,
    padx=60, 
    pady=60
)
frame.pack(expand=True)


name_lb = Label(
    frame,
    text="Enter Your Name",
    font = "Merriweather 10 bold"
)
name_lb.grid(row=1, column=1)

name_tf = Entry(
    frame, 
)
name_tf.grid(row=1, column=2, pady=5)


rollnumber_lb = Label(
    frame,
    text="Enter Your Roll Number",
    font = "Merriweather 10 bold"
)
rollnumber_lb.grid(row=3, column=1)

rollnumber_tf = Entry(
    frame,
)
rollnumber_tf.grid(row=3, column=2, pady=5)

course_lb = Label(
    frame,
    text='''Enter Your Course - Case Sensitive
    (Choose from BTech, BBA, LLB, BCom, BSc)''',
    font = "Merriweather 10 bold"

)
course_lb.grid(row=4, column=1)


course_tf = Entry(
    frame,
)
course_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

books_btn = Button(
    frame3,
    text='Show recommendations',
    font = "Merriweather 8 bold",
    command=select_course
)
books_btn.pack(side=LEFT)

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
