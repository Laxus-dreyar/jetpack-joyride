import signal
import os
import time
import ness

from Board import Field
from mando import Mandalorian
from Back import Background
from placing import place

r,c = os.popen('stty size','r').read().split()
rows = int(r)
columns = int(c)
game_board = Field(rows,2000)
game_board.create()
player = Mandalorian(rows-2,10)
player.place(game_board.grid,game_board.curscreen)

Back = Background()
place(game_board.grid)
# Back.create_ground(game_board.grid)
# Back.create_sky(game_board.grid)

while True:
    os.system('clear')
    game_board.print(columns)
    char = ness.user_input()
    if char == 'q':
        quit()
    elif char == 'd':
        player.move_right(game_board.grid,game_board.curscreen,rows,columns)
    elif char == 'a':
        player.move_left(game_board.grid,game_board.curscreen,rows,columns)
    if char == 'w':
        player.move_up(game_board.grid,game_board.curscreen,rows,columns)
    else:
        player.move_down(game_board.grid,game_board.curscreen,rows,columns)

    player.clearplayer(game_board.grid,game_board.curscreen)
    game_board.movescreen()
    player.place(game_board.grid,game_board.curscreen)
    