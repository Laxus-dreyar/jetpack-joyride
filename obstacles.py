class Obstacle:

    def __init__(self,x,y,shape):
        self.__x = x
        self.__y = y
        self.__shape = shape
    
    def place(self,board):
        x = self.__x
        y = self.__y
        if self.__shape == 1:
            board[x-1][y] = '|'
            board[x][y] = '|'
            board[x+1][y] = '|'
        elif self.__shape == 2:
            board[x][y-2] = '-'
            board[x][y-1] = '-'
            board[x][y] = '-'
            board[x][y+1] = '-'
            board[x][y+2] = '-'
        elif self.__shape == 3:
            board[x+1][y-1] = '/'
            board[x][y] = '/'
            board[x-1][y+1] = '/'
    
    def destroy(self,board):
        x = self.__x
        y = self.__y
        if self.__shape == 1:
            board[x-1][y] = '|'
            board[x][y] = '|'
            board[x+1][y] = '|'
        elif self.__shape == 2:
            board[x][y-2] = '-'
            board[x][y-1] = '-'
            board[x][y] = '-'
            board[x][y+1] = '-'
            board[x][y+2] = '-'
        elif self.__shape == 3:
            board[x+1][y-1] = '/'
            board[x][y] = '/'
            board[x-1][y+1] = '/'