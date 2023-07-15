class MineSweeperInterface:
    '''
        Method responsible for rendering the main menu layout for the game.
    '''
    def RenderMainMenu(self):
        pass
    
    '''
        Method responsible for rendering the options menu layout for configuring the game's settings.
    '''
    def RenderOptionsMenu(self):
        pass
    
    '''
        Method responsible for rendering the layout for the running game.
    '''
    def RenderGameStart(self):
        pass
    
    '''
        Method responsible for rendering the overlaying layout when pausing the game.
    '''
    def RenderPauseScreen(self):
        pass
    
    '''
        Method responsible for rendering the main grid.
    '''
    def RenderGrid(self):
        pass
    
    '''
        Method responsible for rendering the main scoreboard.
    '''
    def RenderScoreBoard(self):
        pass

    '''
        Method responsible for rendering the overboard stopwatch.
    ''' 
    def RenderStopWatch(self):
        pass

    '''
        Method responsible for rendering the restart button for the game.
    ''' 
    def RenderRestartButton(self):
        pass

    '''
        Method responsible for handling the restart button event.
    ''' 
    def RestarGame(self, logger, event):
        pass

    '''
        Method responsible for handling the game starting button event.
    ''' 
    def StartGame(self, logger, event):
        pass
    
    '''
        Method responsible for handling the button event for displaying options menu view.
    ''' 
    def GetSettings(self, logger, event):
        pass
    
    '''
        Method responsible for handling the button event for changing game difficulty.
    ''' 
    def SetDifficulty(self, logger, event):
        pass
    

    '''
        Method responsible for handling the exiting game button event.
    ''' 
    def ExitGame(self, logger, event):
        pass