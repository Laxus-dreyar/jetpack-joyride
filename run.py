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
# rows = 30
# columns = 100
rows = int(r)
columns = int(c)
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
tme_beg = time.time()
last_speedup = -1
speedup_flag = 0
magnet_flag = 0
while True:
    cur_time = time.time()

    # print("\033[H\033[J")
    print('\033[0;0H')
    game_board.print(columns)
    print("Lives: ",player.lives(),"Score: ",player.score(),"Time remaining: ",200 - (cur_time - tme_beg))

    char = ness.user_input()
    
    if last_speedup != -1 and cur_time - last_speedup > 5 and speedup_flag == 1:
        player.dec_spped()
        game_board.dec_speed()
        speedup_flag = 0
    
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
        i.clear(game_board.grid,game_board.curscreen)
        i.move(columns,game_board.grid,game_board.curscreen)
        x = i.ret_x()
        y = i.ret_y()
        fg = i.flag_sts()
        if game_board.grid[x][y+game_board.curscreen] == '-':
            for j in placing.obs_type2_placed:
                obs_y = j.ret_y()
                if obs_y -2 == y + game_board.curscreen or obs_y - 1 == y + game_board.curscreen or obs_y == y + game_board.curscreen or obs_y + 1 == y + game_board.curscreen or obs_y + 2 == y + game_board.curscreen:
                    j.destroy(game_board.grid)
                    i.destroy(game_board.grid,game_board.curscreen)

        elif game_board.grid[x][y+game_board.curscreen] == '|' or game_board.grid[x][y+game_board.curscreen + 1] == '|' or game_board.grid[x][y+game_board.curscreen+2] == '|':
            for j in placing.obs_type1_placed:
                obs_x = j.ret_x()
                obs_y = j.ret_y()
                if obs_y -2 == y + game_board.curscreen or obs_y - 1 == y + game_board.curscreen or obs_y == y + game_board.curscreen or obs_y + 1 == y + game_board.curscreen or obs_y + 2 == y + game_board.curscreen:
                    j.destroy(game_board.grid)
                    i.destroy(game_board.grid,game_board.curscreen)
        
        elif game_board.grid[x][y+game_board.curscreen] == '/' or game_board.grid[x][y+game_board.curscreen+1] == '/' or game_board.grid[x][y+game_board.curscreen+2] == '/':
            for j in placing.obs_type3_placed:
                obs_x = j.ret_x()
                obs_y = j.ret_y()
                # print(obs_x,obs_y)
                # quit()
                if obs_x == x or obs_x == x-1 or obs_x == x + 1 or obs_y == y+game_board.curscreen or obs_y - 1 == y+game_board.curscreen or obs_y + 1== y+game_board.curscreen:
                    j.destroy(game_board.grid)
                    i.destroy(game_board.grid,game_board.curscreen)
        else:
            i.place(game_board.grid,game_board.curscreen,columns)
    
    # player.move_right(game_board.grid,game_board.curscreen,rows,columns)
    # player.move_up(game_board.grid,game_board.curscreen,rows,columns)
    
    x = player.ret_x()
    y = player.ret_y() + game_board.curscreen
    if magnet_flag == 0:
        for i in placing.magnets:
            x1 = i.ret_x()
            y1 = i.ret_y()
            if y1 > game_board.curscreen and y1 < game_board.curscreen + columns:
                if y > y1:
                    player.move_left(game_board.grid,game_board.curscreen,rows,columns)
                elif y < y1:
                    player.move_right(game_board.grid,game_board.curscreen,rows,columns)
                if x > x1:
                    player.move_up(game_board.grid,game_board.curscreen,rows,columns)
                elif x < x1:
                    player.move_down(game_board.grid,game_board.curscreen,rows,columns)
            i.place(game_board.grid)
    
    player.clearplayer(game_board.grid,game_board.curscreen)
    
    if player.lives() == 0:
        quit()
    if player.ret_speedup() == 1 and speedup_flag == 0:
        game_board.inc_speed()
        last_speedup = time.time()
        speedup_flag = 1

    
    if magnet_flag == 0:
        magnet_flag = 1
    else:
        magnet_flag = 0

    game_board.movescreen()
    player.place(game_board.grid,game_board.curscreen)
    if player.status_shield() == 1:
        tm1 = time.time()
        if tm1 - tm > 10:
            player.deactivate()