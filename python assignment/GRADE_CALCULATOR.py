from tkinter import *
screen = Tk()
screen.geometry("400x480")
def calculate():
    computerscience_marks = int(computerscience_entry.get())
    mathematics_marks = int(mathematics_entry.get())
    physics_marks = int(physics_entry.get())
    lifeskills_marks = int(lifeskills_entry.get())
    biology_marks = int(biology_entry.get())
    total = (computerscience_marks + mathematics_marks + physics_marks + lifeskills_marks + biology_marks)
    average = int(total/5)
    Label(screen, text = total, font = "impack 15 bold").place(x=175,y=255)
    Label(screen, text = average, font = "impack 15 bold").place(x=175,y=285)
    if average>40:
        grade = "PASS"
    else:
        grade = "FAIL"
    Label(screen, text = grade, font = "impack 15 bold").place(x=175,y=315)
Label(screen, text = "Grade Calculator", font = "impack 28 bold", bg = "black", fg = "white").pack(fill=X)
Label(screen, text = "Computer Science", font = "impack 14").place(x=30, y=70)
Label(screen, text = "Mathematics", font = "impack 14").place(x=30, y=105)
Label(screen, text = "Physics", font = "impack 14").place(x=30, y=140)
Label(screen, text = "Life Skills", font = "impack 14").place(x=30, y=175)
Label(screen, text = "Biology", font = "impack 14").place(x=30, y=210)
Label(screen, text = "Total", font = "impack 15 bold").place(x=30, y=255)
Label(screen, text = "Average", font = "impack 15 bold").place(x=30, y=285)
Label(screen, text = "Grade", font = "impack 15 bold").place(x=30, y=315)
computerscience_entry = Entry(screen, font = "20", width = 15, bd = 2)
computerscience_entry.place(x=220,y=70)
mathematics_entry = Entry(screen, font = "20", width = 15, bd = 2)
mathematics_entry.place(x=220,y=105)
physics_entry = Entry(screen, font = "20", width = 15, bd = 2)
physics_entry.place(x=220,y=140)
lifeskills_entry = Entry(screen, font = "20", width = 15, bd = 2)
lifeskills_entry.place(x=220,y=175)
biology_entry = Entry(screen, font = "20", width = 15, bd = 2)
biology_entry.place(x=220,y=210)
Button(screen, text = "Calculate", font = "impack 15 bold", bg = "light blue", command = calculate).place(x=80,y=380)
Button(screen, text = "Exit", font = "impack 15 bold", bg = "red", fg = "white", width = 8, command = lambda:exit()).place(x=210,y=380)


mainloop()
