class Obstacle:

    def __init__(self,x,y,shape):
        self.__x = x
        self.__shape = shape
    
    def place(self,x,y,shape,board):
        if self.__shape == 1:
            board[x-1][y] = '|'
            board[x][y] = '|'
            board[x+1][y] = '|'
        elif self.__shape == 2:
            board[x][y-1] = '-'
            board[x][y] = '-'
            board[x][y+1] = '-'