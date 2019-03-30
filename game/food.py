from utils.vector import Vector
from utils.config import Config
from random import randint
from tkinter import Canvas

class Food:
    def __init__(self):
        self.position = Vector()
        self.active = False
        self.__rec = None

    def new_position(self, wall):
        self.position.x = randint(0, Config.width/10 - 1) * 10
        self.position.y = randint(0, Config.height/10 - 1) * 10

        for i in wall:
            if self.position.equal(i):
                self.new_position(wall)
                break

    def draw(self, canvas: Canvas):
        if self.__rec is not None:
            canvas.delete(self.__rec)

        self.__rec = canvas.create_rectangle(self.position.x, self.position.y, self.position.x + 10, self.position.y + 10,
                                           fill=Config.foodColor)
