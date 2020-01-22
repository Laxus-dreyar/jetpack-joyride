class Coin:

    def __init__(self,x,y,board):
        self.__value = 1
        self.__x = x
        self.__y = y
        self.__board = board

    def place(self,x,y,board1):
        board = self.__board
        board[x][y] = '$'