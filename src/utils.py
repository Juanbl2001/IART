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

def check(pos,maze,side,xsize,ysize):
    if side=='L' and (maze[pos[0]][pos[1] - 1][2] != 1) and pos[1] > 1:
        return True
    elif side =='R' and (maze[pos[0]][pos[1] + 1][3] != 1) and pos[1] < xsize:
        return True
    elif side == 'U' and (maze[pos[0] - 1][pos[1]][0] != 1) and pos[0] > 1:
        return True
    elif side == 'D' and (maze[pos[0] + 1][pos[1]][1] != 1) and pos[0] < ysize:
        return True
    else:
        return False

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
