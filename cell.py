from tkinter import Button, Label
import random
import settings

class Cell:
    cells_list = []
    global_socore_label_obj = None
    global_score = 0
    game_over = False

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_flagged = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.cells_list.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=1,
            height=1,
            text=''
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)

        self.cell_btn_object = btn

    def left_click(self,event):
        if self.is_mine:
            self.show_mine()
            return
        
        if self.cell_btn_object["state"] != "disabled":
            if self.surrounding_cells_mines_count == 0:
                for cell in self.surrounding_cells:
                    cell.show_cell()
                    if not cell.is_open:
                        Cell.global_score = Cell.global_score + 1
                    cell.is_open = True

                self.show_cell()
                self.is_open = True
                Cell.global_score = Cell.global_score + 1
                Cell.global_socore_label_obj.configure(text=f"SCORE: {Cell.global_score}")
                return

            self.show_cell()
            self.is_open = True
            Cell.global_score = Cell.global_score + 1
            Cell.global_socore_label_obj.configure(text=f"SCORE: {Cell.global_score}")
    
    def right_click(self,event):
        if not self.is_flagged:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_flagged = True
            Cell.global_score = Cell.global_score - 1
            Cell.global_socore_label_obj.configure(text=f"SCORE: {Cell.global_score}")
            return
        
        self.cell_btn_object.configure(
            bg='gray85'
        )
        self.is_flagged = False

    def get_cell_by_axis(self, x, y):
        for cell in Cell.cells_list:
            if cell.x == x and cell.y == y:
                return cell
    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_cells_mines_count(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter
    
   

    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounding_cells_mines_count)
        self.cell_btn_object["state"] = "disabled"

    def show_mine(self):
        for cell in self.cells_list:
            if cell.is_mine:
                cell.cell_btn_object.configure(bg='orange')
                cell.cell_btn_object["state"] = "disabled"
                print(cell.cell_btn_object["state"])
            else:  
                cell.show_cell()
            
        self.cell_btn_object.configure(bg='red')

    @staticmethod
    def randomize_mines():
        shuffled_cells = random.sample(
            Cell.cells_list,
            settings.MINE_COUNT
        )
        for cell in shuffled_cells:
            cell.is_mine = True

        print(shuffled_cells)

    @staticmethod
    def create_score_label(position):
        lbl = Label(
            position,
            background='black',
            fg='white',
            text=f"SCORE: {Cell.global_score}"
        )
        Cell.global_socore_label_obj = lbl

    @staticmethod
    def refresh():
        for cell in Cell.cells_list:
            cell.cell_btn_object["state"] = "normal"
            cell.cell_btn_object.configure(
                bg='gray85',
                text=' '
            )
        Cell.global_score = 0
        Cell.global_socore_label_obj.configure(text=f"SCORE: {Cell.global_score}")

    def __repr__(self):
        return f"Cell({self.x},{self.y})"

