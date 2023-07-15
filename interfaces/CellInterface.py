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
    def CreateBtnObject(self, position):
        pass
    
    '''
        Method responsible for displaying the underlying concent of the self cell object
    '''
    def ShowCell(self):
        pass
    
    '''
        Method responsible for returning the cell object by its x and y position on the grid
        from the Class' list.
    '''
    def GetCellByAxis(self,x,y):
        pass

    '''
        Method responsible for handling the mouse left-click
    '''
    def LeftClickActions(self, event):
        pass

    '''
        Method responsible for handling the mouse right-click.
    '''
    def RightClickActions(self, event):
        pass

    '''
        Class Method responsible randomly placing the mines in the selected cells from the grid, according to the.
    '''
    @staticmethod
    def RandomizeMines(rule):
        pass