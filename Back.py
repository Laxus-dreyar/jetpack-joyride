class Background:
    def __init__(self):
        self.__sky = "\"
        self.__groundup = 'T'
        self.__grounddown = '-'
    
    def create_sky(self,board):
        for i in range(2000):
            grid[0][i] = self.__sky
    
    def create_ground(self,board):
        for i in range(2000):
            grid[28][i] = self.__groundup
            grid[29][i] = self.__grounddown