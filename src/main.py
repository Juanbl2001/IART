<<<<<<< HEAD
from logos import *
from maps import *
from utils import *
from print import *
=======
#import imp
from typing import Counter
from logos import *
from maps import *
from utils import *
from ai import *

>>>>>>> 6d53f6dd3d55771ed0926e3ed559d7df88ddbb9e

def main():

    # print maintitle logo
    printlogo(maintitle)

    # mode selector
    mode_sel = 0

    while mode_sel != 5:
        mode_sel = input(
            'Choose mode: \n 1 => Human Mode \n 2 => AI mode \n 3 => Exit \n ->')

        if eval(mode_sel) == 1:
            human_mode()

        elif eval(mode_sel) == 2:
            human_mode()

        elif eval(mode_sel) == 3:
            print('GOODBYE!!!\n')
            return 0

        else:
            print('INVALID OPTION!\n')


def human_mode():

    # map selector
    maze_sel = 0

    while maze_sel != 5:
        maze_sel = input(
            'Choose map: \n 1 => test \n 2 => ??? \n 3 => ??? \n 4 => ??? \n 5 => Exit \n ->')

        if eval(maze_sel) == 1:
            human_game(test, testInit, testFin)

        elif eval(maze_sel) == 2:
            human_game(test, testInit, testFin)

        elif eval(maze_sel) == 3:
            human_game(test, testInit, testFin)

        elif eval(maze_sel) == 4:
            human_game(test, testInit, testFin)

        elif eval(maze_sel) == 5:
            print('GOODBYE!!!\n')
            return 0

        else:
            print('INVALID OPTION!\n')


def human_game(maze, pos, fin):

    # Calculate maze dimensions and exit position

    xsize = get_xsize(maze)
    ysize = get_ysize(maze)
<<<<<<< HEAD
    
    #Movement selector
    while pos[0] != fin[0] or pos[1] != fin[1]:
        printMaze(maze)
        mov = input('Choose movement direction: \n 1 => Left \n 2 => Right \n 3 => Up \n 4 => Down \n 5 => Hint \n 6 => Quit \n ->')
        
        if eval(mov) == 1:
            moveleft(pos, maze)
            
        elif eval(mov) == 2:
            moveright(pos, maze, xsize)
            
        elif eval(mov) == 3:
            moveup(pos, maze)
            
        elif eval(mov) == 4:
            movedown(pos, maze, ysize)

        elif eval(mov) == 5:
            print('Hint\n')
            
        elif eval(mov) == 6:
            print('BETTER LUCK NEXT TRY!!!\n')
            return 

        else:  
            print('INVALID OPTION!\n')
    
    # Win state
    # printMaze(maze)
    print('YOU WON!!!\n')
    return

=======
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

                printMaze(maze, pos, xsize, ysize)

                if i.upper() == 'L':
                    moveleft(pos, maze)

                elif i.upper() == 'R':
                    moveright(pos, maze, xsize)

                elif i.upper() == 'U':
                    moveup(pos, maze)

                elif i.upper() == 'D':
                    movedown(pos, maze, ysize)
                else:
                    print('INVALID OPTION!\n')

    # Win state
    printMaze(maze, pos, xsize, ysize)
    print('YOU WON!!!\n')
    return


>>>>>>> 6d53f6dd3d55771ed0926e3ed559d7df88ddbb9e
main()
