import signal
import os
import time
import ness
import placing
import math

from Board import Field
from mando import Mandalorian
from Back import Background
from bullet import Bullet

r,c = os.popen('stty size','r').read().split()
rows = int(r)-5
columns = int(c) -3 
game_board = Field(rows,2000)
game_board.create()
player = Mandalorian(rows-3,10)
player.place(game_board.grid,0)

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
    print("Lives: ",player.lives(),"Score: ",player.score(),"Time remaining: ",200 - int(cur_time - tme_beg))

    char = ness.user_input()
    
    start_screen = game_board.get_curscreen()

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
        player.move_right(game_board.grid,start_screen,rows,columns)
    
    elif char == 'a':
        player.move_left(game_board.grid,start_screen,rows,columns)
    
    elif char == 'b':
        x = player.ret_x()
        y = player.ret_y()
        new_bull = Bullet(x,y)
        bullets.append(new_bull)

    if char == 'w':
        player.move_up(game_board.grid,start_screen,rows,columns)
    
    else:
        x = player.ret_x()
        if x != rows-3:
            player.move_down(game_board.grid,start_screen,rows,columns)


    for i in bullets:
        speed = game_board.get_speed()
        i.clear(game_board.grid,start_screen,speed)
        i.move(columns,game_board.grid,start_screen)
        x = i.ret_x()
        y = i.ret_y()
        fg = i.flag_sts()
        for j in placing.obs_type2_placed:
            obs_y = j.ret_y()
            obs_x = j.ret_x()
            obs_fg = j.get_flag()
            if(obs_fg == 1):
                continue
            fg = i.flag_sts()
            if (obs_y -2 == y + start_screen or obs_y - 1 == y + start_screen or obs_y == y + start_screen or obs_y + 1 == y + start_screen or obs_y + 2 == y + start_screen) and fg == 0 and x == obs_x:
                j.destroy(game_board.grid)
                i.destroy(game_board.grid,start_screen,speed)

        for j in placing.obs_type1_placed:
            obs_x = j.ret_x()
            obs_y = j.ret_y()
            obs_fg = j.get_flag()
            if(obs_fg == 1):
                continue
            fg = i.flag_sts()
            if (obs_y -2 == y + start_screen or obs_y - 1 == y + start_screen or obs_y == y + start_screen or obs_y + 1 == y + start_screen or obs_y + 2 == y + start_screen) and fg == 0 and (x == obs_x or x == obs_x + 1 or x == obs_x -1):
                j.destroy(game_board.grid)
                i.destroy(game_board.grid,start_screen,speed)
        
        for j in placing.obs_type3_placed:
            obs_x = j.ret_x()
            fg = i.flag_sts()
            obs_y = j.ret_y()
            obs_fg = j.get_flag()
            if(obs_fg == 1):
                continue
            if ((obs_x == x or obs_x == x-1 or obs_x == x + 1) and (obs_y == y+start_screen or obs_y - 1 == y+start_screen or obs_y + 1== y+start_screen or obs_y + 2== y+start_screen or obs_y - 2== y+start_screen)) and fg == 0:
                j.destroy(game_board.grid)
                i.destroy(game_board.grid,start_screen,speed)
        
        i.place(game_board.grid,start_screen,columns)
    
    
    x = player.ret_x()
    y = player.ret_y() + start_screen
    if magnet_flag == 0:
        for i in placing.magnets:
            x1 = i.ret_x()
            y1 = i.ret_y()
            if y1 > start_screen and y1 < start_screen + columns:
                if y > y1:
                    player.move_left(game_board.grid,start_screen,rows,columns)
                elif y < y1:
                    player.move_right(game_board.grid,start_screen,rows,columns)
                if x > x1:
                    player.move_up(game_board.grid,start_screen,rows,columns)
                elif x < x1:
                    player.move_down(game_board.grid,start_screen,rows,columns)
            i.place(game_board.grid)
    
    player.clearplayer(game_board.grid,start_screen)
    
    if player.lives() == 0:
        quit()
    if player.ret_speedup() == 1 and speedup_flag == 0:
        game_board.inc_speed()
        last_speedup = time.time()
        speedup_flag = 1

    magnet_flag = magnet_flag + 1
    magnet_flag = magnet_flag%3

    game_board.movescreen()
    start_screen = game_board.get_curscreen()
    player.place(game_board.grid,start_screen)
    if player.status_shield() == 1:
        tm1 = time.time()
        if tm1 - tm > 10:
            player.deactivate()