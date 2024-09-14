from tkinter import *

root = Tk()
root.title('Calculator')

def press(a):
    e.insert(len(e.get()),a)

def bacsp():
    e.delete(len(e.get())-1)

def eql():
    exp = e.get()
    exp = exp.replace('x','*')
    exp = exp.replace('^','**')
    try:
        ans = eval(exp)
        if type(ans) == float:
            ans = format(ans, '.9f')
            ans = ans.rstrip('0')
    except Exception:
        ans = 'ERROR'
    e.delete(0,END)
    e.insert(0,ans)

e = Entry(root, width=40, borderwidth=5)
button1 = Button(root, text="1", padx=20, pady=15, command=lambda: press(1))
button2 = Button(root, text="2", padx=20, pady=15, command=lambda: press(2))
button3 = Button(root, text="3", padx=20, pady=15, command=lambda: press(3))
button4 = Button(root, text="4", padx=20, pady=15, command=lambda: press(4))
button5 = Button(root, text="5", padx=20, pady=15, command=lambda: press(5))
button6 = Button(root, text="6", padx=20, pady=15, command=lambda: press(6))
button7 = Button(root, text="7", padx=20, pady=15, command=lambda: press(7))
button8 = Button(root, text="8", padx=20, pady=15, command=lambda: press(8))
button9 = Button(root, text="9", padx=20, pady=15, command=lambda: press(9))
button0 = Button(root, text="0", padx=20, pady=15, command=lambda: press(0))
buttonpls = Button(root, text="+", padx=20, pady=15, command=lambda: press('+'))
buttonmin = Button(root, text="-", padx=20, pady=15, command=lambda: press('-'))
buttonmul = Button(root, text="x", padx=20, pady=15, command=lambda: press('x'))
buttondiv = Button(root, text="/", padx=20, pady=15, command=lambda: press('/'))
buttoneql = Button(root, text="=", padx=20, pady=15, command=eql)
buttondec = Button(root, text=".", padx=20, pady=15, command=lambda: press('.'))
buttonexp = Button(root, text="^", padx=20, pady=15, command=lambda: press('^'))
buttonbro = Button(root, text="(", padx=20, pady=15, command=lambda: press('('))
buttonbrc = Button(root, text=")", padx=20, pady=15, command=lambda: press(')'))
buttondel = Button(root, text="<-", padx=20, pady=15, command=bacsp)

e.grid(row=0, column=0, columnspan=4)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
buttonpls.grid(row=1, column=3)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonmin.grid(row=2, column=3)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
buttonmul.grid(row=3, column=3)
buttondec.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttoneql.grid(row=4, column=2)
buttondiv.grid(row=4, column=3)
buttonexp.grid(row=5, column=0)
buttonbro.grid(row=5, column=1)
buttonbrc.grid(row=5, column=2)
buttondel.grid(row=5, column=3)


root.mainloop()