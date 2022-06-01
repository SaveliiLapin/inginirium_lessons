import tkinter as tk
import random as rand


def pressed_key(event):  # функция создания движения
    p_p = CANVAS.coords(PLAYER)  # получаем текущие координаты персонажа

    if event.keysym == 'Up' and p_p[1] > 0:
        CANVAS.move(PLAYER, 0, -STEP)
    if event.keysym == 'Down' and p_p[1] < HEIGHT - STEP:
        CANVAS.move(PLAYER, 0, STEP)
    if event.keysym == 'Left' and p_p[0] > 0:
        CANVAS.move(PLAYER, -STEP, 0)
    if event.keysym == 'Right' and p_p[0] < WIDTH - STEP:
        CANVAS.move(PLAYER, STEP, 0)


def restart():
    global PLAYER  # используем переменную в функции
    global PLAYER_POS  # используем переменную в функции

    CANVAS.delete('all') # очищаем холст
    PLAYER_POS = (rand.randint(0, N_X - 1) * STEP, rand.randint(0, N_Y - 1) * STEP)  # ставим случайные координаты
    PLAYER = CANVAS.create_image(PLAYER_POS, image=PLAYER_PIC, anchor='nw')  # создаем игрока


WIN = tk.Tk()  # создали экземпляр окна
STEP = 20  # длина шага персонажа
N_X = 20  # множитель ширины холста
N_Y = 20  # множитель высоты холста
WIDTH = STEP * N_X  # ширина холста
HEIGHT = STEP * N_Y  # высота холста
PLAYER_PIC = tk.PhotoImage(file=r'.\assets\player.png')  # изображение персонажа
PLAYER_POS = (rand.randint(0, N_X - 1) * STEP, rand.randint(0, N_Y - 1) * STEP)  # позиция персонажа


CANVAS = tk.Canvas(WIN, bg='white', width=WIDTH, height=HEIGHT)  # полотно
PLAYER = CANVAS.create_image(PLAYER_POS, image=PLAYER_PIC, anchor='nw')  # создаем персонажа
CANVAS.pack()  # упаковываем полотно


LABEL = tk.Label(WIN, text='Изучаем движение')  # надпись
LABEL.pack()  # упаковываем надпись

RESTART = tk.Button(WIN, text='Рестарт', command=restart)  # создаем кнопку, которая будет вызывать функцию restart
RESTART.pack()  # упаковываем кнопку

WIN.bind('<KeyPress>', pressed_key)  # создаем реакции на кнопки

WIN.mainloop()  # запускаем цикл
