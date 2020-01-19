import signal
import os
import time
import ness
import placing

from Board import Field
from mando import Mandalorian
from Back import Background
from bullet import Bullet

r,c = os.popen('stty size','r').read().split()
rows = 30
columns = 100
game_board = Field(rows,2000)
game_board.create()
player = Mandalorian(rows-3,10)
player.place(game_board.grid,game_board.curscreen)

Back = Background()
placing.place(game_board.grid,rows)
Back.create_ground(game_board.grid,rows)
# Back.create_sky(game_board.grid)
bullets = []
tm = -1
while True:
    print("\033[H\033[J")
    game_board.print(columns)
    char = ness.user_input()
    if char == 'q':
        quit()
    if char == ' ':
        tm1 = time.time()
        if player.status_shield() == 0 and (tm == -1 or tm1 - tm > 60):
            player.activate()
            tm = time.time()

    elif char == 'd':
        player.move_right(game_board.grid,game_board.curscreen,rows,columns)
    
    elif char == 'a':
        player.move_left(game_board.grid,game_board.curscreen,rows,columns)
    
    elif char == 'b':
        x = player.ret_x()
        y = player.ret_y()
        new_bull = Bullet(x,y)
        bullets.append(new_bull)

    if char == 'w':
        player.move_up(game_board.grid,game_board.curscreen,rows,columns)
    
    else:
        x = player.ret_x()
        if x != rows-3:
            player.move_down(game_board.grid,game_board.curscreen,rows,columns)

    for i in bullets:
        x = i.ret_x()
        y = i.ret_y()
        i.clear(game_board.grid,game_board.curscreen)
        i.move(columns,game_board.grid,game_board.curscreen)
        if game_board.grid[x][y+game_board.curscreen + 1] == '-':
            for j in placing.obs_type2_placed:
                obs_y = j.ret_y()
                if obs_y == y + game_board.curscreen + 3:
                    j.destroy(game_board.grid)
                    i.destroy(game_board.grid,game_board.curscreen)
        elif game_board.grid[x][y+game_board.curscreen + 1] == '|':
            for j in placing.obs_type1_placed:
                obs_x = j.ret_x()
                obs_y = j.ret_y()
                print(obs_y,obs_x)
                quit()
                if obs_x == x or obs_x == x-1 or obs_x == x+1 or j == obs_y:
                    j.destroy(game_board.grid)
                    i.destroy(game_board.grid,game_board.curscreen)
        else:
            i.place(game_board.grid,game_board.curscreen,columns)

    player.clearplayer(game_board.grid,game_board.curscreen)
    if player.lives() == 0:
        quit()
    game_board.movescreen()
    player.place(game_board.grid,game_board.curscreen)
    game_board.upd(player.lives(),player.score())
    if player.status_shield() == 1:
        tm1 = time.time()
        if tm1 - tm > 10:
            player.deactivate()