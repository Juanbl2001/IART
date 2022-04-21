#Map building macros
# u -> up
# d -> down
# l -> left
# r -> right
# [u, d, l, r]

def listBitwiseOr(c1, c2):

        list = [ i|j for i, j in zip(c1, c2)]
        return list

no_wall = (0,0,0,0)

r_wall = (0,0,0,1)

l_wall = (0,0,1,0)

d_wall = (0,1,0,0)

u_wall = (1,0,0,0)

lr_wall = listBitwiseOr(l_wall,r_wall)

dr_wall = listBitwiseOr(d_wall,r_wall)

dl_wall = listBitwiseOr(d_wall,l_wall)

dlr_wall = listBitwiseOr(listBitwiseOr(d_wall,r_wall),r_wall)

ur_wall = listBitwiseOr(u_wall,r_wall)

ul_wall = listBitwiseOr(u_wall,l_wall)

ulr_wall = listBitwiseOr(listBitwiseOr(u_wall,l_wall),r_wall)

ud_wall = listBitwiseOr(u_wall,d_wall)

udr_wall = listBitwiseOr(listBitwiseOr(u_wall,d_wall),r_wall)

udl_wall = listBitwiseOr(listBitwiseOr(u_wall,d_wall),l_wall)

udlr_wall = listBitwiseOr(listBitwiseOr(u_wall,d_wall),listBitwiseOr(l_wall,r_wall))

#test map

testInit = [0,0]

testFin = [6,5]

test = [[ul_wall, u_wall, u_wall, u_wall, ur_wall],
        [l_wall, no_wall, dr_wall, l_wall, r_wall],
        [l_wall, r_wall, ul_wall, no_wall, r_wall],
        [l_wall, no_wall, dr_wall, l_wall, r_wall],
        [l_wall, r_wall, ul_wall, no_wall, r_wall],
        [dl_wall, d_wall, d_wall, d_wall, dr_wall]]


test2 = [[ul_wall, u_wall, u_wall, u_wall, ur_wall],
        [l_wall, no_wall, dr_wall, l_wall, r_wall],
        [l_wall, r_wall, ul_wall, no_wall, r_wall],
        [l_wall, no_wall, dr_wall, l_wall, r_wall],
        [l_wall, r_wall, ul_wall, no_wall, r_wall]]

print(ur_wall)