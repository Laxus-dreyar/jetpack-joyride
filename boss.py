from peron import Person
class Boss(Person):

    def __init__(self,x,y,board):
        self.__size = []
        Person.__init__(self,x,y,board)

    def make_shape(self):
        drg = open("dragon.txt")
        for i in drg:
            arr = []
            for j in i:
                if j!='\n':
                    arr.append(j)
            self._shape.append(arr)
    
    def clear_boss(self,board):
        x=self._x
        y=self._y
        for i in self._shape:
            for j in i:
                board[x][y] = ' '
                y = y + 1
            x = x+1
            y = self._y

    def place(self,board1):
        board = self._board
        x=self._x
        y=self._y
        for i in self._shape:
            for j in i:
                board[x][y] = j
                y = y + 1
            x = x+1
            y = self._y
        self.__size = x - self._x
    
    def move_up(self):
        self._x = self._x - 1
        if self._x < 1:
            self._x = 1

    def move_down(self,rows):
        self._x = self._x + 1
        if self._x > rows-15:
            self._x = rows-15
    
    def get_size(self):
        return self.__size
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_lives(self):
        return self._lives