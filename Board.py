class Field:

    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = 20000
        self.grid = []
        self.curscreen = 0
        self.__speed = 1

    def create(self):
        for i in range(self.__rows):
            arr = []
            for j in range(self.__columns):
                arr.append(" ")
            self.grid.append(arr)

    def print(self,columns):
        start = self.curscreen
        for i in range(self.__rows):
            for j in range(start,start+columns):
                print(self.grid[i][j],end='')
            print()
    
    def movescreen(self):
        self.curscreen = self.curscreen + self.__speed

    def change_screen(self):
        self.curscreen = 0

    def inc_speed(self):
        self.__speed = self.__speed + 1
    
    def dec_speed(self):
        self.__speed = self.__speed - 1

    def get_curscreen(self):
        return self.curscreen

    def get_speed(self):
        return self.__speed