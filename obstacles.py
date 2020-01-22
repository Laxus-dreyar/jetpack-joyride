class Obstacle:

    def __init__(self,x,y,shape,board):
        self.__x = x
        self.__y = y
        self.__shape = shape
        self.__flag = 0
        self.__board = board
    
    def place(self,board1):
        board = self.__board
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
    
    def ret_x(self):
        return self.__x
        
    def ret_y(self):
        return self.__y
    
    def get_flag(self):
        return self.__flag

    def destroy(self,board1):
        board = self.__board
        x = self.__x
        y = self.__y
        self.__flag = 1
        if self.__shape == 1:
            board[x-1][y] = ' '
            board[x][y] = ' '
            board[x+1][y] = ' '
        elif self.__shape == 2:
            board[x][y-2] = ' '
            board[x][y-1] = ' '
            board[x][y] = ' '
            board[x][y+1] = ' '
            board[x][y+2] = ' '
        elif self.__shape == 3:
            board[x+1][y-1] = ' '
            board[x][y] = ' '
            board[x-1][y+1] = ' '