from logos import *
from maps import *
from utils import *

def main():
    
    # print maintitle logo
    printlogo(maintitle)

    # mode selector
    mode_sel = 0
    
    while mode_sel != 5:
        mode_sel = input('Choose mode: \n 1 => Human Mode \n 2 => AI mode \n 3 => Exit \n ->')
        
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
        maze_sel = input('Choose map: \n 1 => test \n 2 => ??? \n 3 => ??? \n 4 => ??? \n 5 => Exit \n ->')
        
        if eval(maze_sel) == 1:
            human_game(test, [1,1])
            
        elif eval(maze_sel) == 2:
            human_game(test, [1,1])
            
        elif eval(maze_sel) == 3:
            human_game(test, [1,1])
            
        elif eval(maze_sel) == 4:
            human_game(test, [1,1])
            
        elif eval(maze_sel) == 5:
            print('GOODBYE!!!\n')
            return 0
        
        else:  
            print('INVALID OPTION!\n')
        
    
def human_game(maze, pos):

    #Calculate maze dimensions and exit position
    xsize = get_xsize(maze)
    ysize = get_ysize(maze)
    exit_pos = get_exit_pos(maze, ysize, xsize)
    
    #Movement selector
    while pos[0] != exit_pos[0] or pos[1] != exit_pos[1]:
        printMaze(maze, pos, xsize, ysize)
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
    printMaze(maze, pos, xsize, ysize)
    print('YOU WON!!!\n')
    return

main()