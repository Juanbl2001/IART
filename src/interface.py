import pygame
from utils import *
from maps import *

# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 51, 0)
BLUE = (0, 51, 204)
YELLOW = (255 ,255 ,0)
RED = (204, 0, 0)
BLACK = (0,0,0)

# FONTS
FONT = 'calibri'

#OPTIONS POSITION
Y_DIST = 75
OPTIONS_X = 150
OPTION1_Y = 200
OPTION2_Y = OPTION1_Y + Y_DIST
OPTION3_Y = OPTION2_Y + Y_DIST
OP_WIDTH = 200
OP_HEIGHT = 30

# set up pygame window
BLOCK = 100
FPS = 60
mazeSize = 5


def drawRect(window, posX, posY, rectWidth, rectHeight):

    pygame.draw.rect(window, WHITE, (posX, posY, rectWidth, rectHeight))

def drawWall(window, posX, posY, rectWidth, rectHeight, side):

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

    pygame.draw.rect(window, BLACK, (posX, posY, wallWidth, wallHeight))


def drawAgent(window, x, y, rectWidth, rectHeight):

    if window.get_width() < window.get_height():
        aux = window.get_width()
    else:
        aux = window.get_height()

    radius = 0.06 * aux
    pygame.draw.circle(window,BLUE,(x*BLOCK+rectWidth/2,y*BLOCK+rectHeight/2),radius)

def drawExit(window, exit, rectWidth, rectHeight):

    '''
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
    '''

    pygame.draw.rect(window,RED,(exit[0]*rectWidth,exit[1]*rectHeight,rectWidth,rectHeight))

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
    drawExit(window, goal, rectWidth, rectHeight)

def drawText(window, font, text, x, y):
    textRenderer = font.render(text, False, WHITE)
    window.blit(textRenderer, (x, y))

def drawMenu(window, font):

    #Choose option
    text = "Choose Option"
    x = 160
    y = 60
    drawText(window, font, text, x, y)

    #OP1 - Human mode
    text = "1. Human Mode"
    drawText(window, font, text, OPTIONS_X, OPTION1_Y)

    #OP2 - AI mode
    text = "2. AI Mode"
    drawText(window, font, text, OPTIONS_X, OPTION2_Y)

    # OP3 - EXIT
    text = "3. Exit"
    drawText(window, font, text, OPTIONS_X, OPTION3_Y)


def drawHumanOptions(window,font):

    window.fill(BLACK)

    #Choose Option
    text = "Human Mode"
    x = 165
    y = 40
    drawText(window, font, text, x, y)

    xDist = 200
    yDist = 35

    x = 100

    mazeNumber = 1
    #20 is the number of mazes
    for i in range(20):
        y = 100
        for i in range(10):
            text = "Maze " + str(mazeNumber)
            drawText(window, font, text, x, y)
            mazeNumber += 1
            y += yDist
        x += xDist



def initMaze(window,maze,goal):

    rectWidth = window.get_width() / len(maze)
    rectHeight = window.get_height() / len(maze[0])

    drawMaze(maze,window,rectWidth,rectHeight,goal)
    drawAgent(window,start[0],start[1],rectWidth,rectHeight)

#TESTING