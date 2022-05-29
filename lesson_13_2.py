# Задание 2
#
# Нарисуйте доску с расставленными шашками

import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='white', width=400, height=400)

for i in range(50, 400, 50):
    canvas.create_line((i, 0), (i, 400), fill='black')
    canvas.create_line((0, i), (400, i), fill='black')

x = 0
y = 0
stroka = 0

for i in range(12):
    canvas.create_oval((x, y), (x + 50, y + 50), fill='lightgreen')
    canvas.create_oval((350 - x, y + 250), (350 - x + 50, y + 300), fill='lightblue')

    x += 100

    if x >= 400:
        stroka += 1

        if stroka % 2 != 0:
            x = 50
        else:
            x = 0

        y += 50

canvas.pack()
win.mainloop()
