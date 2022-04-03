pos = [1,1] #initial robot position
xsize = 5 #size of board horizontally
ysize = 6 #size of board vertically

def moveright(pos,maze):
    if(maze[pos[0]+1][pos[1]] == 0 and pos[0] < xsize):
        pos[0]+=1
        return 1
    return 0

def moveleft(pos,maze):
    if(maze[pos[0]-1][pos[1]] == 0 and pos[0] > 1):
        pos[0]-=1
        return 1
    return 0

def moveup(pos,maze):
    if(maze[pos[0]][pos[1]+1] == 0 and pos[1] < ysize):
        pos[1]+=1
        return 1
    return 0

def movedown(pos,maze):
    if(maze[pos[0]][pos[1]-1] == 0 and pos[1] > 1):
        pos[1]-=1
        return 1
    return 0
    