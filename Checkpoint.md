# Checkpoint

## Game 
This is a single player game where the goal is to find the (shortest) path to a labyrinth's exit.

## Solution

There is always going to be a solution for every labyrinth. This solution is going to be the sequence of moves for the shortest path to the exit. This sequence needs to be repeated until the robot reaches the goal.

## References

## Problem formulation 

### State Representation
- (x,y) - Represents the user current position
- place(x,y) - Represents what is in (x,y)
- if place(x,y) == 0 then (x,y) is free
- if place(x,y) == 1 then a wall occupies (x,y)
- if place(x,y) == 2 then (x,y) is the exit
- We are representing the labyrinth's dimensions as xSize and ySize.
- Consider the xy axis has its origin in the superior left corner, like this:

    ![Axis Representation](img/xyaxis.png)

### Initial state

Can be any (x,y), usually in one of the corners of the labyrinth.
We are considering it's (0,0), for example.

### Objective test

Any (x,y) and place(x,y) = 2.

### Operators (Name, Preconditions, Effect, Cost)

| Name  | Preconditions             | Effect    | Cost |
| ----- | ------------------------- | --------- | ---- |
| UP    | y>0 & place(x,y)!=1       | y = y-1   |  1   | 
| DOWN  | y<ySize & place(x,y)!=1   | y = y+1   |  1   |
| LEFT  | x>0 & place(x,y)!=1       | x = x-1   |  1   |
| RIGHT | x<xSize & place(x,y)!=1   | x = x+1   |  1   |

## Programming language

We are using **Python** for this project.
*explain why*

## Data structures to be used
