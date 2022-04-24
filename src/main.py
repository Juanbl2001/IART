#import imp

from tracemalloc import start
from logos import *
from maps import *
from utils import *
from typing import Counter
from ai import *
from moves import *
from time import *


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


# UCS
"""
start_ucs = time()
ucs(p18Start, p18Goal,p18,7)
end_ucs=time()
print("Time in UCS: " + str(end_ucs-start_ucs))

#Greedy
start_greedy = time()
greedy(p18Start, p18Goal,p18,7)
end_greedy = time()
print("Time in Greedy: " + str(end_greedy-start_greedy))
#BFS
start_bfs = time()
newBfs(p18Start, p18Goal,p18)
end_bfs = time()
print("Time in BFS: " + str(end_bfs-start_bfs))
"""
