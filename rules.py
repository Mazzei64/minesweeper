import settings

class Rule:

    def __init__(self, grid_size=settings.GRID_SIZE):
        self.GRID_PADDING = settings.GRID_PADDING
        self.Y_PADDING_FACTOR = settings.Y_PADDING_FACTOR
        self.HEADER_HEIGHT = settings.HEADER_HEIGHT
        self.BUTTON_PX_WIDTH = settings.BUTTON_PX_WIDTH
        self.BUTTON_PX_HEIGHT = settings.BUTTON_PX_HEIGHT
        self.GRID_SIZE = grid_size
        self.WIDTH = settings.WIDTH
        self.HEIGHT = settings.HEIGHT


        self.MENU_SCREEN_SIZE = settings.MENU_SCREEN_SIZE
        self.IN_GAME_SCREEN_SIZE = settings.IN_GAME_SCREEN_SIZE
        self.IN_GAME_HEADER_WIDTH = settings.IN_GAME_HEADER_WIDTH
        self.IN_GAME_HEADER_HEIGHT = settings.IN_GAME_HEADER_HEIGHT
        self.IN_GAME_BODY_WIDTH = settings.IN_GAME_BODY_WIDTH
        self.IN_GAME_BODY_HEIGHT = settings.IN_GAME_BODY_HEIGHT

        self.IN_GAME_RESTART_BUTTON_W = settings.IN_GAME_RESTART_BUTTON_W
        self.IN_GAME_RESTART_BUTTON_X = settings.IN_GAME_RESTART_BUTTON_X 

        self.IN_GAME_EXIT_BUTTON_W = settings.IN_GAME_EXIT_BUTTON_W
        self.IN_GAME_EXIT_BUTTON_PADDING_RIGHT = settings.IN_GAME_EXIT_BUTTON_PADDING_RIGHT
        self.IN_GAME_EXIT_BUTTON_X = settings.IN_GAME_EXIT_BUTTON_X


        self.CELL_COUNT = settings.CELL_COUNT
        self.MINE_COUNT = settings.MINE_COUNT


    def __InGameUpdateRules(self):
        self.WIDTH = (self.BUTTON_PX_WIDTH*self.GRID_SIZE)
        self.HEIGHT = (self.BUTTON_PX_HEIGHT*self.GRID_SIZE) + self.Y_PADDING_FACTOR

        self.IN_GAME_SCREEN_SIZE = f"{self.WIDTH + (self.GRID_PADDING*2)}x{self.HEIGHT + self.GRID_PADDING}"
        self.IN_GAME_HEADER_WIDTH = self.WIDTH + (self.GRID_PADDING*2)
        self.IN_GAME_HEADER_HEIGHT = self.HEADER_HEIGHT
        self.IN_GAME_BODY_WIDTH = self.WIDTH + (self.GRID_PADDING*2)
        self.IN_GAME_BODY_HEIGHT = self.HEIGHT - self.Y_PADDING_FACTOR + (self.GRID_PADDING*2)

        self.IN_GAME_RESTART_BUTTON_X = (self.IN_GAME_HEADER_WIDTH / 2) - (self.IN_GAME_RESTART_BUTTON_W / 2)

        self.IN_GAME_EXIT_BUTTON_X = self.IN_GAME_HEADER_WIDTH - (self.IN_GAME_EXIT_BUTTON_W + self.IN_GAME_EXIT_BUTTON_PADDING_RIGHT)

        self.CELL_COUNT = self.GRID_SIZE ** 2
        self.MINE_COUNT = self.CELL_COUNT // 4

    def SetGridSize(self, val):
        self.GRID_SIZE = val
        self.__InGameUpdateRules()

    
