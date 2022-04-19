<<<<<<< HEAD
#0 = no walls
#1 = wall up
#2 = wall down
#3 = wall right
#4 = wall left

def moveright(pos, maze, xsize):
    if((maze[pos[0]][pos[1]]).count(3) == 0 and pos[1] < xsize):
=======
from maps import *

def moveright(pos, maze, xsize):
    if((maze[pos[0]][pos[1] + 1][3] != 1) and pos[1] < xsize):
>>>>>>> d8a501f7a523f07144ebc6b9988c2039c20105d7
        pos[1] += 1
        return 1
    return 0

def moveleft(pos, maze):
<<<<<<< HEAD
    if((maze[pos[0]][pos[1]]).count(4) == 0 and pos[1] > 0):      
=======
    if((maze[pos[0]][pos[1] - 1][2] != 1) and pos[1] > 1):      
>>>>>>> d8a501f7a523f07144ebc6b9988c2039c20105d7
        pos[1] -= 1
        return 1
    return 0

def moveup(pos, maze):
<<<<<<< HEAD
    if((maze[pos[0]][pos[1]]).count(1) == 0 and pos[0] > 0):
=======
    if((maze[pos[0] - 1][pos[1]][0] != 1) and pos[0] > 1):
>>>>>>> d8a501f7a523f07144ebc6b9988c2039c20105d7
        pos[0] -= 1
        return 1
    return 0

def movedown(pos, maze, ysize):
<<<<<<< HEAD
    if((maze[pos[0]][pos[1]]).count(2) == 0 and pos[0] < ysize):      
=======
    if((maze[pos[0] + 1][pos[1]][1] != 1) and pos[0] < ysize):      
>>>>>>> d8a501f7a523f07144ebc6b9988c2039c20105d7
        pos[0] += 1
        return 1
    return 0

def printMaze(maze, pos, xsize, ysize):
    
    # converte a matriz estado numa matriz para "display friendly"
    aux = [[0 for x in range(xsize)] for y in range(ysize)] 
    for i in range(ysize):
        for j in range(xsize):
            if maze[i][j] == 0:
                aux[i][j] = '.'
            elif maze[i][j] == 1:
                aux[i][j] = 'X'
            elif maze[i][j] == 2:
                aux[i][j] = 'E'
                
    # adiciona o jogador a matriz de display
    aux[pos[0]][pos[1]] = 'P'
    
    for i in range(ysize):
        print(*aux[i])
    return

def get_xsize(maze):
    return len(maze[0])

def get_ysize(maze):
    return len(maze)

def printlogo(logo):
    for i in range(len(logo)):
        print(*logo[i])
