import signal
import os
import time
import ness

from Board import Field
from mando import Mandalorian
from Back import Background
from placing import place

r,c = os.popen('stty size','r').read().split()
rows = 30
columns = 100
game_board = Field(rows,2000)
game_board.create()
player = Mandalorian(rows-3,10)
player.place(game_board.grid,game_board.curscreen)

Back = Background()
place(game_board.grid,rows)
Back.create_ground(game_board.grid,rows)
# Back.create_sky(game_board.grid)
tm = -1
while True:
    os.system('clear')
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
        x = player.ret_x()
        y = player.ret_y() + game_board.curscreen
        if ness.check_collision(x,y+2,game_board.grid) == 2 or ness.check_collision(x+1,y+2,game_board.grid) == 2 or ness.check_collision(x-1,y+2,game_board.grid) == 2:
            if player.status_shield() == 0:
                player.decrease_Life()
        
        elif ness.check_collision(x,y+2,game_board.grid) == 1 or ness.check_collision(x+1,y+2,game_board.grid) == 1 or ness.check_collision(x-1,y+2,game_board.grid) == 1:
            player.increase_score()
        
        player.move_right(game_board.grid,game_board.curscreen,rows,columns)
    
    elif char == 'a':
        x = player.ret_x()
        y = player.ret_y() + game_board.curscreen
        if ness.check_collision(x,y-2,game_board.grid) == 2 or ness.check_collision(x+1,y-2,game_board.grid) == 2 or ness.check_collision(x-1,y-2,game_board.grid) == 2:
            if player.status_shield() == 0:
                player.decrease_Life()
        elif ness.check_collision(x,y-2,game_board.grid) == 1 or ness.check_collision(x+1,y-2,game_board.grid) == 1 or ness.check_collision(x-1,y-2,game_board.grid) == 1:
            player.increase_score()
    
        player.move_left(game_board.grid,game_board.curscreen,rows,columns)
    
    if char == 'w':
        x = player.ret_x()
        y = player.ret_y() + game_board.curscreen
        if ness.check_collision(x-1,y,game_board.grid) == 2 or ness.check_collision(x-1,y-1,game_board.grid) == 2 or ness.check_collision(x-1,y+1,game_board.grid) == 2:
            if player.status_shield() == 0:
                player.decrease_Life()
        if ness.check_collision(x-1,y,game_board.grid) == 1 or ness.check_collision(x-1,y-1,game_board.grid) == 1 or ness.check_collision(x-1,y+1,game_board.grid) == 1:
            player.increase_score()
    
        player.move_up(game_board.grid,game_board.curscreen,rows,columns)
    
    else:
        x = player.ret_x()
        if x != rows-3:
            
            # y = player.ret_y() + game_board.curscreen
            # if ness.check_collision(x+1,y,game_board.grid) == 2 or ness.check_collision(x+1,y-1,game_board.grid) == 2 or ness.check_collision(x+1,y+1,game_board.grid) == 2:
            #     player.decrease_Life()
            # elif ness.check_collision(x+1,y,game_board.grid) == 2 or ness.check_collision(x+1,y-1,game_board.grid) == 2 or ness.check_collision(x+1,y+1,game_board.grid) == 2:
            #     player.increase_score()
        
            player.move_down(game_board.grid,game_board.curscreen,rows,columns)

    x = player.ret_x()
    y = player.ret_y() + game_board.curscreen
    player.clearplayer(game_board.grid,game_board.curscreen)
    if ness.check_collision(x,y+2,game_board.grid) == 2 or ness.check_collision(x+1,y+2,game_board.grid) == 2 or ness.check_collision(x-1,y+2,game_board.grid) == 2:
        if player.status_shield() == 0:
                player.decrease_Life()
    elif ness.check_collision(x,y+2,game_board.grid) == 1 or ness.check_collision(x+1,y+2,game_board.grid) == 1 or ness.check_collision(x-1,y+2,game_board.grid) == 1:
        player.increase_score()
    if player.lives() == 0:
        quit()
    game_board.movescreen()
    player.place(game_board.grid,game_board.curscreen)
    game_board.upd(player.lives(),player.score())
    if player.status_shield() == 1:
        tm1 = time.time()
        if tm1 - tm > 10:
            player.deactivate()