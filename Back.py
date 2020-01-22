class Background:
    def __init__(self,board):
        self.__sky = "x"
        self.__ground = 'x'
        self.__board = board
    
    def create_ground(self,board1,rows):
        board = self.__board
        for i in range(8000):
            board[rows-1][i] = self.__ground
