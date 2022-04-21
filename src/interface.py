import pygame
from maps import *

def drawRect(window, posX, posY, rectWidth, rectHeight):

    rectColor = (164, 112, 44)

    pygame.draw.rect(window, rectColor, (posX, posY, rectWidth, rectHeight))

def drawWall(window, posX, posY, rectWidth, rectHeight, side):

    wallColor = (0,0,0)

    if side == "l" or side == "r":
        wallWidth = 0.9 * rectWidth
        wallHeight = rectHeight
    else:
        wallWidth = rectHeight
        wallHeight = 0.9 * rectWidth

    if side == "d" or side == "r":
        posX += (rectWidth - wallWidth)
        posY += (rectHeight - wallHeight)


    pygame.draw.rect(window, wallColor, (posX, posY, wallWidth, wallHeight))


def drawMaze(maze, window):

    window.fill((255,255,255))

    posX = 0
    posY = 0

    rectWidth = window.get_width() / len(maze)
    rectHeight = window.get_height() / len(maze[0])

    for line in maze:
        for elem in line:

            #draws rectangle no matter how many walls its drawing after
            drawRect(window,posX,posY,rectWidth,rectHeight)

            # [u, d, l, r]
            right = elem & r_wall
            left = elem & l_wall
            up = elem & u_wall
            down = elem & d_wall

            if right == r_wall:
                drawWall(window, posX, posY, rectWidth, rectHeight, "r")

            if left == l_wall:
                drawWall(window, posX, posY, rectWidth, rectHeight, "l")

            if up == u_wall:
                drawWall(window, posX, posY, rectWidth, rectHeight, "u")

            if down == d_wall:
                drawWall(window, posX, posY, rectWidth, rectHeight, "d")



def initMaze(maze):

    pygame.init()

    width = 600
    height = 600

    window = pygame.display.set_mode([width, height])

    drawMaze(maze,window)

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw a solid blue circle in the center
        #pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()

    pygame.quit()


#TESTING
initMaze(test)