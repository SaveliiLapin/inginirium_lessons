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
    global ENEMY
    global ENEMY_POS
    global ENEMY_PIC

    ENEMY_PIC = tk.PhotoImage(file=r'.\assets\exit.png')  # изображение врага
    ENEMY_POS = (rand.randint(0, N_X - 1) * STEP, rand.randint(0, N_Y - 1) * STEP)  # позиция врага

    while ENEMY_POS == PLAYER_POS:  # сверяемся, что позиция персонажа != позиция врага
        ENEMY_POS = (rand.randint(0, N_X - 1) * STEP, rand.randint(0, N_Y - 1) * STEP)  # позиция врага

    ENEMY = CANVAS.create_image(ENEMY_POS, image=ENEMY_PIC, anchor='nw')  # создаем врага


def in_exit():
    global P_MOV
    global E_MOV

    p_p = CANVAS.coords(PLAYER)  # получаем текущие координаты персонажа
    e_p = CANVAS.coords(ENEMY)  # получаем текущие координаты врага

    if p_p == e_p:
        LABEL.config(text='Проигрыш!')
        P_MOV = False
        E_MOV = False


def pressed_key(event):  # функция создания движения
    p_p = CANVAS.coords(PLAYER)  # получаем текущие координаты персонажа
    if P_MOV:
        if event.keysym == 'Up' and p_p[1] > 0:
            CANVAS.move(PLAYER, 0, -STEP)
        if event.keysym == 'Down' and p_p[1] < HEIGHT - STEP:
            CANVAS.move(PLAYER, 0, STEP)
        if event.keysym == 'Left' and p_p[0] > 0:
            CANVAS.move(PLAYER, -STEP, 0)
        if event.keysym == 'Right' and p_p[0] < WIDTH - STEP:
            CANVAS.move(PLAYER, STEP, 0)

    if E_MOV:
        e_p = CANVAS.coords(ENEMY)
        x = 0
        y = 0

        if e_p[0] == 0:
            x = rand.randint(0, 1)
        elif e_p[0] == WIDTH - STEP:
            x = rand.randint(-1, 0)
        else:
            x = rand.randint(-1, 1)

        if e_p[1] == 0:
            y = rand.randint(0, 1)
        elif e_p[1] == HEIGHT - STEP:
            y = rand.randint(-1, 0)
        else:
            y = rand.randint(-1, 1)

        CANVAS.move(ENEMY, x * STEP, y * STEP)

    in_exit()


def restart():
    global P_MOV
    global E_MOV

    CANVAS.delete('all')  # очищаем холст
    player_creation()
    exit_creation()
    P_MOV = True
    E_MOV = True


WIN = tk.Tk()  # создали экземпляр окна
STEP = 20  # длина шага персонажа
N_X = 20  # множитель ширины холста
N_Y = 20  # множитель высоты холста
WIDTH = STEP * N_X  # ширина холста
HEIGHT = STEP * N_Y  # высота холста
P_MOV = True  # может ли персонаж двигаться
E_MOV = True  # может ли враг двигаться


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
