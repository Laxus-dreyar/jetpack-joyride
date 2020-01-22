class Speedup:
    
    def __init__(self,x,y,board):
        self.__x = x
        self.__y = y
        self.__board = board

    def place(self,board1):
        board = self.__board
        board[self.__x][self.__y] = 'F'