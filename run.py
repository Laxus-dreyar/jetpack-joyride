import signal
import os
import time
import ness

from Board import Field
from mando import Mandalorian
from Back import Background

game_board = Field(30,2000)
game_board.create()

player = Mandalorian(26,10)
player.place(game_board.grid,0)

Back = Background()
# Back.create_ground(game_board.grid)
# Back.create_sky(game_board.grid)

while True:
    os.system('clear')
    game_board.print(0)
    char = ness.user_input()
    if char == 'q':
        quit()
    elif char == 'd':
        player.move_right(game_board.grid,0)
    elif char == 'a':
        player.move_left(game_board.grid,0)
    if char == 'w':
        player.move_up(game_board.grid,0)
    else:
        player.move_down(game_board.grid,0)
    player.place(game_board.grid,0)