from tkinter import *

root = Tk()

#defining a label Label(<master widget>, <data>)
myLabel = Label(root, text = 'hello world', padx=50, pady=10)#padx and pady add padding to the widget

#basic way to put a widget into a window, puts the item wherever it can in the order the pack func is ran
myLabel.pack()

#event loop
root.mainloop()