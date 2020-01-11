import signal
import os
import time

from Board import Field
from mando import Mandalorian
from Back import Background

game_board = Field(30,2000)
game_board.create()

player = Mandalorian(26,10)
player.place(game_board.grid,0)

Back = Background()
Back.create_ground(game_board.grid)
Back.create_sky(game_board.grid)

game_board.print(0)