class CellInterface:
    '''
        Property responsible for returning cell objects that are currently surrounding
        self in the grid.
    '''
    @property
    def surrouding_cells(self):
        pass
    
    '''
        Property responsible for returning the count of cells that are currently surrounding
        self on the grid.
    '''
    @property
    def surrounding_cells_count(self):
        pass
    
    '''
        Method responsible for instantiating a button object to the button field of the object.
    '''
    def create_btn_object(self, position):
        pass
    
    '''
        Method responsible for displaying the underlying concent of the self cell object
    '''
    def show_cell(self):
        pass

    '''
        Method responsible for displaying the underlying concent of the self cell object
        when it's a mine
    '''
    def show_mine(self):
        pass
    
    '''
        Method responsible for returning the cell object by its x and y position on the grid
        from the Class' list.
    '''
    def get_cell_by_axis(self,x,y):
        pass

    '''
        Method responsible for handling the mouse left-click
    '''
    def left_click(self, event):
        pass

    '''
        Method responsible for handling the mouse right-click.
    '''
    def right_click(self, event):
        pass

    '''
        Class Method responsible randomly placing the mines in the selected cells from the grid, according to the.
    '''
    @staticmethod
    def randomize_mines(rule):
        pass

    '''
        Class Method responsible creating the score main label
    '''
    @staticmethod
    def create_score_label(rule):
        pass

    '''
        Class Method for refreshing objects in the class list to their original state.
    '''
    @staticmethod
    def refresh(rule):
        pass

    '''
        Class Method for flushing out every object reference from the class list.
    '''
    @staticmethod
    def flushCells(rule):
        pass