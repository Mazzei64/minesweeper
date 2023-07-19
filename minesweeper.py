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
        self.__menuWindow.withdraw()
        self.__RenderGameWindow()

    def __RenderGameWindow(self):
        self.__gameWindow = Toplevel(self.__menuWindow)
        self.__gameWindow.title("Minesweeper")
        self.__gameWindow.geometry(settings.IN_GAME_SCREEN_SIZE)        
        self.__gameWindow.resizable(False, False)
        x = self.__menuWindow.winfo_x()
        y = self.__menuWindow.winfo_y()
        self.__gameWindow.geometry("+%d+%d" %(x,y))

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
      
        restartButton = Label(
            headerFrame,
            width=3,
            height=1,
            relief='raised',
            font=("Arial", 14),
            text='⚫',
            bg='black',
            fg='red'
            )
        
        quitButton = Label(
            headerFrame,
            width=4,
            height=1,
            relief='raised',
            font=("Arial", 15),
            text='exit',
            bg='black',
            fg='red',
            borderwidth=1
        )

        quitButton.place(x=settings.IN_GAME_EXIT_BUTTON_X, y=11)
        restartButton.place(x=settings.IN_GAME_RESTART_BUTTON_X, y=15)
        
        quitButton.bind('<Enter>', self.__OverButton)
        quitButton.bind('<Leave>', self.__OffButton)
        quitButton.bind('<Button-1>', self.__ExitGame)

        restartButton.bind('<Enter>', self.__OverButton)
        restartButton.bind('<Leave>', self.__OffButton)
        restartButton.bind('<Button-1>', self.__RestartGame)

        Cell.create_score_label(headerFrame)
        Cell.global_socore_label_obj.place(
            x=5,
            y=15
        )

        self.__gameWindow.protocol("WM_DELETE_WINDOW", self.__on_closing)

    def __OverButton(self, event):
        event.widget.configure(relief='sunken')
        event.widget.configure(bg='red', fg='black')

    def __OffButton(self, event):
        event.widget.configure(relief='raised')
        event.widget.configure(bg='black', fg='red')

    def __RestartGame(self, event):
        Cell.refresh()

    def __ExitGame(self, event):
        self.__gameWindow.destroy()
        self.__menuWindow.deiconify()

    def __on_closing(self):
        self.__menuWindow.destroy()

    def Run(self):
        self.__menuWindow.mainloop()


