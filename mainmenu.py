# Projeto POO SnakeGame
# Feito por Anderson

from tkinter import Tk, Frame, Button, Label
from utils.windowmanager import WindowManager

class Menu():
    def __init__(self):
        self.__window = Tk()
        self.__wman = WindowManager(self.__window)
        self.setup()

        self.__window.mainloop()
    
    def setup(self):
        self.__window.geometry('200x70')
        self.__window.resizable(False, False)
        self.__window.title("Menu")

        Label(self.__window, text='Escolha uma opção:').place(x=37, y=6)
        Button(self.__window, text='Jogar', command=self.game).place(x=47, y=31)
        Button(self.__window, text='Editor', command=self.editor).place(x=97, y=31)

    def game(self):
        self.__wman.open('Game')

    def editor(self):
        self.__wman.open('Editor')

# Main
if __name__ == "__main__":
    Menu()
