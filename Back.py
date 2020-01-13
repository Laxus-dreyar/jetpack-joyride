import pyautogui 
class Background:
    def __init__(self):
        self.__sky = "/"
        self.__ground = 'x'
    
    def create_sky(self,board):
        for i in range(2000):
            board[0][i] = self.__sky
    
    def create_ground(self,board,rows):
        for i in range(2000):
            board[rows-1][i] = self.__ground
