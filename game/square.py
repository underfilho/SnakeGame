from utils.vector import Vector
from utils.config import Config
from tkinter import Canvas

class Square:
    def __init__(self):
        self.position = Vector(20, 20)
        self._speed = Vector(10, 0)
        self.__square = None

    def update(self):
        self.position.plus(self._speed)

    def draw(self, canvas: Canvas):
        if self.__square is not None:
            canvas.delete(self.__square)

        self.__square = canvas.create_rectangle(self.position.x, self.position.y, self.position.x + 10, self.position.y + 10,
                                      fill=Config.snakeColor)
