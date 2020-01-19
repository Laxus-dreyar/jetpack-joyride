class Field:

    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = 20000
        self.grid = []
        self.curscreen = 0

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
        self.curscreen = self.curscreen + 1

    def change_screen(self):
        self.curscreen = 0

    def upd(self,lives,score):
        self.grid[0][self.curscreen] = "Lives: "
        self.grid[0][self.curscreen + 1] = lives
        self.grid[1][self.curscreen] = "Score: "
        self.grid[1][self.curscreen + 1] = score