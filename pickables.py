class Pickable:

    def __init__(self,x,y,shape,board):
        self._x = x
        self._y = y
        self._shape = shape
        self._flag = 0
        self._board = board
        self._ch = '-'

    def place(self,board1):
        board = self.__board
        x = self.__x
        y = self.__y
        if self.__shape == 1:
            board[x-1][y] = self._ch
            board[x][y] = self._ch
            board[x+1][y] = self._ch