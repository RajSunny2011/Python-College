from tkinter import *

root = Tk()

def click3():
    Label1=Label(root, text="YOU WILL PAY SOON", fg="red", bg='#000000')#fg- foreground(text), bg- background. can use hex codes or names to select colour
    Label1.pack()

#defining a button Button(<master widget>, <data>)
Button1 = Button(root, text='click here')
Button2 = Button(root, text="Can't click here", state=DISABLED)
Button3 = Button(root, text="DO NOT click this", command=click3)#If you put brackets after the func the program will call the func as soon as it gets to this line

Button1.pack()
Button2.pack()
Button3.pack()


root.mainloop()