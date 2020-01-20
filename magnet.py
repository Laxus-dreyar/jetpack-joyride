class Magnet():

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def make_field(self,board):
        x = self.__x
        y = self.__y
        for i in range(7):
            for j in range(7):
                board[i][j] = 0