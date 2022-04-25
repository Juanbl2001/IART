import pygame
from interface import *

# set up pygame window
BLOCK = 100
FPS = 60
mazeSize = 5

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

def humanMode(window):
    print("humanmode")
    initMaze(window, p1, goal, BLOCK)

def aiMode(window):
    print("aimode")

def main():

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Python Maze Generator")
    clock = pygame.time.Clock()

    width = mazeSize*BLOCK
    height = mazeSize*BLOCK

    if width > 600:
        width = 600
    if height > 600:
        height = 600

    window = pygame.display.set_mode([width, height])
    drawMenu(window, 1)

    running = True
    menu = True

    while running:
        clock.tick(FPS)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if menu == True:
                    menu = False
                    op = checkOption(pos)
                    if op == 1:
                        humanMode(window)
                    elif op == 2:
                        aiMode(window)
                    elif op == 3:
                        running = False
                    else:
                        menu = True

        # Flip the display
        pygame.display.flip()

    pygame.quit()

main()