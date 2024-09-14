import tkinter as tk

def select_section(item):
    print(item)

root = tk.Tk()
item = ["a","b","c"]

section_buttons = []

for i in range(len(item)):
    button = tk.Button(master=root, text=item[i], command=lambda: select_section(item[i]))
    button.grid(column=0,row=i)
    section_buttons.append(button)

root.mainloop()