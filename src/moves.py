def moveright(pos, maze):
    if((maze[pos[0]][pos[1]][3] != 1)):
        pos[1] += 1
        return 1
    return 0


def moveleft(pos, maze):
    if((maze[pos[0]][pos[1]][2] != 1)):
        pos[1] -= 1
        return 1
    return 0


def moveup(pos, maze):
    if((maze[pos[0]][pos[1]][0] != 1)):
        pos[0] -= 1
        return 1
    return 0


def movedown(pos, maze):
    if((maze[pos[0]][pos[1]][1] != 1)):
        pos[0] += 1
        return 1
    return 0