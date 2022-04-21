import pygame
from maps import *

def drawMaze(maze, window):

    window.fill((255,255,255))

    rectWidth = window.get_width()/len(maze)
    rectHeight = window.get_height()/len(maze[0])
    rectColor = (164,112,44)

    wallColor = (0,0,0)
    posX = 0
    posY = 0

    for line in maze:
        for elem in line:
            if elem == [0,0,0,0]:
                pygame.draw.rect(window, rectColor, (posX, posY,rectWidth,rectHeight))
            #elif elem == [0,0,0,1]:

            #elif elem ==

            posX += rectWidth


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