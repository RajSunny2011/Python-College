from tkinter import *

root = Tk()

def click1():
    Label1=Label(root, text='Hello '+e.get(), fg="red", bg='#000000')#fg- foreground(text), bg- background. can use hex codes or names to select colour
    Label1.pack()

Button1 = Button(root, text='click here', command=click1)

#entry allows you to take in input note:pad doesnt work in entry
e = Entry(root, width=50, bg='#feffba')

print(e.get)
e.pack()
e.insert(0, "Your name please")#puts in deafault text in a entry
Button1.pack()

root.mainloop()