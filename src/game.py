from ctypes.wintypes import RGB
import pygame
from time import sleep
from interface import *
from ai import *
from moves import *
from utils import *

def checkOption(pos):

    x = pos[0]
    y = pos[1]

    if x >= OPTIONS_X and x <= OPTIONS_X + OP_WIDTH:
        if y >= OPTION1_Y and y <= OPTION1_Y + OP_HEIGHT:
            return 1
        elif y >= OPTION2_Y and y <= OPTION2_Y + OP_HEIGHT:
            return 2
        elif y >= OPTION3_Y and y <= OPTION3_Y + OP_HEIGHT:
            return 3
        else:
            return 0


def chooseMaze(window, font):

    drawMazeOptions(window, font)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                op = mazeCheckOption(pos)

                if op >= 1 and op <= NUMBER_OF_MAZES:
                    mazeName = "p" + str(op)
                    return mazeName

            pygame.display.flip()


def mazeCheckOption(pos):

    posX = pos[0]
    posY = pos[1]
    x = MAZESOP_X
    y = MAZESOP_Y

    mazeNumber = 1
    for i in range(NUMBER_OF_MAZES):
        #updates x coordenate (2nd column)
        if i == int(NUMBER_OF_MAZES/2):
            x += MAZESOP_XDIST
            y = MAZESOP_Y

        if posX >= x and posX <= x+MAZEOP_WIDTH and posY >= y and posY <= y + MAZEOP_HEIGHT:
            print(mazeNumber)
            return mazeNumber
        y += MAZESOP_YDIST
        mazeNumber += 1

    return 0

def chooseSearch(window, font):

    drawSearchOptions(window, font)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                op = searchCheckOption(pos)

                if op == 1:
                    return "bfs"
                elif op == 2:
                    return "dfs"
                elif op == 3:
                    return "greedy"
                elif op == 4:
                    return "astar"

            pygame.display.flip()

def searchCheckOption(pos):

    x = pos[0]
    y = pos[1]

    if x >= OPTIONS_X and x <= OPTIONS_X + OP_WIDTH:
        if y >= SEARCH_OPTION1_Y and y <= SEARCH_OPTION1_Y + OP_HEIGHT:
            return 1
        if y >= SEARCH_OPTION2_Y and y <= SEARCH_OPTION2_Y + OP_HEIGHT:
            return 2
        if y >= SEARCH_OPTION3_Y and y <= SEARCH_OPTION3_Y + OP_HEIGHT:
            return 3
        if y >= SEARCH_OPTION4_Y and y <= SEARCH_OPTION4_Y + OP_HEIGHT:
            return 4

    return 0


def humanMode(window, font):

    mazeName = chooseMaze(window, font)
    if mazeName == 0:
        return
    maze = globals()[mazeName]
    initMaze(window, maze, goal)


def aiMode(window, font):

    mazeName = chooseMaze(window, font)
    if mazeName == 0:
        return
    maze = globals()[mazeName]
    method = chooseSearch(window, font)


    mazeSolSizeName = mazeName + "SolSize"
    mazeSolSize = globals()[mazeSolSizeName]

    seq = []

    if method == "bfs":
        seq = bfs(start, goal, maze)

    elif method == "dfs":
        seq = dfs(start, goal, maze, mazeSolSize)

    elif method == "greedy":
        seq = greedy(start, goal, maze, mazeSolSize)

    elif method == "astar":
        seq = aStar(start, goal, maze, mazeSolSize)

    else:
        return

    rectSizes = initMaze(window, maze, goal)
    pygame.display.flip()
    sleep(1)

    agentPos = start
    solving = True
    print("Sequence: ", seq)

    while solving == True:
        for i in seq:
            sleep(0.5)
            if agentPos == goal:
                solving = False
                break

            oldPos = agentPos
            if i == "R":
                agentPos = getRight(agentPos,maze)
            elif i == "L":
                agentPos = getLeft(agentPos, maze)
            elif i == "D":
                agentPos = getDown(agentPos, maze)
            elif i == "U":
                agentPos = getUp(agentPos, maze)

            if(oldPos != agentPos):
                drawAgent(window, oldPos[0], oldPos[1], rectSizes[0], rectSizes[1], WHITE) #remove agent
                """
                if(i == "U" or i == "D"):
                    #print(i,i)
                    drawPathV(window, oldPos[0], oldPos[1], rectSizes[0], rectSizes[1], BLACK)
                else:
                    #print(i)
                    drawPathH(window, oldPos[0], oldPos[1], rectSizes[0], rectSizes[1], BLACK)
                """
                drawAgent(window, agentPos[0], agentPos[1], rectSizes[0], rectSizes[1],BLUE)
                pygame.display.flip()


"""
def human_game(maze, pos, fin):

    # Calculate maze dimensions and exit position

    xsize = get_xsize(maze)
    ysize = get_ysize(maze)
    mazeName = chooseMaze(window, font)
    if mazeName == 0:
        return
    maze = globals()[mazeName]
    #method = chooseSearch(window, font)
    mazeSolSizeName = mazeName + "SolSize"
    mazeSolSize = globals()[mazeSolSizeName]

    seq = greedy(start, goal, maze, mazeSolSize)
    mov = input(
        'Choose movement direction: \n L => Left \n R => Right \n U => Up \n D => Down \n H => Hint \n Q => Quit \n ->')
    if mov.upper() == 'H':
        print('Hint\n')
        mov = input(
            'Choose movement direction: \n L => Left \n R => Right \n U => Up \n D => Down \n H => Hint \n Q => Quit \n ->')
    elif mov.upper() == 'Q':
        print('BETTER LUCK NEXT TRY!!!\n')
        return
    # Movement selector
    patternSize = len(mov)
    while pos[0] != fin[0] or pos[1] != fin[1]:
        for i in mov:
            while pos[0] != fin[0] or pos[1] != fin[1]:
                print(manDist(pos, fin))  # Print heuristic

                print(getCost())  # Print Cost
                addCost()  # Add Cost, initially +1 per move

                #printMaze(maze, pos, xsize, ysize)

                if i.upper() == 'L':
                    moveleft(pos, maze)

                elif i.upper() == 'R':
                    moveright(pos, maze)

                elif i.upper() == 'U':
                    moveup(pos, maze)

                elif i.upper() == 'D':
                    movedown(pos, maze)
                else:
                    print('INVALID OPTION!\n')

    # Win state
    #printMaze(maze, pos, xsize, ysize)
    print('YOU WON!!!\n')
    return
"""

def main():

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Python Maze Generator")
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont(FONT, 30)

    width = mazeSize*BLOCK
    height = mazeSize*BLOCK

    if width > 600:
        width = 600
    if height > 600:
        height = 600

    window = pygame.display.set_mode([width, height])

    drawMenu(window, font)

    running = True
    menu = True

    while running:
        clock.tick(FPS)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                op = checkOption(pos)
                if op == 1:
                    humanMode(window, font)
                elif op == 2:
                    aiMode(window, font)
                elif op == 3:
                    exit()

        # Flip the display
        pygame.display.flip()

    pygame.quit()

main()