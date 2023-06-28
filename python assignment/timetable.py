
# Take n greater than 0.25 and less than 5
same=True
n=0.3

# Adding a background image
background_image =Image.open("library.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="Welcome to RCPL Library", fg='black')
headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

btn1 = Button(root,text="Employee",bg='black', fg='white', command=Employee)
btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Student",bg='black', fg='white', command=Student)
btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)
