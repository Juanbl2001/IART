# Using A*
# Cost -> Number of moves until it reaches the exit
# Heuristic -> Manhattan distance

from importlib.resources import path
from queue import Empty
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


def dfs(neighbours, position, destination, maze, visited=None, path=None):

    if visited is None:
        visited = []
    if path is None:
        path = []

    visited.add(position)
    path.append(position)

    if position[0] != destination[0] or position[1] != destination[1]:

        neighbours = check(position, maze)

        for neighbour in neighbours[position]:
            if neighbour not in visited:
                dfs(neighbours, neighbour, visited, path)

    return path


def bfs(start, goal, maze):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [start]

    # return path if start is goal
    if start == goal:
        return [goal]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = check(node, maze)
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    print("No path to destiny exists")
    return 0


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

    path.append(neighbour)
    return path
