# Using A*
# Cost -> Number of moves until it reaches the exit
# Heuristic -> Manhattan distance

from importlib.resources import path
from queue import *
from moves import *
from utils import *
import math

valueCost = 0


def linDist(robotPos, finalPos):

    h = ((robotPos[0] - finalPos[0]) ^ 2 +
         (robotPos[1] - finalPos[1]) ^ 2) ^ 0.5

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


def greedy(start, goal, maze):

    queue = []
    queue.append(["L"])
    queue.append(["R"])
    queue.append(["U"])
    queue.append(["D"])

    

    while queue:
        heuristic = 9999
        for i in queue:
            aux = [start[0], start[1]] #so the initial Position doesn't get altered
            lastPos = move(i, aux, goal, maze) #get last position achievable with that sequence
            auxHeuristic = manDist(lastPos, goal) #calculate the heuristic from that last position achieved
            if(auxHeuristic < heuristic): 
                heuristic = auxHeuristic
                bestSeq = i
                bestPos = lastPos
        
        queue.remove(bestSeq)
        
        aux = [start[0], start[1]]
        if goal == bestPos:
            return bestSeq

        for movDir in ["L", "R", "U", "D"]:
            newSeq = list(bestSeq)
            newSeq.append(movDir)
            queue.append(newSeq)


def getRight(pos,maze):
    if(maze[pos[0]][pos[1]][3]==0):
        return [pos[0],pos[1]+1]
    else:
        return [pos[0],pos[1]]

def getLeft(pos,maze):
    if(maze[pos[0]][pos[1]][2]==0):
        return [pos[0],pos[1]-1]
    else:
        return [pos[0],pos[1]]

def getUp(pos,maze):
    if(maze[pos[0]][pos[1]][0]==0):
        return [pos[0]-1,pos[1]]
    else:
        return [pos[0],pos[1]]

def getDown(pos,maze):
    if(maze[pos[0]][pos[1]][1]==0):
        return [pos[0]+1,pos[1]]
    else:
        return [pos[0],pos[1]]