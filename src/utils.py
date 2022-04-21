from maps import *

def moveright(pos, maze, xsize):
    if((maze[pos[0]][pos[1] + 1][3] != 1) and pos[1] < xsize):
        pos[1] += 1
        return 1
    return 0

def moveleft(pos, maze):
    if((maze[pos[0]][pos[1] - 1][2] != 1) and pos[1] > 1):      
        pos[1] -= 1
        return 1
    return 0

def moveup(pos, maze):
    if((maze[pos[0] - 1][pos[1]][0] != 1) and pos[0] > 1):
        pos[0] -= 1
        return 1
    return 0

def movedown(pos, maze, ysize):
    if((maze[pos[0] + 1][pos[1]][1] != 1) and pos[0] < ysize):      
        pos[0] += 1
        return 1
    return 0

def get_xsize(maze):
    return len(maze[0])

def get_ysize(maze):
    return len(maze)

def printlogo(logo):
    for i in range(len(logo)):
        print(*logo[i])
