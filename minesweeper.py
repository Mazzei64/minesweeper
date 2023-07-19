from cell import Cell
import settings
import images
from roundedbutton import RoundedButton

from tkinter import *
from tkinter import ttk


class MineSweeper:
    def __init__(self):
        self.__gameWindow = None
        self.__menuWindow = None
        self.__menuWindowConfig = None
        self.__buttonImage = None
        # self.__bt = Button(self.__screen, text="Start", width=1,height=1, fg="blue")
        # self.__bt.place(x=(300), y=(398))

        self.__RenderMainMenu()

    def __RenderMainMenu(self):
        self.__menuWindow = Tk()
        self.__menuWindow.title("Minesweeper")
        self.__menuWindow.geometry(settings.MENU_SCREEN_SIZE)
        self.__menuWindow.eval('tk::PlaceWindow . center')
        self.__menuWindow.resizable(False, False)
        
        startButton = Button(self.__menuWindow, text="Start", width=8,height=1, fg="blue")
        startButton.place(x=(8*8)+35,y=0)
        optionsButton = Button(self.__menuWindow, text="Options", width=8,height=1, fg="blue")
        optionsButton.place(x=(8*8)+35,y=35)

        startButton.bind('<Button-1>', self.__StartGame)
        self.__menuWindow.configure()

    def __StartGame(self, event):
        # self.__menuWindowConfig = self.__menuWindow.config()
        self.__menuWindow.destroy()
        # print(self.__menuWindowConfig)
        self.__RenderGameWindow()

    def __RenderGameWindow(self):
        self.__gameWindow = Tk()
        self.__gameWindow.title("Minesweeper")
        self.__gameWindow.geometry(settings.IN_GAME_SCREEN_SIZE)
        self.__gameWindow.eval('tk::PlaceWindow . center')
        self.__gameWindow.resizable(False, False)
        self.__buttonImage = PhotoImage(file='images/light-red-button.png')
        self.__buttonImage.configure(width=30, height=30)
        # self.__buttonImage.zoom(x=30, y=30)

        headerFrame = frame = Frame(
            self.__gameWindow,
            bg='black',
            width = settings.IN_GAME_HEADER_WIDTH,
            height = settings.IN_GAME_HEADER_HEIGHT
        )
        frame.place(
            x=0,
            y=0
        )

        frame = Frame(
            self.__gameWindow,
            bg='gray',
            width = settings.IN_GAME_BODY_WIDTH,
            height= settings.IN_GAME_BODY_HEIGHT
        )
        frame.place(
            x=settings.GRID_PADDING,
            y=settings.Y_PADDING_FACTOR
        )

        for x in range(settings.GRID_SIZE):
            for y in range(settings.GRID_SIZE):
                cell = Cell(x,y)
                cell.create_btn_object(frame)
                cell.cell_btn_object.grid(
                    column=x,
                    row=y,
                )

        Cell.randomize_mines()

        bt = Button(
            headerFrame,
            image=self.__buttonImage,
            width=30,
            height=30,
            borderwidth=0
            # wraplength=1,
            # bg='black',
            # fg='red',
            # activebackground='black',
            # activeforeground='red',
            # bd='0',
            
            )
        bt.place(x=140, y=10)
        # bt = RoundedButton(headerFrame, width=30, height=30, cornerradius=15,padding=1, color='red', bg='white', command=self.RestartGame) 
        # bt.place(x=140, y=10)
        bt.bind('<Button-1>', self.RestartGame)

        Cell.create_score_label(headerFrame)
        Cell.global_socore_label_obj.place(
            x=5,
            y=15
        )

        self.__gameWindow.mainloop()

    def RestartGame(self, event):
        Cell.refresh()

    def Run(self):
        self.__menuWindow.mainloop()


