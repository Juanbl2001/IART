# Using A*
# Cost -> Number of moves until it reaches the exit
# Heuristic -> Manhattan distance

from cmath import sqrt
from curses import nl
from importlib.resources import path
from lib2to3.pgen2.token import NEWLINE
from queue import *
from time import sleep
from moves import *
from utils import *
import math

valueCost = 0


def linDist(robotPos, finalPos):

    h = sqrt((abs(robotPos[0] - finalPos[0]))^2 + (abs(robotPos[0] - finalPos[0]))^2 ^ 2)
    return h


def manDist(robotPos, finalPos):

    h = abs(robotPos[0] - finalPos[0]) + abs(robotPos[1] - finalPos[1])

    return h


def addCost():
    valueCost += 1


def eucDist(robotPos, finalPos):

    h = math.dist(robotPos, finalPos)
    return h


def getCost():
    return valueCost


def dfs(position, destination, maze, visited=None, path=None):

    if visited is None:
        visited = []
    if path is None:
        path = []

    visited.append(position)
    path.append(position)

    if position[0] == destination[0] and position[1] == destination[1]:
        print(path)
        return path

    neighbours = check(position, maze)

    for neighbour in neighbours:
        if neighbour not in visited:
            dfs(neighbour, destination, maze, visited, path)
    return None

"""
#Antigo BFS
def bfs(start, goal, maze):

    queue = []

    queue.append([start])
    while queue:

        path = queue.pop(0)

        node = path[-1]

        if node == goal:
            return path

        for neighbour in check(node, maze):
            new_path = list(path)
            new_path.append(neighbour)
            queue.append(new_path)
"""

def newBfs(start, goal, maze):

    queue = []
    queue.append(["L"])
    queue.append(["R"])
    queue.append(["U"])
    queue.append(["D"])

    while queue:

        seq = queue.pop(0)
        # print(seq)
        aux = [start[0], start[1]]
        if goal == move(seq, aux, goal, maze):
            return seq

        for movDir in ["L", "R", "U", "D"]:
            newSeq = list(seq)
            newSeq.append(movDir)
            queue.append(newSeq)


def greedy(start, goal, maze, sizeOfAnswer):

    queue = []
    queue.append(["L"])
    queue.append(["R"])
    queue.append(["U"])
    queue.append(["D"])

    while queue:
        count+=1
        heuristic = 999.0
        for i in range(len(queue)):
            aux = [start[0], start[1]] #so the initial Position doesn't get altered
            lastPos = move(queue[i], aux, goal, maze) #get last position achievable with that sequence

            auxHeuristic = eucDist(lastPos, goal) #calculate the heuristic from that last position achieved
            if(auxHeuristic <= heuristic):
                if(auxHeuristic == heuristic and len(queue[i]) > len(bestSeq) and i != 0):
                    continue
                else:
                    heuristic = auxHeuristic
                    bestSeq = queue[i]
                    bestPos = lastPos
            
        queue.remove(bestSeq)

        #checks depth
        if goal == bestPos:
            print(count)
            print(bestSeq)
            return bestSeq

        for movDir in ["L", "R", "U", "D"]:
            newSeq = list(bestSeq)
            newSeq.append(movDir)
            queue.append(newSeq)
