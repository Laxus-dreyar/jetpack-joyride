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
                board[self.__x + i - 1][self.__y + j - 1 - start] = self.__shape[i][j]
    def move_right(self):
        self.__x = self.__x + 1

    def move_left(self):
        self.__y = self.__y + 1