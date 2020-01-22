class Boss:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__shape = []
        self.__size = []
        self.__lives = 3

    def make_shape(self):
        drg = open("dragon.txt")
        for i in drg:
            arr = []
            for j in i:
                if j!='\n':
                    arr.append(j)
            self.__shape.append(arr)
    
    def clear_boss(self,board):
        x=self.__x
        y=self.__y
        for i in self.__shape:
            for j in i:
                board[x][y] = ' '
                y = y + 1
            x = x+1
            y = self.__y

    def place(self,board):
        x=self.__x
        y=self.__y
        for i in self.__shape:
            for j in i:
                board[x][y] = j
                y = y + 1
            x = x+1
            y = self.__y
        self.__size = x - self.__x
    
    def move_up(self):
        self.__x = self.__x - 1
        if self.__x < 3:
            self.__x = 3

    def move_down(self,rows):
        self.__x = self.__x + 1
        if self.__x > rows-15:
            self.__x = rows-15
    
    def get_size(self):
        return self.__size
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def decrease_life(self):
        self.__lives = self.__lives - 1
    
    def get_lives(self):
        return self.__lives