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

testInit = [0,0]

testFin = [6,5]

test = [[ul_wall, u_wall, u_wall, u_wall, ur_wall],
        [l_wall, no_wall, dr_wall, l_wall, r_wall],
        [l_wall, r_wall, ul_wall, no_wall, r_wall],
        [l_wall, no_wall, dr_wall, l_wall, r_wall],
        [l_wall, r_wall, ul_wall, no_wall, r_wall],
        [dl_wall, d_wall, d_wall, d_wall, dr_wall]]