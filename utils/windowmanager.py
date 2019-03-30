class WindowManager:
    def __init__(self, root):
        self.__root = root

    def open(self, window):
        self.__root.destroy()

        if window == 'Game':
            from game.snakegame import SnakeGame
            SnakeGame()
        if window == 'Editor':
            from editor.editmap import EditMap 
            EditMap()
        if window == 'Menu':
            from mainmenu import Menu
            Menu()