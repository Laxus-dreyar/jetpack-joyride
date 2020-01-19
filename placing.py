import signal
import os
import time
import ness
import random

from Board import Field
from mando import Mandalorian
from Back import Background
from obstacles import Obstacle
from coin import Coin

obs_type1_placed = []
obs_type2_placed = []
obs_type3_placed = []
coins_placed = []

def space5(x,y,board):
    for i in range(5):
        for j in range(5):
            if board[x+i-2][y+j-2] != ' ':
                return True

def place(board,rows):
    i = 0
    while i < 25:
        x = random.randint(2,rows-6)
        y = random.randint(10,2000-50)
        if (space5(x-1,y,board)) or (space5(x-1,y,board)) or (space5(x-1,y,board)):
            continue
        obs_type1_placed.append(Obstacle(x,y,1))
        obs_type1_placed[i].place(board)
        i = i + 1

    i = 0
    while i < 25:
        x = random.randint(2,rows-6)
        y = random.randint(10,2000-50)
        if (space5(x,y-1,board)) or (space5(x,y,board)) or (space5(x,y+1,board)):
            i = i-1
            continue
        obs_type2_placed.append(Obstacle(x,y,2))
        obs_type2_placed[i].place(board)
        i = i + 1

    i = 0
    while i < 25:
        x = random.randint(2,rows-6)
        y = random.randint(10,2000-50)
        if (board[x-1][y+1] != ' ') or (board[x][y] != ' ') or (board[x+1][y-1] != ' '):
            i = i-1
            continue
        obs_type3_placed.append(Obstacle(x,y,3))
        obs_type3_placed[i].place(board)
        i = i + 1

    i = 0
    while i < 100:
        x = random.randint(2,rows-6)
        y = random.randint(10,2000-50)
        if board[x][y] != ' ':
            continue
        coins_placed.append(Coin(x,y))
        coins_placed[i].place(x,y,board)
        i = i + 1