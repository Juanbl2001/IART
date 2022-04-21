def listBitwiseOr(c1, c2):
    list = [i | j for i, j in zip(c1, c2)]
    return list


def listBitwiseAnd(c1, c2):
    list = [i & j for i, j in zip(c1, c2)]
    return list

# check for available positions around a certain position (returns list of available positions)


def check(pos, maze):
    possibleMoves = []
    if (maze[pos[0]][pos[1]][2] != 1):
        possibleMoves.append([pos[0], pos[1]-1])
    if (maze[pos[0]][pos[1]][3] != 1):
        possibleMoves.append([pos[0], pos[1]+1])
    if (maze[pos[0]][pos[1]][0] != 1):
        possibleMoves.append([pos[0]-1, pos[1]])
    if (maze[pos[0]][pos[1]][1] != 1):
        possibleMoves.append([pos[0]+1, pos[1]])
    return possibleMoves


def get_xsize(maze):
    return len(maze[0])


def get_ysize(maze):
    return len(maze)


def printlogo(logo):
    for i in range(len(logo)):
        print(*logo[i])
