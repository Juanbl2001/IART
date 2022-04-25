import pygame
from interface import *
from ai import *
from moves import *

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


def human_game(maze, pos, fin):

    # Calculate maze dimensions and exit position

    xsize = get_xsize(maze)
    ysize = get_ysize(maze)
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


def humanMode(window, font):

    print("humanmode")
    drawHumanOptions(window,font)
    '''
    initMaze(window, p1, goal)
    # map selector
    maze_sel = 0

    while maze_sel != 5:
        maze_sel = input(
            'Choose map: \n 1 => test \n 2 => ??? \n 3 => ??? \n 4 => ??? \n 5 => Exit \n ->')

        if eval(maze_sel) == 1:
            human_game(test, testInit, testGoal)

        elif eval(maze_sel) == 2:
            human_game(test, testInit, testGoal)

        elif eval(maze_sel) == 3:
            human_game(test, testInit, testGoal)

        elif eval(maze_sel) == 4:
            human_game(test, testInit, testGoal)

        elif eval(maze_sel) == 5:
            print('GOODBYE!!!\n')
            return 0

        else:
            print('INVALID OPTION!\n')
    
    '''

def aiMode(window):
    print("aimode")

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
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if menu == True:
                    menu = False
                    op = checkOption(pos)
                    if op == 1:
                        humanMode(window,font)
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