import tkinter as tk
import random as rand


def player_creation():
    global PLAYER
    global PLAYER_POS
    global PLAYER_PIC

    PLAYER_PIC = tk.PhotoImage(file=r'.\assets\player.png')  # изображение персонажа
    PLAYER_POS = (rand.randint(0, N_X - 1) * STEP, rand.randint(0, N_Y - 1) * STEP)  # позиция персонажа
    PLAYER = CANVAS.create_image(PLAYER_POS, image=PLAYER_PIC, anchor='nw')  # создаем персонажа


def exit_creation():
    global EXIT
    global EXIT_POS
    global EXIT_PIC

    EXIT_PIC = tk.PhotoImage(file=r'.\assets\exit.png')  # изображение выхода
    EXIT_POS = (rand.randint(0, N_X - 1) * STEP, rand.randint(0, N_Y - 1) * STEP)  # позиция выхода

    while EXIT_POS == PLAYER_POS:  # сверяемся, что позиция персонажа != позиция выхода
        EXIT_POS = (rand.randint(0, N_X - 1) * STEP, rand.randint(0, N_Y - 1) * STEP)  # позиция выхода

    EXIT = CANVAS.create_image(EXIT_POS, image=EXIT_PIC, anchor='nw')  # создаем выход


def in_exit():
    global MOV

    p_p = CANVAS.coords(PLAYER)  # получаем текущие координаты персонажа
    e_p = CANVAS.coords(EXIT)  # получаем текущие координаты персонажа

    if p_p == e_p:
        LABEL.config(text='Победа!')
        MOV = False


def pressed_key(event):  # функция создания движения
    p_p = CANVAS.coords(PLAYER)  # получаем текущие координаты персонажа
    if MOV:
        if event.keysym == 'Up' and p_p[1] > 0:
            CANVAS.move(PLAYER, 0, -STEP)
        if event.keysym == 'Down' and p_p[1] < HEIGHT - STEP:
            CANVAS.move(PLAYER, 0, STEP)
        if event.keysym == 'Left' and p_p[0] > 0:
            CANVAS.move(PLAYER, -STEP, 0)
        if event.keysym == 'Right' and p_p[0] < WIDTH - STEP:
            CANVAS.move(PLAYER, STEP, 0)

    in_exit()


def restart():
    global MOV

    CANVAS.delete('all')  # очищаем холст
    player_creation()
    exit_creation()
    MOV = True


WIN = tk.Tk()  # создали экземпляр окна
STEP = 20  # длина шага персонажа
N_X = 20  # множитель ширины холста
N_Y = 20  # множитель высоты холста
WIDTH = STEP * N_X  # ширина холста
HEIGHT = STEP * N_Y  # высота холста
MOV = True  # может ли персонаж двигаться


CANVAS = tk.Canvas(WIN, bg='white', width=WIDTH, height=HEIGHT)  # полотно

player_creation()
exit_creation()

CANVAS.pack()  # упаковываем полотно


LABEL = tk.Label(WIN, text='Изучаем движение')  # надпись
LABEL.pack()  # упаковываем надпись

RESTART = tk.Button(WIN, text='Рестарт', command=restart)  # создаем кнопку, которая будет вызывать функцию restart
RESTART.pack()  # упаковываем кнопку

WIN.bind('<KeyPress>', pressed_key)  # создаем реакции на кнопки

WIN.mainloop()  # запускаем цикл
