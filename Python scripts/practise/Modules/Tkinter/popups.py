from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x80')

l = ['showinfo','showwarning','showerror']

def popup(n):
    if n == "showinfo":
        messagebox.showinfo('Info!','message')
    elif n == 'showwarning':
        messagebox.showwarning('Warning!','message')
    elif n == 'showerror':
        messagebox.showerror('Error!','message')

Button(root, text='Show info', command=lambda: popup('showinfo')).pack()
Button(root, text='Show warning', command=lambda: popup('showwarning')).pack()
Button(root, text='Show error', command=lambda: popup('showerror')).pack()

root.mainloop()