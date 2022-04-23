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

    while queue:

        seq = queue.pop(0)
        aux = [start[0], start[1]]

        if goal == move(seq, aux, goal, maze):
            return seq

        for movDir in ["L", "R", "U", "D"]:
            newSeq = list(seq)
            newSeq.append(movDir)
            queue.append(newSeq)


def greedy(start, goal, maze):

    path = []
    explored = []
    pos = start

    path.append(start)
    explored.append(start)

    while pos != goal:

        neighbours = check(pos, maze)
        h = 9999

        for n in neighbours:

            hAux = manDist(n, goal)

            if hAux < h and (n not in explored):
                h = hAux
                pos = n
                explored.append(n)

        if pos not in path:
            path.append(pos)

        else:
            print("Couldn't find goal :(")
            return 0

    return path
