# IART 2021/2022: Robot Maze

## Team members
- Juan Bellon [201908142]
- Luísa Araújo [201904996]
- Nuno Castro [202003324]

## To do
### Topic 1: Heuristic Search Methods for One Player Solitaire Games
A solitaire game is characterized by the *type of board and pieces*, the *rules of movement of the pieces*
(possible operators/plays), and the *conditions for ending the game with defeat* (impossibility to solve,
maximum number of moves reached, time limit reached) or *victory* (solitaire solved), together with the
*respective score*. Typically, in the event of a win, a score is awarded depending on the **number of moves**,
**resources spent**, **bonuses collected** and/or **time spent**.
In addition to implementing a solitaire game for a human player, the program must be able to solve different
versions/levels of this game, using appropriate search methods, focusing on the comparison between
uninformed search methods (breadth-first search, depth-first search, iterative deepening, uniform cost) and
heuristic search methods (greedy search, A* Algorithm), with different heuristic functions. The algorithms
employed should be compared with several criteria, with emphasis on the quality of the solution obtained,
number of operations performed, maximum memory used, and time spent to obtain the solution.
The application should have a text or graphical use interface to show the evolution of the board and interact
with the user/player. You should allow a game mode in which the PC solves the solitaire alone using the
algorithm and respective configuration as selected by the user. Optionally, you can allow a Human game
mode in which the user can solve the game, while asking the PC for “hints”.

### Checkpoint
Each group must submit in Moodle a brief presentation (max. 5 slides), in PDF format, which will be used
in the class to analyze, together with the teacher, the progress of the work. The presentation should contain:<br>
(1) specification of the work to be performed (definition of the game or optimization problem to be solved)<br>
(2) related work with references to works found in a bibliographic search (articles, web pages and/or source
code)<br> (3) formulation of the problem as a search problem (state representation, initial state, objective test,
operators (names, preconditions, effects and costs), heuristics/evaluation function) or optimization problem
(solution representation, neighborhood/mutation and crossover functions, hard constraints, evaluation
functions)<br>(4) implementation work already carried out (programming language, development
environment, data structures, among others).


## SETUP

<code>
sudo apt-get install python3-tk
pip install matplotlib
pip install pyamaze
</code>