class Background:
    def __init__(self):
        self.__sky = "x"
        self.__ground = 'x'
        # self.__board = board
    
    def create_sky(self,board):
        for i in range(8000):
            board[0][i] = self.__sky
    
    def create_ground(self,board,rows):
        for i in range(8000):
            board[rows-1][i] = self.__ground
