class Mandalorian:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__shape = [[" ","O"," "],["-","|","-"],["/"," ","\\"]]
        self.__life = 3
        self.__score = 0

    def start(self,grid):
        for i in range (25,28):
            for j in range (20,23,1):
                grid[i][j] = self.__shape[i-25][j-25]