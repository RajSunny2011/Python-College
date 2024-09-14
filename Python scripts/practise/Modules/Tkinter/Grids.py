from tkinter import *

root = Tk()


label1 = Label(root, text = 'Hello World!')
label2 = Label(root, text = 'Nice to meet you')
label3 = Label(root, text = 'My name is Mr. G')

#grid puts the widgets in a relative grid
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=9, column=17)#if rows or columns are empty tk ignores them


root.mainloop()