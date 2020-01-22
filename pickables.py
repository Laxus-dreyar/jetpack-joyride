class Pickable:

    def __init__(self,x,y,shape,board):
        self._x = x
        self._y = y
        self._shape = shape
        self._flag = 0
        self._board = board
        self._ch = '-'

    def place(self,board1):
        board = self._board
        x = self._x
        y = self._y
        board[x-1][y] = self._ch
        board[x][y] = self._ch
        board[x+1][y] = self._ch

    def ret_x(self):
        return self._x
    
    def ret_y(self):
        return self._y

    def get_flag(self):
        return self._flag
    
    def destroy(self,board1):
        board = self._board
        x = self._x
        y = self._y
        board[x-1][y] = ' '
        board[x][y] = ' '
        board[x+1][y] = ' '