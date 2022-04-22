# Using A*
# Cost -> Number of moves until it reaches the exit
# Heuristic -> Manhattan distance

from importlib.resources import path
from queue import *
from utils import *

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


def greedy(start, goal, maze):

    path = []
    explored = []
    neighbour = start

    path.append(start)
    explored.append(start)

    while neighbour != goal:

        neighbours = check(neighbour, maze)
        h = 9999

        for n in neighbours:

            hAux = manDist(n, goal)

            if hAux < h and (n not in explored):
                h = hAux
                neighbour = n
                explored.append(n)

        if neighbour not in path:
            path.append(neighbour)

        else:
            print("Couldn't find goal :(")
            return 0

    return path
