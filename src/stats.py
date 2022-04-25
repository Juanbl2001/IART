#import imp

from tracemalloc import start
from maps import *
from utils import *
from typing import Counter
from ai import *
from moves import *
from time import *
from stats import *
import numpy as np
import matplotlib.pyplot as plt
import itertools

def stats(pt,s):
    p = globals()[pt]

    start_dfs = time()
    dfs(start, goal, p, s)
    end_dfs = time()
    time_dfs = float(end_dfs-start_dfs)

    # Greedy
    start_greedy = time()
    ans=greedy(start, goal,p,s)
    end_greedy = time()
    time_greedy = float(end_greedy-start_greedy)
    print(ans)

    # BFS
    start_bfs = time()
    bfs(start, goal, p)
    end_bfs = time()
    time_bfs = float(end_bfs-start_bfs)

    # A*
    start_astar = time()
    aStar(start, goal, p, s)
    end_astar = time()
    time_astar = float(end_astar-start_astar)

    TimeEfficiency(time_dfs, time_bfs, time_greedy, time_astar, s)
    SpaceEfficiency(getCostDfs(),getCostBfs(),getCostGreedy(),getCostAstar(),s)
    return

# creating the dataset
def TimeEfficiency(time_dfs,time_bfs,time_greedy,time_astar,stepsRequired):
    data = {'DFS':time_dfs, 'BFS':time_bfs, 'Greedy':time_greedy,
            'A*':time_astar}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (8, 4))
    
    # creating the bar plot
    plt.bar(courses, values, color ='green',
            width = 0.5)
    
    plt.xlabel("Algorithm")
    plt.ylabel("Time to find solution")
    plt.title("Time efficiency of Algorithms with "+str(stepsRequired)+" steps")
    plt.show()
    return

def SpaceEfficiency(space_dfs,space_bfs,space_greedy,space_astar,stepsRequired):
    data = {'DFS':space_dfs, 'BFS':space_bfs, 'Greedy':space_greedy,
            'A*':space_astar}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (8, 4))
    
    # creating the bar plot
    plt.bar(courses, values, color ='green',
            width = 0.5)
    
    plt.xlabel("Algorithm")
    plt.ylabel("Iterations to find solution")
    plt.title("Space efficiency of Algorithms with "+str(stepsRequired)+" steps")
    plt.show()
    return

def main():
        mapOption = str(input("Enter Map Number: "))
        mapOption = "p"+mapOption
        s = int(input("Enter Answer Size: "))
        stats(mapOption,s)
        exit()
main()