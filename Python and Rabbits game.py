"""Python and Rabbits game.
The image and sound files are located in the repository by
name 'Image-and-sound-for-the-published-repositories'"""


"""Игра: Питон и кролики.
Файлы изображения и звука находятся в repository по имени
 'Image-and-sound-for-the-published-repositories'"""


from tkinter import *
import random
from PIL import ImageTk, Image
import winsound
import threading
import time

# Создаем глобальные переменные
# Ширина экрана
WIDTH = 800
# Высота экрана
HEIGHT = 600
# Размер сегмента змеи
SEG_SIZE = 40
# Переменная, отвечающая за состояние игры
IN_GAME = False


def start_igra(event):
    global IN_GAME
    IN_GAME = True
    c.itemconfigure(restart_text, state='hidden')
    c.itemconfigure(pause, state='hidden')
    c.itemconfigure(close_but, state='hidden')
    #create_block()
    main()
    print('Старт')


def pause_igra(event):
    global IN_GAME
    IN_GAME = False
    c.itemconfig(pause_mon, state='hidden')
    c.itemconfig(close_but, fill='red', state='hidden')
    c.itemconfig(restart_text, text="", fill='red', state='hidden')
    c.itemconfig(pause, state='normal')
    print('Пауза')


def end_of_game(event):
    c.itemconfig(close_but, fill='#8a8a8a', state='normal')
    c.itemconfig(restart_text, text="Новая Игра", fill='#c9c9c9', state='normal')
    c.itemconfig(pause_mon, state='hidden')


def musika_kusaet_potok():
    thr1 = threading.Thread(target=musika_kusaet).start()


def musika_kusaet_sebj_p():
    thr2 = threading.Thread(target=musika_kusaet_sebj).start()


def musika_new0_p():
    thr3 = threading.Thread(target=musika_new0).start()


def musika_exzit_p():
    thr4 = threading.Thread(target=musika_exzit).start()


def musika_new_p():
    thr5 = threading.Thread(target=musika_new).start()


def musika_kus_p():
    thr6 = threading.Thread(target=musika_kus).start()


def musika_kusaet_sebj():
    winsound.PlaySound("C:\\FOTO  Python\\mkrik-sam-sebj.wav",
                       winsound.SND_FILENAME)


def musika_kusaet():
    winsound.PlaySound("C:\\FOTO  Python\\mpoedanie.wav",
                       winsound.SND_FILENAME)


def musika_exzit():
    winsound.PlaySound("C:\\FOTO  Python\\malovato-budet.mp3",
                       winsound.SND_FILENAME)


def musika_kus():
    winsound.PlaySound("C:\\FOTO  Python\\igrok-ubit.wav",
                       winsound.SND_FILENAME)


def musika_new0():
    winsound.PlaySound("C:\\FOTO  Python\\smeh-zloveschiy-radostnyiy1.wav",
                       winsound.SND_FILENAME)


def musika_new():
    winsound.PlaySound("C:\\FOTO  Python\\mnew-game.wav",
                       winsound.SND_FILENAME)


def color_des():
    c.itemconfig('group1', fill="#d76b00", width=6)


def color():
    list = ["#e2180e", "#13a50c", "#0cdcc7", "#9c0ab6", "#9d2266",
            "#b50b2d", "#bd022d", "#e2180e", "RED", "GREEN",
            "BROWN", "BLUE", "PURPLE", "CYAN"]
    random.shuffle(list)
    c.itemconfig('group1', fill=list[0])


# Вспомогательная функция
def create_block():
    """ Создаем еду для змейки """
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy, posx + SEG_SIZE, posy + SEG_SIZE,
                          fill='#b9a82d', width=2)


# Подсчет очков
class Score(object):
    # функция отображения очков на экране
    def __init__(self):
        self.score = 0
        self.x = 110
        self.y = 20
        c.create_text(self.x, self.y, text="Счёт: {}".format(self.score),
                      font="Times 20",
                      fill="Yellow", tag="score", state='hidden')

    # функция счета очков и вывод на экран
    def increment(self):
        c.delete("score")
        self.score += 1
        c.create_text(self.x, self.y, text="Зайцев поймал: {}".format(z),
                      font="Times 20",
                      fill="#c9c9c9", tag="score")

    # функция сброса очков при начале новой игры
    def reset(self):
        c.delete("score")
        self.score = 0


z = 0


# Функция для управления игровым процессом
def main():
    """ Моделируем игровой процесс """
    global IN_GAME, z, index
    if IN_GAME:
        s.move()
        c.itemconfig(pause_mon, state='normal')
        # Определяем координаты головы
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        # столкновения с краями игрового поля
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            musika_kus_p()
            color_des()
            s.reset_snake()
            IN_GAME = False
        # Поедание яблока
        elif head_coords == c.coords(BLOCK):
            z = z + 1
            musika_kusaet_potok()
            s.add_segment()
            s.add_segment()
            s.add_segment()
            c.delete(BLOCK)
            create_block()
            color()
        # Поедание змейки
        else:
            for index in range(len(s.segments) - 1):
                if head_coords == c.coords(s.segments[index].instance):
                    musika_kusaet_sebj_p()
                    #musika_kusaet_sebj()
                    color_des()
                    s.reset_snake()
                    IN_GAME = False
          #запрет на появление еды на змейке
            for index in range(len(s.segments)):
                if c.coords(BLOCK) == c.coords(s.segments[index].instance):
                    c.delete(BLOCK)
                    create_block()
        # скорость змейки
        root.after(300, main)
    # Не IN_GAME -> останавливаем игру и выводим сообщения
    else:
        end_of_game(event=close_but)


class Segment(object):
    """ Сегмент змейки """
    global instance

    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="red", tag="group1", width=2)
        """первое звено --- начало игры"""
        c.itemconfig(self.instance, fill='black')


class Snake(object):
    """ Класс змейки """
    global segment

    def __init__(self, segments):
        self.segments = segments
        # Варианты движения
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # инициируем направление движения
        self.vector = self.mapping["Right"]

    def move(self):
        """ Двигаем змейку в заданном направлении """
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance

            """Сделать первое звено (голова) постоянного цвета"""
            #c.itemconfig(self.segments[-1].instance, fill='#ff8000')
            c.itemconfig(self.segments[-1].instance, fill='black')

            """Сделать последнее звено (хвост) постоянного цвета"""
            c.itemconfig(self.segments[0].instance, fill='#d2d2d2')
            c.itemconfig(self.segments[1].instance, fill='#d2d2d2')
            c.itemconfig(self.segments[2].instance, fill='#d2d2d2')

            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)
        x1, y1, x2, y2 = c.coords(self.segments[-1].instance)
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
                 x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)

    def add_segment(self):
        """ Добавляем сегмент змейки """
        score.increment()
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        """ Изменение направления движения змейки """
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    # Функция обновления змейки при старте новой игры
    def reset_snake(self):
        for segment in self.segments:
            c.delete(segment.instance)


# функция для вывода сообщения
def set_state(item, state):
    c.itemconfigure(item, state=state)
    c.itemconfigure(BLOCK, state='hidden')


# Функция для нажатия кнопки (новая игра)
def clicked(event):
    musika_new_p()
    global IN_GAME, z
    z = 0
    s.reset_snake()
    IN_GAME = True
    c.delete(BLOCK)
    score.reset()
    c.itemconfigure(restart_text, state='hidden')
    c.itemconfigure(game_over_text, state='hidden')
    c.itemconfigure(close_but, state='hidden')
    start_game()
    musika_new0_p()


# Функция для старта игры
def start_game():
    global s
    create_block()
    s = create_snake()
    c.bind("<KeyPress>", s.change_direction)
    main()


# Создаем сегменты и змейку
def create_snake():
    segments = [Segment(SEG_SIZE, SEG_SIZE)]
    # Segment(SEG_SIZE * 2, SEG_SIZE)]
    # Segment(SEG_SIZE * 3, SEG_SIZE)]
    return Snake(segments)


# выход из игры
def close_win(root):
    musika_new0_p()
    exit()


# Настройка главного окна
root = Tk()
st = (' ')
root.title(80 * st + "ИГРА PYTHON   (ПИТОН ЛОВИТ ЗАЙЦЕВ)")
root.iconbitmap(default="C:\FOTO  Python\mrabbit48.ico")
root.geometry('800x600+350+50')
root.resizable(0, 0)
root.wm_attributes('-topmost', 1)
# Создаем экземпляр класса Canvas
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#252c58")
c.grid()
foto1 = ImageTk.PhotoImage(file="C:\FOTO  Python\mpus--1.jpg")
imagesprite = c.create_image(0, 0, image=foto1, anchor=NW)
# Захватываем фокус для отлавливания нажатий клавиш
c.focus_set()
c.bind('<space>', pause_igra)
c.bind('<KeyPress-Return>', start_igra)
st = ' '
pause_mon = c.create_text(400, 20,
                      text = "Для ПАУЗЫ нажмите ПРОБЕЛ",
                               font='Times 12', fill='white', state='hidden')
pause = c.create_text(400, 200,
                      text = st*8+"ПАУЗА!!!\n для продолжения\n нажмите ENTER",
                               font='Times 30', fill='white', state='hidden')
# Текст результата игры
game_over_text = c.create_text(WIDTH / 2, HEIGHT / 2, text="",
                               font='Times 40', fill='red', state='hidden')
# Текст начала новой игры после проигрыша
restart_text = c.create_text(WIDTH / 2, HEIGHT - HEIGHT / 3,
                             font='Times 30',
                             fill='#c9c9c9',
                             text="Новая Игра", state='hidden')
# Текст выхода из программы после проигрыша
close_but = c.create_text(WIDTH / 2, HEIGHT - HEIGHT / 5, font='Times 30',
                          fill='#8a8a8a',
                          text="Выход", state='hidden')
# Отработка событий при нажимания кнопок
c.tag_bind(restart_text, "<Button-1>", clicked)
c.tag_bind(close_but, "<Button-1>", close_win)
# Считаем очки
score = Score()
# Запускаем игру
start_game()
# запускаем окно
root.mainloop()