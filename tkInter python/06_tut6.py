from textwrap import fill
from tkinter import *
root = Tk()
root.geometry("555x244")
root.title("My GUI With Harry")

# # Important Label Options
# text = adds the text
# bd or background = background
# fg = foreground
# font = sets the font
# type 1 = font=("Merriweather", 12, "bold")
# type 2 
# padx = x padding
# pady = y padding
# relief = border styling - SUNKIN, RAISED, GROOVE, RIDGE

title_label = Label(text = "Hey there this is me, Rupal", bg = "red", fg = "white", padx = 23, pady = 94, font="arial 12 bold", borderwidth = 5, relief=SUNKEN)

# Impoertant Pack Options
# anchor = North west, north east, etc
# side = top, bottom, left, right
# ###by default, the side is always top
# fill
# padx
# pady

title_label.pack(side = BOTTOM, anchor = "sw", fill = X, padx = 23, pady = 43)



root.mainloop()
