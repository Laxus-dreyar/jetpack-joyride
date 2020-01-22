import time
from peron import Person
import math
class Mandalorian(Person):

    def __init__(self,x,y,board):
        Person.__init__(self,x,y,board)
        self._shape = [[" ","O"," "],["-","|","-"],["/"," ","\\"]]
        self.__shape1 = [["\\","O","/"],["|"," ","|"],["/"," ","\\"]]
        self.__score = 0
        self.__shield = 0
        self.__decreaselftime = -1
        self.__speedup = 0
        self.__timedown = int(time.time())
        self.__last = 0

    def increase_score(self):
        self.__score = self.__score + 1

    def inc_speed(self):
        self.__speedup = 1

    def dec_spped(self):
        self.__speedup = 0

    def place(self,board1,start):
        board = self._board
        flg = 0
        if self.__shield == 0:
            for i in range(3):
                for j in range(3):
                    if board[self._x + i - 1][self._y + start + j - 1] == '|' or board[self._x + i - 1][self._y + start + j - 1] == '-' or board[self._x + i - 1][self._y + start + j - 1] == '/':
                        if flg == 0:
                            self.decrease_Life()
                            board[self._x + i - 1][self._y + start + j - 1] = ' '
                            board[self._x + i - 1][self._y + start + j] = ' '
                            board[self._x + i - 1][self._y + start + j + 1] = ' '
                            flg = 1

                    elif board[self._x + i - 1][self._y + start + j - 1] == '$':
                        self.increase_score()
                    elif board[self._x + i - 1][self._y + start + j - 1] == 'F':
                        self.inc_speed()
                    board[self._x + i - 1][self._y + start + j - 1] = self._shape[i][j]
        
        else:
            for i in range(3):
                for j in range(3):
                    board[self._x + i - 1][self._y + start + j - 1] = self.__shape1[i][j]

    def activate(self):
        self.__shield = 1
    
    def status_shield(self):
        return self.__shield

    def deactivate(self):
        self.__shield = 0

    def clearplayer(self,board1,start):
        board = self._board
        for i in range(3):
            for j in range(3):
                board[self._x + i - 1][self._y + start + j - 1] = ' ' 
                
    def check(self,start,rows,columns):

        if self._y > columns - 2:
            self._y = columns - 2

        if self._y <  2:
            self._y = 2

        if self._x < 3:
            self._x = 3

        if self._x > rows-3:
            self._x = rows-3
    
    def move_right(self,board1,start,rows,columns):
        board = self._board
        self.clearplayer(board,start)
        self._y = self._y + 2
        self.check(start,rows,columns)
        self.place(board,start)

    def move_left(self,board1,start,rows,columns):
        board = self._board
        self.clearplayer(board,start)
        self._y = self._y - 2
        self.check(start,rows,columns)
        self.place(board,start)

    def move_up(self,board1,start,rows,columns):
        board = self._board
        self.clearplayer(board,start)
        self._x = self._x - 2
        self.check(start,rows,columns)
        self.place(board,start)
        self.__timedown = time.time()
        self.__last = self._x

    def move_down(self,board1,start,rows,columns):
        board = self._board
        t = (time.time() - self.__timedown)
        self.clearplayer(board,start)
        self._x = self.__last + math.ceil(4*t*t)
        # self._x = self._x + 1
        self.check(start,rows,columns)
        self.place(board,start)

    def ret_x(self):
        return int(self._x)
    
    def ret_y(self):
        return int(self._y)

    def lives(self):
        return int(self._lives)
    
    def score(self):
        return int(self.__score)

    def ret_speedup(self):
        return (int)(self.__speedup)