from tkinter import Tk, Canvas, Frame, messagebox
from utils.windowmanager import WindowManager
from utils.config import Config
from utils.wall import Wall
from game.snake import Snake
from game.food import Food

class SnakeGame:
    def __init__(self):
        self.__window = Tk()
        self.__wman = WindowManager(self.__window)
        self.__canvas = None
        self.__snake = None
        self.__food = None
        self.__wall = list()

        self.setup()
        self.start()

        self.__window.mainloop()

    def setup(self):
        self.__window.geometry('%ix%i' % (Config.width, Config.height))
        self.__window.resizable(False, False)
        self.__window.title("Snake")

        self.__window.bind('<Key>', self.set_direction)
        self.__window.bind('<Escape>', lambda event: self.end('Saindo do jogo'))

    def set_direction(self, event):
        if event.keysym == 'Up':
            self.__snake[0].direction(0, -1)
        if event.keysym == 'Down':
            self.__snake[0].direction(0, 1)
        if event.keysym == 'Left':
            self.__snake[0].direction(-1, 0)
        if event.keysym == 'Right':
            self.__snake[0].direction(1, 0)

    def start(self):
        frame = Frame(bg=Config.bgColor)
        frame.pack()

        self.__canvas = Canvas(frame, bg=Config.bgColor, width=str(Config.width), height=str(Config.height), highlightthickness=0)
        self.__canvas.pack()
        self.__snake = Snake()
        self.__food = Food()

        self.create_map()

        messagebox.showinfo("Snake", "Meta: " + str(Config.goal) + "\nPressione Esc para sair do jogo")
        self.__window.focus_force()
        self.update()

    def update(self):
        if not self.__food.active:
            self.__food.new_position(self.__wall)
            self.__food.draw(self.__canvas)
            self.__food.active = True

        result = self.__snake.update_snake(self.__canvas, self.__food, self.__wall)

        if result != "":
            self.end(result)

        self.__window.after(Config.defaultSpeed, self.update)

    def create_map(self):
        try:
            file = open('editor\map.txt')
        except IOError:
            return

        num_lines = len(file.readlines())
        file.seek(0)

        for i in range(0, num_lines):
            pos = file.readline().split("x")
            wall = Wall(int(pos[0]), int(pos[1]))
            self.__wall.append(wall)
            self.__canvas.create_rectangle(wall.x, wall.y, wall.x + 10, wall.y + 10, fill=Config.wallColor)

    def end(self, message):
        messagebox.showinfo("Fim de jogo", message)
        self.__wman.open('Menu')
