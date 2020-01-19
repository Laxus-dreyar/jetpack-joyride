class Bullet:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__flag = 0

    def ret_x(self):
        return self.__x

    def ret_y(self):
        return self.__y
    def place(self,board,start):
        board[self.__x][self.__y + start] = '*'

    def clear(self,board,start):
        board[self.__x][self.__y + start] = ' '

    def update(self):
        self.__flag = 1
    
    def move(self,columns,board,start):
        self.__y = self.__y + 1
        if self.__y <= columns-1 and board[self.__x][self.__y + start] != '$' and self.__flag == 0:
            self.place(board,start)
        else:
            self.clear(board,start)