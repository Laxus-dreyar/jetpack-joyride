import signal
import os
import time
import ness
import placing
import math
import pyfiglet 

from Board import Field
from mando import Mandalorian
from Back import Background
from bullet import Bullet
from boss import Boss

os.system('reset')
r,c = os.popen('stty size','r').read().split()
# rows = 30
rows = int(r)-7
columns = int(c) -3 
game_board = Field(rows,800)
game_board.create()
player = Mandalorian(rows-3,10,game_board.get_grid())
player.place(game_board.get_grid(),0)

Back = Background(game_board.get_grid())
placing.place(game_board.get_grid(),rows)
Back.create_ground(game_board.get_grid(),rows)

bullets = []
bullets_forboss = []
enemy_bullets = []

tm = -1
tme_beg = time.time()

last_speedup = -1
speedup_flag = 0
magnet_flag = 0
bullet_fg = 0

boss = Boss(10,850,game_board.get_grid())
boss.make_shape()
boss.place(game_board.get_grid())
while True:
    for sk in range(columns):
        print('X',end='')
    cur_time = time.time()
    t_rem = 80 - int(cur_time - tme_beg)
    # print("\033[H\033[J")
    print('\033[0;0H')
    game_board.print(columns,player.ret_x(),player.ret_y())
    print("Lives: ",player.lives(),"Score: ",player.score(),"Time remaining: ",t_rem)

    char = ness.user_input()
    
    start_screen = game_board.get_curscreen()
    if start_screen < 750:

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
            player.move_right(game_board.get_grid(),start_screen,rows,columns)
        
        elif char == 'a':
            player.move_left(game_board.get_grid(),start_screen,rows,columns)
        
        elif char == 'b':
            x = player.ret_x()
            y = player.ret_y()
            new_bull = Bullet(x,y,game_board.get_grid())
            bullets.append(new_bull)

        if char == 'w':
            player.move_up(game_board.get_grid(),start_screen,rows,columns)
        
        else:
            x = player.ret_x()
            if x != rows-3:
                player.move_down(game_board.get_grid(),start_screen,rows,columns)


        for i in bullets:
            speed = game_board.get_speed()
            i.clear(game_board.get_grid(),start_screen,speed)
            i.move(columns,game_board.get_grid(),start_screen)
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
                    j.destroy(game_board.get_grid())
                    i.destroy(game_board.get_grid(),start_screen,speed)

            for j in placing.obs_type1_placed:
                obs_x = j.ret_x()
                obs_y = j.ret_y()
                obs_fg = j.get_flag()
                if(obs_fg == 1):
                    continue
                fg = i.flag_sts()
                if (obs_y -2 == y + start_screen or obs_y - 1 == y + start_screen or obs_y == y + start_screen or obs_y + 1 == y + start_screen or obs_y + 2 == y + start_screen) and fg == 0 and (x == obs_x or x == obs_x + 1 or x == obs_x -1):
                    j.destroy(game_board.get_grid())
                    i.destroy(game_board.get_grid(),start_screen,speed)
            
            for j in placing.obs_type3_placed:
                obs_x = j.ret_x()
                fg = i.flag_sts()
                obs_y = j.ret_y()
                obs_fg = j.get_flag()
                if(obs_fg == 1):
                    continue
                if ((obs_x == x or obs_x == x-1 or obs_x == x + 1) and (obs_y == y+start_screen or obs_y - 1 == y+start_screen or obs_y + 1== y+start_screen or obs_y + 2== y+start_screen or obs_y - 2== y+start_screen)) and fg == 0:
                    j.destroy(game_board.get_grid())
                    i.destroy(game_board.get_grid(),start_screen,speed)
            
            i.place(game_board.get_grid(),start_screen,columns,1)
        
        
        x = player.ret_x()
        y = player.ret_y() + start_screen
        if magnet_flag == 0:
            for i in placing.magnets:
                x1 = i.ret_x()
                y1 = i.ret_y()
                if y1 > start_screen and y1 < start_screen + columns:
                    if y > y1:
                        player.move_left(game_board.get_grid(),start_screen,rows,columns)
                    elif y < y1:
                        player.move_right(game_board.get_grid(),start_screen,rows,columns)
                    if x > x1:
                        player.move_up(game_board.get_grid(),start_screen,rows,columns)
                    elif x < x1:
                        player.move_down(game_board.get_grid(),start_screen,rows,columns)
                i.place(game_board.get_grid())
        
        player.clearplayer(game_board.get_grid(),start_screen)
        
        if player.lives() <= 0 or t_rem <= 0:
            os.system('reset')
            result = pyfiglet.figlet_format("Game over")
            result1 = pyfiglet.figlet_format("your final score")
            strin = str(player.score())
            result2 = pyfiglet.figlet_format(strin)
            print(result,result1,result2)
            quit()
        
        if player.ret_speedup() == 1 and speedup_flag == 0:
            game_board.inc_speed()
            last_speedup = time.time()
            speedup_flag = 1

        magnet_flag = magnet_flag + 1
        magnet_flag = magnet_flag%3

        game_board.movescreen()
        start_screen = game_board.get_curscreen()
        player.place(game_board.get_grid(),start_screen)
        if player.status_shield() == 1:
            tm1 = time.time()
            if tm1 - tm > 10:
                player.deactivate()
        
    else:
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
            player.move_right(game_board.get_grid(),start_screen,rows,math.floor(columns/2))
        
        elif char == 'a':
            player.move_left(game_board.get_grid(),start_screen,rows,math.floor(columns/2))
        
        elif char == 'b':
            x = player.ret_x()
            y = player.ret_y()
            new_bull = Bullet(x,y,game_board.get_grid())
            bullets_forboss.append(new_bull)

        if char == 'w':
            player.move_up(game_board.get_grid(),start_screen,rows,math.floor(columns/2))
        
        else:
            x = player.ret_x()
            if x != rows-3:
                player.move_down(game_board.get_grid(),start_screen,rows,math.floor(columns/2))
        
        
        x = boss.get_x()
        y = boss.get_y()
        size_boss = boss.get_size()
        if bullet_fg == 0:
            new_bull = Bullet(x,y-start_screen,game_board.get_grid())
            new_bull1 = Bullet(x+size_boss-2,y-start_screen,game_board.get_grid())
            enemy_bullets.append(new_bull)
            enemy_bullets.append(new_bull1)

        for i in bullets_forboss:
            bx = i.ret_x()
            by = i.ret_y() + start_screen
            fg = i.flag_sts()
            if (bx <= x + size_boss and bx >= x) and (by > y - 7) and fg == 0:
                i.destroy(game_board.get_grid(),start_screen,0)
                boss.decrease_life()
            i.clear(game_board.get_grid(),start_screen,0)
            i.move(columns,game_board.get_grid(),start_screen)
            i.place(game_board.get_grid(),start_screen,columns,1)
        
        for i in enemy_bullets:
            bx = i.ret_x()
            by = i.ret_y()
            fg = i.flag_sts()
            px = player.ret_x()
            py = player.ret_y()
            i.clear(game_board.get_grid(),start_screen,0)
            if (bx == px + 1 or bx == px or bx == px-1) and (by == py+1 or by == py-1 or by == py) and fg == 0:
                i.destroy(game_board.get_grid(),start_screen,0)
                player.decrease_Life()
            i.move2(columns,game_board.get_grid(),start_screen)
            i.place2(game_board.get_grid(),start_screen,columns,1)

        player.clearplayer(game_board.get_grid(),start_screen)
        boss.clear_boss(game_board.get_grid())

        if x >= player.ret_x():
            boss.move_up()
        elif x < player.ret_x():
            boss.move_down(rows)

        if player.lives() <= 0 or t_rem <= 0:
            os.system('reset')
            result = pyfiglet.figlet_format("Game over")
            result1 = pyfiglet.figlet_format("your final score")
            strin = str(player.score())
            result2 = pyfiglet.figlet_format(strin)
            print(result,result1,result2)
            quit()
        
        if boss.get_lives() == 0:
            os.system('reset')
            result = pyfiglet.figlet_format("You win")
            result1 = pyfiglet.figlet_format("your final score")
            strin = str(player.score() + math.floor(t_rem/5))
            result2 = pyfiglet.figlet_format(strin)
            print(result,result1,result2)
            quit()
            
        if player.ret_speedup() == 1 and speedup_flag == 0:
            game_board.inc_speed()
            last_speedup = time.time()
            speedup_flag = 1

        start_screen = game_board.get_curscreen()
        player.place(game_board.get_grid(),start_screen)
        bullet_fg = bullet_fg + 1
        bullet_fg = bullet_fg %20
        boss.place(game_board.get_grid())
        print("Boss lives: ",boss.get_lives())
        if player.status_shield() == 1:
            tm1 = time.time()
            if tm1 - tm > 10:
                player.deactivate()
        print()
    
    print()