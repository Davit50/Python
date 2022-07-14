import tkinter
from random import randint as r, choice


def draw(event):
    if h > w:
        a = r(1, w)
    else:
        a = r(1, h)

    xy = (r(1, h - a), r(1, h - a))
    size = (xy[0] + a, xy[1] + a)
    i = '1234567890ABCDEF'
    a1 = choice(i)
    a2 = choice(i)
    a3 = choice(i)
    a4 = choice(i)
    a5 = choice(i)
    a6 = choice(i)
    canvas.create_oval(xy, size, fill=f'#{a1}{a2}{a3}{a4}{a5}{a6}')

    print(xy)
    print(size)


h = 600
w = 600
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=h, width=w)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
