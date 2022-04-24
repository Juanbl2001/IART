# Using A*
# Cost -> Number of moves until it reaches the exit
# Heuristic -> Manhattan distance

from calendar import c
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

    h = sqrt((abs(robotPos[0] - finalPos[0])) ^ 2 +
             (abs(robotPos[0] - finalPos[0])) ^ 2 ^ 2)
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


def newDfs(start, goal, maze, sizeOfAnswer, seq=None, visited=None, limit=None):

    if seq is None:
        seq = []

    if visited is None:
        visited = []

    if limit is None:
        limit = 0

    if limit <= sizeOfAnswer:

        if seq != []:
            visited.append([seq])

        aux = [start[0], start[1]]

        if goal == move(seq, aux, goal, maze) and len(seq) == sizeOfAnswer:
            print(seq)
            return seq

        for movDir in ["L", "R", "U", "D"]:
            newSeq = list(seq)
            newSeq.append(movDir)
            if newSeq not in visited:
                newDfs(start, goal, maze, sizeOfAnswer,
                       newSeq, visited, (limit+1))


def newBfs(start, goal, maze):

    queue = []
    queue.append(["L"])
    queue.append(["R"])
    queue.append(["U"])
    queue.append(["D"])
    count = 0
    while queue:
        count += 1
        seq = queue.pop(0)
<<<<<<< HEAD
        #print("Value Error: "+ str("".join(seq)))
=======
>>>>>>> 29fc2d731a127f8917e2052ec9a764e60ede699d
        aux = [start[0], start[1]]

        if goal == move(seq, aux, goal, maze):
            print("\nCount in BFS: "+str(count))
            print("Value BFS: " + str("".join(seq)))
            return seq

        for movDir in ["L", "R", "U", "D"]:
            newSeq = list(seq)
            newSeq.append(movDir)
            queue.append(newSeq)


def greedy(start, goal, maze, sizeOfAnswer):

    queue = []
    queue.append(setUp("L", start, goal, maze))
    queue.append(setUp("R", start, goal, maze))
    queue.append(setUp("U", start, goal, maze))
    queue.append(setUp("D", start, goal, maze))
    count = 0

    # by storing the value in the queue we dont need to re-search the last position of each value each time
    # time saved from 0.8s -> 0.004s
    while queue:
        bestHeuristic = 999.0
        for i in range(len(queue)):
            if(queue[i][1] <= bestHeuristic):
                if(queue[i][1] == bestHeuristic):
                    continue
                else:
                    bestVal = queue[i]
                    bestHeuristic = queue[i][1]

        count += 1
        queue.remove(bestVal)

        # checks depth
        if goal == bestVal[2]:
            print("\nCount in Greedy: "+str(count))
            print("Value Greedy: " + str(bestVal[0]))
            return bestVal[0]

        if(len(bestVal[0]) < sizeOfAnswer):
            for movDir in "LDUR":
                newSeq = setUp(bestVal[0]+movDir, start, goal, maze)
                queue.append(newSeq)


def ucs(start, goal, maze, sizeOfAnswer):

    queue = []
    queue.append(setUp("L", start, goal, maze))
    queue.append(setUp("R", start, goal, maze))
    queue.append(setUp("U", start, goal, maze))
    queue.append(setUp("D", start, goal, maze))
    count = 0

    # by storing the value in the queue we dont need to re-search the last position of each value each time
    # time saved from 0.8s -> 0.004s
    while queue:
        bestHeuristic = 999.0
        for i in range(len(queue)):
            if(queue[i][1] <= bestHeuristic):
                if(queue[i][1] == bestHeuristic and len(queue[i][0]) > len(bestVal[0])):
                    continue
                else:
                    bestVal = queue[i]
                    bestHeuristic = queue[i][1]
        count += 1

        queue.remove(bestVal)

        # checks depth
        if goal == bestVal[2]:
            print("\nCount in UCS: "+str(count))
            print("Value UCS: " + str(bestVal[0]))
            return bestVal[0]

        if(len(bestVal[0]) < sizeOfAnswer):
            for movDir in "LDUR":
                newSeq = setUp(bestVal[0]+movDir, start, goal, maze)
                queue.append(newSeq)


def setUp(seq, start, goal, maze):
    aux = [start[0], start[1]]
    # get last position achievable with that sequence
    pos = move(seq, aux, goal, maze)
    return [seq, manDist(pos, goal), pos]
