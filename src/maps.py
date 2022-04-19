#Map building macros
# u -> up
# d -> down
# l -> left
# r -> right
# [u, d, l, r]

no_wall = [0,0,0,0]

r_wall = [0,0,0,1]

l_wall = [0,0,1,0]

lr_wall = [0,0,1,1]

d_wall = [0,1,0,0]

dr_wall = [0,1,0,1]

dl_wall = [0,1,1,0]

dlr_wall = [0,1,1,1]

u_wall = [1,0,0,0]

ur_wall = [1,0,0,1]

ul_wall = [1,0,1,0]

ulr_wall = [1,0,1,1]

ud_wall = [1,1,0,0]

udr_wall = [1,1,0,1]

udl_wall = [1,1,1,0]

udlr_wall = [1,1,1,1]


#test map
<<<<<<< HEAD
#0 = no walls
#1 = wall up
#2 = wall down
#3 = wall right
#4 = wall left
test = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,2,1],
        [1,1,1,1,1]]

newTest = [[[1,4],[1,2],[1,3]],
           [[4],[1,3],[3,4]],
           [[4],[2,3],[3,4]],
           [[4,2],[1,2,3],[2,3,4]]]
=======

testInit = [0,0]

testFin = [6,5]

test = [[ul_wall, u_wall, u_wall, u_wall, ur_wall],
        [l_wall, no_wall, dr_wall, l_wall, r_wall],
        [l_wall, r_wall, ul_wall, no_wall, r_wall],
        [l_wall, no_wall, dr_wall, l_wall, r_wall],
        [l_wall, r_wall, ul_wall, no_wall, r_wall],
        [dl_wall, d_wall, d_wall, d_wall, dr_wall]]
>>>>>>> d8a501f7a523f07144ebc6b9988c2039c20105d7
