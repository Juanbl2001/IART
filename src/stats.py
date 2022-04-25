import numpy as np
import matplotlib.pyplot as plt
 
  
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