#for testing
from maps import *

def printMaze(maze):
    for i in range(len(maze)):
        line = maze[i]
        
        # initializeArrays(len(line))
        under = [0 for i in range(len(line))]
        above = [0 for i in range(len(line))]

        #ONE TAB = 5 SPACES
        for j in range(len(line)):
            
            elem = line[j]
            
            if elem == [0,0,0,0]:
                print("\t\t\t", end ="")

            elif elem == [0,0,0,1]:
                print("\t\t    |", end ="")

            elif elem == [0,0,1,0]:
                print("|    \t\t", end ="")

            elif elem == [0,0,1,1]:
                print("|    \t    |", end ="")

            elif elem == [0,1,0,0]:
                under[j] = 1

            elif elem == [0,1,0,1]:
                print("\t\t    |", end ="")
                under[j] = 1

            elif elem == [0,1,1,0]:
                print("|    \t\t", end ="")
                under[j] = 1

            elif elem == [0,1,1,1]:
                print("|    \t    |", end ="")
                under[j] = 1

            elif elem == [1,0,0,0]:
                print("\t\t\t", end ="")
                above[j] = 1

            elif elem == [1,0,0,1]:
                print("\t\t    |", end ="")
                above[j] = 1

            elif elem == [1,0,1,0]:
                print("|    \t\t", end ="")
                above[j] = 1

            elif elem == [1,0,1,1]:
                print("|    \t    |", end ="")
                above[j] = 1

            elif elem == [1,1,0,0]:
                print("\t\t\t", end ="")
                above[j] = 1
                under[j] = 1

            elif elem == [1,1,0,1]:
                print("\t\t    |", end ="")
                above[j] = 1
                under[j] = 1

            elif elem == [1,1,1,0]:
                print("|    \t\t", end ="")
                above[j] = 1
                under[j] = 1

            elif elem == [1,1,1,1]:
                print("|    \t    |", end ="")
                above[j] = 1
                under[j] = 1
        
        for k in above:
            if k == 1:
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

        for k in under:
            if k == 1:
                print("_______________")
        #just new line    
        print("\n\n")

printMaze(test)