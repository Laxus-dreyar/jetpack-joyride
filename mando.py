class Mandalorian:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__shape = [[" ","O"," "],["-","|","-"],["/"," ","\\"]]
        self.__life = 3
        self.__score = 0
    
    def place(self,board,start):
        for i in range(3):
            for j in range(3):
                board[self.__x + i - 1][self.__y + start + j - 1] = self.__shape[i][j]

    def clearplayer(self,board,start):
        for i in range(3):
            for j in range(3):
                board[self.__x + i - 1][self.__y + start + j - 1] = ' ' 

    def decrease_Life(self):
        self.__life = self.__life-1
        # self.clearplayer(board,start)
        # self.__x = rows-3
        # self.__y = 10

    def increase_score(self):
        self.__score = self.__score + 1

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