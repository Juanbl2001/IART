# Using A*
# Cost -> Number of moves until it reaches the exit
# Heuristic -> Manhattan distance

from utils import *


def bot(test, testInit):



def heuristic(robotPos, maze):

    exit = get_exit_pos(maze)
    
    h = abs(robotPos[0] - exit[0]) + abs(robotPos[1] - exit[1])

    return h

def cost(robotPos, maze):
    
