from tkinter import*
import string
import random
import pyperclip

def generator():
    passwordField.delete(0,END)

    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    number=string.digits
    special_characters=string.punctuation

    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets, password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets+number, password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets+number+special_characters, password_length))

def copy(): 
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg="gray30")
choice=IntVar()
Font=('arial',12,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray30', fg='white')
passwordLabel.grid(pady=8)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice)
weakradioButton.grid(pady=4)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice)
mediumradioButton.grid(pady=4)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice)
strongradioButton.grid(pady=6)

lengthLabel=Label(root,text='Password Length',font=('Courier',16,'bold'),bg='gray30', fg='white')
lengthLabel.grid(pady=3)

length_Box = Spinbox(root,from_=6, to_=20,width=8,font=Font)
length_Box.grid(pady=3)

generateButton=Button(root, text='Generate',font=Font,command=generator)
generateButton.grid(pady=3)

passwordField=Entry(root,width=26,bd=1,font=Font)
passwordField.grid(pady=3)

coptButton=Button(root, text='Copy Password',font=Font,command=copy)
coptButton.grid(pady=3)


root.mainloop()