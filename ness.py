import signal
import os
import time

from Board import Field
from mando import Mandalorian
from Back import Background
from alarmexeption import AlarmException
from getChar import _getChUnix as getChar

def alarmhandler(signum, frame):
    raise AlarmException

def user_input(timeout=0.1):
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

def check_collision(x,y,board):

    if board[x][y] == ' ':
        return int(0)
    elif board[x][y] == '$':
        return int(1)
    elif board[x][y] == '|' or board[x][y] == '-' or board[x][y] == '/':
        return int(2)