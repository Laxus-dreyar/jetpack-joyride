import time
class Mandalorian:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__shape = [[" ","O"," "],["-","|","-"],["/"," ","\\"]]
        self.__shape1 = [["\\","O","/"],["|"," ","|"],["/"," ","\\"]]
        self.__life = 3
        self.__score = 0
        self.__shield = 0
        self.__decreaselftime = -1
        self.__speedup = 0
    
    def decrease_Life(self):
        now = time.time()
        self.__life = self.__life-1
        self.__decreaselftime = now

    def increase_score(self):
        self.__score = self.__score + 1

    def inc_speed(self):
        self.__speedup = 1

    def dec_spped(self):
        self.__speedup = 0
    def place(self,board,start):
        flg = 0
        if self.__shield == 0:
            for i in range(3):
                for j in range(3):
                    if board[self.__x + i - 1][self.__y + start + j - 1] == '|' or board[self.__x + i - 1][self.__y + start + j - 1] == '-' or board[self.__x + i - 1][self.__y + start + j - 1] == '/':
                        if flg == 0:
                            self.decrease_Life()
                            board[self.__x + i - 1][self.__y + start + j - 1] = ' '
                            board[self.__x + i - 1][self.__y + start + j] = ' '
                            board[self.__x + i - 1][self.__y + start + j + 1] = ' '
                            flg = 1

                    elif board[self.__x + i - 1][self.__y + start + j - 1] == '$':
                        self.increase_score()
                    elif board[self.__x + i - 1][self.__y + start + j - 1] == 'M':
                        self.inc_speed()
                    board[self.__x + i - 1][self.__y + start + j - 1] = self.__shape[i][j]
        
        else:
            for i in range(3):
                for j in range(3):
                    board[self.__x + i - 1][self.__y + start + j - 1] = self.__shape1[i][j]

    def activate(self):
        self.__shield = 1
    
    def status_shield(self):
        return self.__shield

    def deactivate(self):
        self.__shield = 0

    def clearplayer(self,board,start):
        for i in range(3):
            for j in range(3):
                board[self.__x + i - 1][self.__y + start + j - 1] = ' ' 
                
    def check(self,start,rows,columns):

        if self.__y > columns - 2:
            self.__y = columns - 2

        if self.__y <  2:
            self.__y = 2

        if self.__x < 4:
            self.__x = 4

        if self.__x > rows-3:
            self.__x = rows-3
    
    def move_right(self,board,start,rows,columns):
        self.clearplayer(board,start)
        self.__y = self.__y + 2
        self.check(start,rows,columns)
        self.place(board,start)

    def move_left(self,board,start,rows,columns):
        self.clearplayer(board,start)
        self.__y = self.__y - 2
        self.check(start,rows,columns)
        self.place(board,start)

    def move_up(self,board,start,rows,columns):
        self.clearplayer(board,start)
        self.__x = self.__x - 2
        self.check(start,rows,columns)
        self.place(board,start)

    def move_down(self,board,start,rows,columns):
        self.clearplayer(board,start)
        self.__x = self.__x + 1
        self.check(start,rows,columns)
        self.place(board,start)

    def ret_x(self):
        return int(self.__x)
    
    def ret_y(self):
        return int(self.__y)

    def lives(self):
        return int(self.__life)
    
    def score(self):
        return int(self.__score)

    def ret_speedup(self):
        return (int)(self.__speedup)