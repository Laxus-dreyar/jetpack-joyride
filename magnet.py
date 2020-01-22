class Magnet():

    def __init__(self,x,y,board):
        self.__x = x
        self.__y = y
        self.__board = board

    def place(self,board1):
        board = self.__board
        x = self.__x
        y = self.__y
        board[x][y] = 'M'

    def make_field(self,board):
        # board = self.__board
        x = self.__x
        y = self.__y
        for i in range(7):
            for j in range(7):
                if i < 3 and j < 3:
                    board[x+i-3][y+j-3] = 1
                    # print(x+i-3)
                elif i < 3 and j > 3:
                    board[x+i-3][y+j-3] = 2
                elif i > 3 and j < 3:
                    board[x+i-3][y+j-3] = 3
                elif i > 3 and j > 3:
                    board[x+i-3][y+j-3] = 4
                elif i == 3 and j < 3:
                    board[x+i-3][y+j-3] = 5
                elif i == 3 and j > 3:
                    board[x+i-3][y+j-3] = 6
                elif i < 3 and j == 3:
                    board[x+i-3][y+j-3] = 7
                elif i > 3 and j == 3:
                    board[x+i-3][y+j-3] = 8
                elif i == 3 and j == 3:
                    board[x+i-3][y+j-3] = 9

    def ret_x(self):
        return self.__x
    def ret_y(self):
        return self.__y