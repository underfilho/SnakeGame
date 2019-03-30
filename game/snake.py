from game.body import *
from utils.config import Config

# A cobra é uma lista de bodys, com uma cabeça e um método pra atualizar
class Snake(list):
    def __init__(self):
        super().__init__()
        self.append(Head())

    def update_snake(self, canvas, food, wall):
        for index, i in enumerate(self):
            if index > 0 and self[0].position.equal(i.position):
                return "Voce Perdeu"
            i.update()
            i.draw(canvas)

        for i in wall:
            if self[0].position.equal(i):
                return "Voce Perdeu"

        if (self[0].position.x < 0 or self[0].position.x == Config.width or
                self[0].position.y < 0 or self[0].position.y == Config.height):
            return "Voce Perdeu"

        if self[0].position.equal(food.position):
            body = Body()
            body.set_father(self[len(self) - 1])
            self.append(body)
            #Config.defaultSpeed -= 7

            food.active = False

        if len(self) == Config.goal:
            return "Você Venceu"

        return ""
