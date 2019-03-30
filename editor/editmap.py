from tkinter import Tk, Canvas, Frame, messagebox
from utils.windowmanager import WindowManager
from utils.config import Config
from utils.wall import Wall

class EditMap:
    def __init__(self):
        self.__window = Tk()
        self.__wman = WindowManager(self.__window)
        self.__canvas = None
        self.__wall = list()

        self.setup()
        self.start()
        self.draw_matrix()
        self.welcome()
        self.__window.focus_force()

        self.__window.mainloop()

    def setup(self):
        self.__window.geometry('%ix%i' % (Config.width, Config.height))
        self.__window.resizable(False, False)
        self.__window.title("Editor")

        # Botão esquerdo do mouse
        self.__window.bind('<Button-1>', self.new_wall)
        # Botão direito do mouse
        self.__window.bind('<Button-3>', self.delete_wall)
        self.__window.bind('<Return>', self.save)
        self.__window.bind('<Escape>', lambda event: self.end('Saindo do editor'))

    def start(self):
        self.__window.focus_force()
        frame = Frame(bg="black")
        frame.pack()

        self.__canvas = Canvas(frame, bg="black", width=str(Config.width), height=str(Config.height), highlightthickness=0)
        self.__canvas.pack()

    def welcome(self):
        messagebox.showinfo("Editor de mapas", "Para criar novas paredes clique com o botão esquerdo do mouse, com o direito para apagar\n"
                                               "Para concluir seu mapa tecle Enter, para cancelar Esc")

    def new_wall(self, event):
        # Cria um retângulo na posição do clique
        rec = Wall(int(event.x/10) * 10, int(event.y/10) * 10)
        exist = False

        for i in self.__wall:
            if i.equal(rec.x, rec.y):
                exist = True

        if not exist:
            rec.id = self.__canvas.create_rectangle(rec.x, rec.y, rec.x + 10, rec.y + 10,
                                        fill=Config.wallColor)
            self.__wall.append(rec)

    def delete_wall(self, event):
        rec = Wall(int(event.x/10) * 10, int(event.y/10) * 10)
        aux = len(self.__wall) - 1

        if aux >= 0:
            for index, i in enumerate(self.__wall):
                if i.equal(rec.x, rec.y):
                    aux = index

            self.__canvas.delete(self.__wall[aux].id)
            self.__wall.pop(aux)

    def save(self, event):
        file = open('editor\map.txt', 'w')
        file.close()
        file = open('editor\map.txt', 'a')

        for i in self.__wall:
            file.write("%ix%i\n" % (i.x, i.y))

        file.close()
        self.end("Novo mapa criado")

    def draw_matrix(self):
        for i in range(1, 25):
            self.__canvas.create_line(i*10, 0, i*10, 250, fill='grey')
        for i in range(1, 25):
            self.__canvas.create_line(0, i*10, 250, i*10, fill='grey')

    def end(self, message):
        messagebox.showinfo("Saindo do Editor", message)
        self.__wman.open('Menu')
