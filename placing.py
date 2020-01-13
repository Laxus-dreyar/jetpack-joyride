import signal
import os
import time
import ness
import random

from Board import Field
from mando import Mandalorian
from Back import Background
from obstacles import Obstacle

obs_type1_placed = []
def place(board):
    for i in range(50):
        x = random.randint(2,26)
        y = random.randint(10,2000-50)
        if (board[x-1][y] != ' ') or (board[x][y] != ' ') or (board[x+1][y] != ' '):
            i = i-1
        obs_type1_placed.append(Obstacle(x,y,1))
        obs_type1_placed[i].place(x,y,1,board)