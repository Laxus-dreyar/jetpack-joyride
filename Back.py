import pyautogui 
class Background:
    def __init__(self):
        self.__sky = "/"
        self.__groundup = 'T'
        self.__grounddown = '-'
    
    def create_sky(self,board):
        for i in range(2000):
            board[0][i] = self.__sky
    
    def create_ground(self,board,rows):
        for i in range(2000):
            board[28][i] = self.__groundup
            board[29][i] = self.__grounddown
