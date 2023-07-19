from cell import Cell
from rules import Rule
import settings
import images
from roundedbutton import RoundedButton

from tkinter import *
from tkinter import ttk


class MineSweeper:
    def __init__(self, rule=Rule()):
        self.__gameWindow = None
        self.__menuWindow = None
        self.__selectedDifficulty = 1
        self.__rule_obj = rule

        self.__RenderMainMenu()

    def __RenderMainMenu(self):
        self.__menuWindow = Tk()
        self.__menuWindow.title("Minesweeper")
        self.__menuWindow.geometry(self.__rule_obj.MENU_SCREEN_SIZE)
        self.__menuWindow.eval('tk::PlaceWindow . center')
        self.__menuWindow.resizable(False, False)
        
        startButton = Button(self.__menuWindow, text="Start", width=8,height=1, fg="blue")
        startButton.place(x=(8*8)+35,y=0)
        optionsButton = Button(self.__menuWindow, text="Options", width=8,height=1, fg="blue")
        optionsButton.place(x=(8*8)+35,y=35)

        startButton.bind('<Button-1>', self.__StartGame)
        optionsButton.bind('<Button-1>', self.__OpenSettings)

    def __OpenSettings(self, event):
        self.__menuWindow.withdraw()
        self.__RenderSettingsWindow()

    def __StartGame(self, event):
        self.__menuWindow.withdraw()
        self.__RenderGameWindow()
    
    

    def __RenderSettingsWindow(self):
        self.__settingsWindow = Toplevel(self.__menuWindow)
        self.__settingsWindow.title("Settings")
        self.__settingsWindow.geometry(self.__rule_obj.MENU_SCREEN_SIZE)        
        self.__settingsWindow.resizable(False, False)
        x = self.__menuWindow.winfo_x()
        y = self.__menuWindow.winfo_y()
        self.__settingsWindow.geometry("+%d+%d" %(x,y))
        
        settingsBody = Frame(
            self.__settingsWindow,
            # bg='red',
            width = self.__rule_obj.IN_GAME_BODY_WIDTH,
            height= self.__rule_obj.IN_GAME_BODY_HEIGHT
        )
        settingsBody.place(relx=0.5, rely=0.5, anchor=CENTER)

        caption = Label(settingsBody,text='Select Difficulty:', font=('Arial',14))
        caption.pack(anchor=W, ipady=10)
        
        # self.__optionSelected = IntVar()
        self.__optionSelected = IntVar()

        if self.__rule_obj.GRID_SIZE == 6:
            self.__optionSelected.set('1')
        elif self.__rule_obj.GRID_SIZE == 8:
            self.__optionSelected.set('2')
        elif self.__rule_obj.GRID_SIZE == 12:
            self.__optionSelected.set('3')

        R1 = Radiobutton(settingsBody, text="easy", value=1,variable=self.__optionSelected)
        R1.pack( anchor = W )

        R2 = Radiobutton(settingsBody, text="normal", value=2,variable=self.__optionSelected)
        R2.pack( anchor = W )

        R3 = Radiobutton(settingsBody, text="hard", value=3, variable=self.__optionSelected)
        R3.pack( anchor = W)

        bt=Button(settingsBody, text='Apply')
        bt.pack( anchor = W )
        bt.bind('<Button-1>', self.__SettingsOptionSelect)
        self.__settingsWindow.protocol("WM_DELETE_WINDOW", self.__on_closing)

    def __SettingsOptionSelect(self,event):
        if self.__optionSelected.get() == 1:
            self.__rule_obj.SetGridSize(6)
        elif self.__optionSelected.get() == 2:
            self.__rule_obj.SetGridSize(8)
        elif self.__optionSelected.get() == 3:
            self.__rule_obj.SetGridSize(12)

        self.__menuWindow.deiconify()
        self.__settingsWindow.destroy()
        
    def __RenderGameWindow(self):
        self.__gameWindow = Toplevel(self.__menuWindow)
        self.__gameWindow.title("Minesweeper")
        self.__gameWindow.geometry(self.__rule_obj.IN_GAME_SCREEN_SIZE)        
        self.__gameWindow.resizable(False, False)
        x = self.__menuWindow.winfo_x()
        y = self.__menuWindow.winfo_y()
        self.__gameWindow.geometry("+%d+%d" %(x,y))

        headerFrame = frame = Frame(
            self.__gameWindow,
            bg='black',
            width = self.__rule_obj.IN_GAME_HEADER_WIDTH,
            height = self.__rule_obj.IN_GAME_HEADER_HEIGHT
        )
        frame.place(
            x=0,
            y=0
        )

        frame = Frame(
            self.__gameWindow,
            bg='gray',
            width = self.__rule_obj.IN_GAME_BODY_WIDTH,
            height= self.__rule_obj.IN_GAME_BODY_HEIGHT
        )
        frame.place(
            x=self.__rule_obj.GRID_PADDING,
            y=self.__rule_obj.Y_PADDING_FACTOR
        )

        for x in range(self.__rule_obj.GRID_SIZE):
            for y in range(self.__rule_obj.GRID_SIZE):
                cell = Cell(x,y)
                cell.create_btn_object(frame)
                cell.cell_btn_object.grid(
                    column=x,
                    row=y,
                )

        Cell.randomize_mines(self.__rule_obj)
      
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

        quitButton.place(x=self.__rule_obj.IN_GAME_EXIT_BUTTON_X, y=11)
        restartButton.place(x=self.__rule_obj.IN_GAME_RESTART_BUTTON_X, y=15)
        
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
        Cell.flushCells()
        self.__gameWindow.destroy()
        self.__menuWindow.deiconify()

    def __on_closing(self):
        self.__menuWindow.destroy()

    def Run(self):
        self.__menuWindow.mainloop()


