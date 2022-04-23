from utils import *

# Map building macros
# u -> up
# d -> down
# l -> left
# r -> right
# [u, d, l, r]

no_wall = [0, 0, 0, 0]

r_wall = [0, 0, 0, 1]

l_wall = [0, 0, 1, 0]

d_wall = [0, 1, 0, 0]

u_wall = [1, 0, 0, 0]

lr_wall = listBitwiseOr(l_wall, r_wall)

dr_wall = listBitwiseOr(d_wall, r_wall)

dl_wall = listBitwiseOr(d_wall, l_wall)

dlr_wall = listBitwiseOr(listBitwiseOr(d_wall, r_wall), r_wall)

ur_wall = listBitwiseOr(u_wall, r_wall)

ul_wall = listBitwiseOr(u_wall, l_wall)

ulr_wall = listBitwiseOr(listBitwiseOr(u_wall, l_wall), r_wall)

ud_wall = listBitwiseOr(u_wall, d_wall)

udr_wall = listBitwiseOr(listBitwiseOr(u_wall, d_wall), r_wall)

udl_wall = listBitwiseOr(listBitwiseOr(u_wall, d_wall), l_wall)

udlr_wall = listBitwiseOr(listBitwiseOr(
    u_wall, d_wall), listBitwiseOr(l_wall, r_wall))

# test map

testInit = [0, 0]

testGoal = [4, 5]

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
         [dl_wall, d_wall, d_wall, d_wall, dr_wall]]

testGoal2 = [4, 4]

test3 = [[ul_wall, u_wall, u_wall, u_wall, ur_wall],
         [l_wall, no_wall, no_wall, no_wall, r_wall],
         [dl_wall, no_wall, no_wall, no_wall, r_wall],
         [dl_wall, no_wall, no_wall, no_wall, r_wall],
         [dl_wall, d_wall, d_wall, d_wall, dr_wall]]

# (X, Y, DIRECTION ->
testGoal3 = [3, 0, "u"]
# print(ur_wall)


test4 = [[ul_wall, u_wall, ur_wall],
         [dl_wall, r_wall, r_wall],
         [dl_wall, d_wall, dr_wall]]

# (X, Y, DIRECTION ->
testGoal4 = [2, 2, "d"]

Start = [4, 0]
Goal = [0, 4]

p1 = [[ulr_wall, ul_wall, u_wall, ur_wall, ulr_wall],
      [l_wall, no_wall, ur_wall, l_wall, dr_wall],
      [l_wall, r_wall, dl_wall, no_wall, ur_wall],
      [l_wall, no_wall, u_wall, no_wall, r_wall],
      [dl_wall, d_wall, d_wall, d_wall, dr_wall]]

p2 = [[udl_wall, ud_wall, ud_wall, u_wall, udr_wall],
      [ulr_wall, udl_wall, u_wall, no_wall, ur_wall],
      [l_wall, ur_wall, l_wall, r_wall, lr_wall],
      [l_wall, no_wall, d_wall, no_wall, dr_wall],
      [dl_wall, d_wall, ud_wall, d_wall, udr_wall]]

p3 = [[ul_wall, u_wall, u_wall, ur_wall, ulr_wall],
      [l_wall, r_wall, dl_wall, no_wall, r_wall],
      [l_wall, no_wall, udr_wall, l_wall, r_wall],
      [l_wall, no_wall, udr_wall, l_wall, r_wall],
      [dlr_wall, dl_wall, ud_wall, d_wall, dr_wall]]

p4 = [[ulr_wall, udl_wall, u_wall, ud_wall, udr_wall],
      [l_wall, ur_wall, dl_wall, u_wall, ur_wall],
      [lr_wall, d_wall, u_wall, r_wall, dlr_wall],
      [l_wall, u_wall, no_wall, no_wall, ur_wall],
      [dl_wall, d_wall, d_wall, d_wall, dr_wall]]

p5 = [[ulr_wall, ul_wall, u_wall, ur_wall, ulr_wall],
      [l_wall, d_wall, no_wall, d_wall, r_wall],
      [lr_wall, ulr_wall, l_wall, u_wall, dr_wall],
      [l_wall, r_wall, l_wall, no_wall, ur_wall],
      [dl_wall, dr_wall, dl_wall, d_wall, dr_wall]]

p6 = [[udl_wall, ud_wall, ud_wall, u_wall, udr_wall],
      [ulr_wall, udl_wall, u_wall, no_wall, ur_wall],
      [l_wall, ur_wall, l_wall, r_wall, lr_wall],
      [l_wall, no_wall, d_wall, no_wall, dr_wall],
      [dl_wall, d_wall, ud_wall, d_wall, udr_wall]]

p7 = [[udl_wall, ud_wall, ud_wall, u_wall, udr_wall],
      [ulr_wall, udl_wall, u_wall, no_wall, ur_wall],
      [l_wall, ur_wall, l_wall, r_wall, lr_wall],
      [l_wall, no_wall, d_wall, no_wall, dr_wall],
      [dl_wall, d_wall, ud_wall, d_wall, udr_wall]]

p8 = [[udl_wall, ud_wall, ud_wall, u_wall, udr_wall],
      [ulr_wall, udl_wall, u_wall, no_wall, ur_wall],
      [l_wall, ur_wall, l_wall, r_wall, lr_wall],
      [l_wall, no_wall, d_wall, no_wall, dr_wall],
      [dl_wall, d_wall, ud_wall, d_wall, udr_wall]]

p9 = [[udl_wall, ud_wall, ud_wall, u_wall, udr_wall],
      [ulr_wall, udl_wall, u_wall, no_wall, ur_wall],
      [l_wall, ur_wall, l_wall, r_wall, lr_wall],
      [l_wall, no_wall, d_wall, no_wall, dr_wall],
      [dl_wall, d_wall, ud_wall, d_wall, udr_wall]]

p10 = [[udl_wall, ud_wall, ud_wall, u_wall, udr_wall],
       [ulr_wall, udl_wall, u_wall, no_wall, ur_wall],
       [l_wall, ur_wall, l_wall, r_wall, lr_wall],
       [l_wall, no_wall, d_wall, no_wall, dr_wall],
       [dl_wall, d_wall, ud_wall, d_wall, udr_wall]]
