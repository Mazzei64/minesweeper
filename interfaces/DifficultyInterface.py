class DifficultyInterface:
    '''
        Method responsible for defining a list for a variety of increasing grid sizes in regards to the
        set of difficulties already set.
    '''
    def SetGridSize(self, size):
        pass
    
    '''
        Method responsible for defining the default timeout in regards to the level of difficulty
        and also determines whether this should be a rule or not.
    '''
    def SetTimeOut(self, timeout, allowed):
        pass
    
    '''
        Method responsible for defining the cell to bomb ration in according to the game difficulty setting.
    '''
    def SetCellToBombRatio(self, ratio):
        pass
    
    '''
        Method responsible for defining the points gained per score in accordance with the current difficulty
        setting.
    '''
    def SetPointsPerScore(self, points):
        pass
    
    '''
        Method responsible for defining the points lost per tile marked as a supposed bomb.
    '''
    def SetPointsPerTileMarked(self, points):
        pass