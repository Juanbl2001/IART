import pygame
from utils import *
from maps import *

def drawRect(window, posX, posY, rectWidth, rectHeight):

    rectColor = (18, 91, 13)

    pygame.draw.rect(window, rectColor, (posX, posY, rectWidth, rectHeight))

def drawWall(window, posX, posY, rectWidth, rectHeight, side):

    wallColor = (0,0,0)

    ratio = 0.05
    if side == "l" or side == "r":
        wallWidth = ratio * rectWidth
        wallHeight = rectHeight
    else:
        wallWidth = rectHeight
        wallHeight = ratio * rectWidth

    if side == "d" or side == "r":
        posX += (rectWidth - wallWidth)
        posY += (rectHeight - wallHeight)

    print("Wall Width = ", wallWidth)
    print("Wall Height = ",wallHeight)
    pygame.draw.rect(window, wallColor, (posX, posY, wallWidth, wallHeight))


def drawAgent(window, x, y):

    agentColor = (226,208,48)
    if window.get_width() < window.get_height():
        aux = window.get_width()
    else:
        aux = window.get_height()

    radius = 0.05 * aux
    pygame.draw.circle(window,agentColor,(x,y),radius)

def drawExit(maze, window, exit, rectWidth, rectHeight):

    exitColor = (222,1,1)
    ratio = 0.05

    # check which side is the exit
    if exit[2] == "l" or exit[2] == "r":
        width = ratio * rectWidth
        height = rectHeight
    else:
        width = rectWidth
        height = ratio * rectHeight

    if exit[2] == "d" or exit[2] == "r":
        x = rectWidth * (exit[0]+1) - width
        y = rectHeight * (exit[1]+1) - height

    else:
        x = rectWidth * exit[0]
        y = rectHeight * exit[1]

    pygame.draw.rect(window,exitColor,(x,y,width,height))

def drawMaze(maze, window, rectWidth, rectHeight, goal):

    window.fill((255,255,255))

    posY = 0

    y = 0
    count = 0
    for line in maze:
        posX = 0

        for elem in line:

            #draws rectangle no matter how many walls its drawing after
            drawRect(window,posX,posY,rectWidth,rectHeight)

            # [u, d, l, r]
            right = listBitwiseAnd(elem, r_wall)
            left = listBitwiseAnd(elem, l_wall)
            up = listBitwiseAnd(elem, u_wall)
            down = listBitwiseAnd(elem, d_wall)

            if right == r_wall:
                drawWall(window, posX, posY, rectWidth, rectHeight, "r")

            if left == l_wall:
                drawWall(window, posX, posY, rectWidth, rectHeight, "l")

            if up == u_wall:
                drawWall(window, posX, posY, rectWidth, rectHeight, "u")

            if down == d_wall:
                drawWall(window, posX, posY, rectWidth, rectHeight, "d")

            posX += rectWidth
            count += 1


        posY += rectHeight
    drawExit(maze, window, goal, rectWidth, rectHeight)


def initMaze(maze,goal):

    pygame.init()

    width = len(maze[0]*100)
    height = len(maze*100)

    window = pygame.display.set_mode([width, height])

    rectWidth = window.get_width() / len(maze)
    rectHeight = window.get_height() / len(maze[0])

    drawMaze(maze,window,rectWidth,rectHeight,goal)
    drawAgent(window,rectWidth/2,rectHeight/2)

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Flip the display
        pygame.display.flip()

    pygame.quit()


#TESTING
initMaze(test3, testGoal3)