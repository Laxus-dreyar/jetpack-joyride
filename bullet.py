import time
class Bullet:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__flag = 0

    def ret_x(self):
        return self.__x

    def ret_y(self):
        return self.__y

    def place(self,board,start,columns,flg):
        if self.__y > columns:
            self.__flag = 1
        x = self.__x
        y = self.__y
        if self.__y <= columns-1 and board[self.__x][self.__y + start] != '$' and self.__flag == 0 and board[self.__x][self.__y + start] != 'F' and board[self.__x][self.__y + start] != 'M' and flg == 1:
            board[self.__x][self.__y + start] = '*'

    
    def place2(self,board,start,columns,flg):
        if self.__y <= columns-1 and board[self.__x][self.__y + start] != '$' and self.__flag == 0 and board[self.__x][self.__y + start] != 'F' and board[self.__x][self.__y + start] != 'M' and flg == 1:
            board[self.__x][self.__y + start] = '*'

    def clear(self,board,start,speed):
        if board[self.__x][self.__y + start - speed] != '$' and self.__flag == 0:
            board[self.__x][self.__y + start - speed] = ' '
    
    def flag_sts(self):
        return self.__flag

    def move(self,columns,board,start):
        self.__y = self.__y + 3

    def move2(self,columns,board,start):
        self.__y = self.__y - 3
        if self.__y < 0:
            self.__y = -2
        # print("moving",self.__y+start)

    def destroy(self,board,start,speed):
        self.clear(board,start,speed)
        self.__flag = 1