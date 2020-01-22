class Person:
    
    def __init__(self,x,y,board):
        self._x = x
        self._y = y
        self._shape = []
        self._lives = 3
        self._board = board

    def place(self,start,board1):
        board = self._board
        for i in range(3):
                for j in range(3):
                    board[self._x + i - 1][self._y + start + j - 1] = self._shape[i][j]
    
    def move_up(self):
        self.__x = self.__x - 1
        if self.__x < 1:
            self.__x = 1

    def move_down(self,rows):
        self.__x = self.__x + 1
        if self.__x > rows-15:
            self.__x = rows-15
    
    def decrease_Life(self):
        self._lives = self._lives-1