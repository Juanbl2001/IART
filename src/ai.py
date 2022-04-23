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
    count = 0

    while queue:
        count+=1
        heuristic = 999.0
        for i in range(len(queue)):
            aux = [start[0], start[1]] #so the initial Position doesn't get altered
            lastPos = move(queue[i], aux, goal, maze) #get last position achievable with that sequence
            auxHeuristic = eucDist(lastPos, goal) #calculate the heuristic from that last position achieved
            if(auxHeuristic <= heuristic):
                heuristic = auxHeuristic
                bestSeq = queue[i]
                bestPos = lastPos
            
        queue.remove(bestSeq)

        #checks depth
        if goal == bestPos:
            print(count)
            print("In greedy"+ str(bestSeq))
            return bestSeq

        if(len(bestSeq) < sizeOfAnswer):
            for movDir in ["L", "R", "U", "D"]:
                newSeq = list(bestSeq)
                newSeq.append(movDir)
                queue.append(newSeq)



def ucs(start, goal, maze, sizeOfAnswer):

    queue = []
    queue.append(["L",-1,[0,0]])
    queue.append(["R",-1,[0,0]])
    queue.append(["U",-1,[0,0]])
    queue.append(["D",-1,[0,0]])
    count = 0

    #by storing the value in the queue we dont need to re-search the last position of each value each time
    #time saved from 0.8s -> 0.004s
    while queue:
        count+=1
        bestHeuristic = 999.0
        for i in range(len(queue)):
            aux = [start[0], start[1]] #so the initial Position doesn't get altered
            if(queue[i][1]==-1):
                queue[i][2] = move(queue[i][0], aux, goal, maze) #get last position achievable with that sequence
                queue[i][1] = eucDist(queue[i][2], goal) #get heuristic
            if(queue[i][1] <= bestHeuristic):
                if(queue[i][1] == bestHeuristic and len(queue[i][0]) > len(bestVal[0]) and i != 0):
                    continue
                else:
                    bestVal = queue[i]
                    bestHeuristic = queue[i][1]

        queue.remove(bestVal)

        #checks depth
        if goal == bestVal[2]:
            print(count)
            print("In ucs"+ str(bestVal))
            return bestVal[0]

        if(len(bestVal[0]) < sizeOfAnswer):
            for movDir in "LDUR":
                newSeq = [bestVal[0]+movDir,-1,[0,0]]
                queue.append(newSeq)