from tkinter import *

root = Tk()
root.title('Calculator')
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

cal = 0
n1 = 0


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def add():
    global n1, cal
    cal = 0
    n1 = float(e.get())
    e.delete(0, END)


def sub():
    global n1, cal
    cal = 1
    n1 = float(e.get())
    e.delete(0, END)


def div():
    global n1, cal
    cal = 2
    n1 = float(e.get())
    e.delete(0, END)


def mul():
    global n1, cal
    cal = 3
    n1 = float(e.get())
    e.delete(0, END)


def equal():
    res = 0
    if cal == 0:
        res = n1 + float(e.get())
    if cal == 1:
        res = n1 - float(e.get())
    if cal == 2:
        res = n1 / float(e.get())
    if cal == 3:
        res = n1 * float(e.get())
    e.delete(0, END)
    e.insert(0, res)


def ket():
    e.insert(END, ".")


Button(root, text='1', padx=40, pady=20, command=lambda: click(1)).grid(row=3, column=0)
Button(root, text='2', padx=40, pady=20, command=lambda: click(2)).grid(row=3, column=1)
Button(root, text='3', padx=40, pady=20, command=lambda: click(3)).grid(row=3, column=2)
Button(root, text='4', padx=40, pady=20, command=lambda: click(4)).grid(row=2, column=0)
Button(root, text='5', padx=40, pady=20, command=lambda: click(5)).grid(row=2, column=1)
Button(root, text='6', padx=40, pady=20, command=lambda: click(6)).grid(row=2, column=2)
Button(root, text='7', padx=40, pady=20, command=lambda: click(7)).grid(row=1, column=0)
Button(root, text='8', padx=40, pady=20, command=lambda: click(8)).grid(row=1, column=1)
Button(root, text='9', padx=40, pady=20, command=lambda: click(9)).grid(row=1, column=2)
Button(root, text='0', padx=40, pady=20, command=lambda: click(0)).grid(row=4, column=1)
Button(root, text='C', padx=40, pady=20, command=clear).grid(row=0, column=3)
Button(root, text='/', padx=40, pady=20, command=div).grid(row=1, column=3)
Button(root, text='*', padx=40, pady=20, command=mul).grid(row=2, column=3)
Button(root, text='-', padx=40, pady=20, command=sub).grid(row=3, column=3)
Button(root, text='+', padx=40, pady=20, command=add).grid(row=4, column=3)
Button(root, text='=', padx=40, pady=20, command=equal).grid(row=4, column=2)
Button(root, text='.', padx=40, pady=20, command=ket).grid(row=4, column=0)

root.mainloop()
