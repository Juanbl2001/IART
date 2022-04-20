# Using A*
# Cost -> Number of moves until it reaches the exit
# Heuristic -> Manhattan distance

from utils import *
from main import *


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


def dfs(neighbours, position, destination, visited=None, path=None):

    if visited is None:
        visited = []
    if path is None:
        path = []

    visited.add(position)
    path.append(position)

    if position[0] != destination[0] or position[1] != destination[1]:

        neighbours = check()

        for neighbour in neighbours[position]:
            if neighbour not in visited:
                dfs(neighbours, neighbour, visited, path)

    return path


def bfs_shortest_path(start, goal):
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
            neighbours = check()
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
