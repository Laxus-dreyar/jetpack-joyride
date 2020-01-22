from colorama import Fore,Back,Style
class Field:

    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = 20000
        self.grid = []
        self.__curscreen = 0
        self.__speed = 1

    def create(self):
        for i in range(self.__rows):
            arr = []
            for j in range(self.__columns):
                arr.append(" ")
            self.grid.append(arr)

    def print(self,columns,x,y):
        start = self.__curscreen
        for i in range(self.__rows):
            for j in range(start,start+columns):
                if (i == x+1 or i == x or i==x-1) and (j == y+1+self.__curscreen or j == y+self.__curscreen or j == y+self.__curscreen-1):
                    print(Fore.WHITE + self.grid[i][j],end='')
                elif self.grid[i][j] == '$':
                    print(Fore.YELLOW + '$',end='')
                elif self.grid[i][j] == '-' or self.grid[i][j] == '/' or self.grid[i][j] == '|' or self.grid[i][j] == '*':
                    print(Fore.RED + self.grid[i][j],end='')
                elif self.grid[i][j] == 'M' or self.grid[i][j] == 'F':
                    print(Fore.BLUE + self.grid[i][j],end='')
                else:
                    print(Fore.WHITE + self.grid[i][j],end='')
            print()
    
    def movescreen(self):
        self.__curscreen = self.__curscreen + self.__speed
        if self.__curscreen > 750:
            self.__curscreen =750
            self.__speed = 0

    def change_screen(self):
        self.__curscreen = 0

    def inc_speed(self):
        self.__speed = self.__speed + 1
    
    def dec_speed(self):
        self.__speed = self.__speed - 1

    def get_curscreen(self):
        return self.__curscreen

    def get_speed(self):
        return self.__speed