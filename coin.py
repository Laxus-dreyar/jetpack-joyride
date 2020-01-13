class Coin:

    def __init__(self,x,y):
        self.__value = 1
        self.__x = x
        self.__y = y

    def place(self,x,y,board):
        board[x][y] = '$'