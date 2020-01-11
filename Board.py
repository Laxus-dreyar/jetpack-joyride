class Field:

    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = columns
        self.__grid = []

    def create(self):
        for i in range(self.__rows):
            arr = []
            for j in range(self.__columns):
                arr.append(" ")
            self.__grid.append(arr)

    def print(self,start):
        for i in range(self.__rows):
            for j in range(start,start+100):
                print(self.__grid[i][j],end='')
            print()