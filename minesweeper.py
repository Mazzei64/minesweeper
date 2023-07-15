import random
from itertools import product

from tkinter import *
from tkinter import ttk

class MineSweeper:
    def __init__(self, m, n, initial=0):
        self.__screen = Tk()
        self.__screen.title("Minesweeper")
        self.__screen.geometry("800x800")
        self.__screen.resizable(False, False)
        self.__bt = Button(self.screen, text="Start", width=1,height=1, fg="blue")
        self.__bt.place(x=(300), y=(398))

    def __RenderMainMenu(self):
        pass

    def Run(self):
        self.screen.mainloop()

