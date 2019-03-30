from game.square import Square
from utils.vector import Vector

class Body(Square):
    def __init__(self):
        super().__init__()
        # O pai será o quadrado a ser seguido
        self.__father = None
        self.__nextSpeed = Vector()
        self.__dirChanged = False

    def update(self):
        # Se mudou a direção da cabeça do pai, mude do filho também
        if self.__dirChanged:
            self._speed.set(self.__nextSpeed)
            self.__dirChanged = False
        if not self._speed.equal(self.__father._speed):
            self.__nextSpeed.set(self.__father._speed)
            self.__dirChanged = True

        super().update()

    # O pai será a próxima célula, a qual essa seguirá
    def set_father(self, father):
        self.__father = father
        self.position.x = father.position.x - father._speed.x
        self.position.y = father.position.y - father._speed.y
        self._speed.set(father._speed)


class Head(Square):
    # Chamado ao mudar direção
    def direction(self, x, y):
        if self._speed.x != 0 and y != 0:
            self._speed.y = y * 10
            self._speed.x = 0
        if self._speed.y != 0 and x != 0:
            self._speed.x = x * 10
            self._speed.y = 0
