# Using A*
# Cost -> Number of moves until it reaches the exit
# Heuristic -> Manhattan distance

from utils import *
from main import *


valueCost = 0


def heuristic(robotPos, maze):

    exit = testFin
    
    h = abs(robotPos[0] - exit[0]) + abs(robotPos[1] - exit[1])

    return h

def addCost():
    valueCost+=1

def getCost():
    return valueCost
    
