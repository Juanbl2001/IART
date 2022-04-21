import pygame
from utils import *
from maps import *

def drawRect(window, posX, posY, rectWidth, rectHeight):

    rectColor = (164, 112, 44)

    pygame.draw.rect(window, rectColor, (posX, posY, rectWidth, rectHeight))

def drawWall(window, posX, posY, rectWidth, rectHeight, side):

    wallColor = (0,0,0)

    if side == "l" or side == "r":
        wallWidth = 0.1 * rectWidth
        wallHeight = rectHeight
    else:
        wallWidth = rectHeight
        wallHeight = 0.1 * rectWidth

    if side == "d" or side == "r":
        posX += (rectWidth - wallWidth)
        posY += (rectHeight - wallHeight)

    print("Wall Width = ", wallWidth)
    print("Wall Height = ",wallHeight)
    pygame.draw.rect(window, wallColor, (posX, posY, wallWidth, wallHeight))


def drawMaze(maze, window):

    window.fill((255,255,255))

    posY = 0

    rectWidth = window.get_width() / len(maze)
    rectHeight = window.get_height() / len(maze[0])

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

def initMaze(maze):

    pygame.init()

    width = len(maze[0]*100)
    height = len(maze*100)

    window = pygame.display.set_mode([width, height])

    drawMaze(maze,window)

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
initMaze(test3)