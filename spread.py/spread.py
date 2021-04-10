import os
from time import sleep
from random import randint

h_ = 10
w_ = 10

mat = [[0 for _ in range(w_)] for _ in range(h_)]

def prmat(m):
    for h in m:
        for w in h:
            if w:
                print("■", end=" ")
            else:
                print("  ", end="")
        print()

def addrndm(m):
    rdr = randint(0, 3)
    rd = [1 if i == rdr else 0 for i in range(0, 4)]
    hn = 0

    for h in m:
        for w in h:
            if w:
                dry = randint(0, 1)
                drx = randint(2, 3)

                dpy = rd[dry]
                dpx = rd[drx]

                x = w+dpx
                y = hn+dpy

                try:
                    m[y][x] = 1
                except IndexError:
                    pass
        hn += 1
    return m

rpx = randint(0, h_-1)
rpy = randint(0, w_-1)

mat[rpy][rpx] = 1


while True:
    os.system("clear")
    mat = addrndm(mat)
    prmat(mat)
    sleep(0.01)