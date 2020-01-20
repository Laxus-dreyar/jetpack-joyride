class Speedup:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def place(self,board):
        board[self.__x][self.__y] = 'M'