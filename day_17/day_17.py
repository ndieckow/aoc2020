import re
from itertools import product

data = open("input.txt").read().strip().split('\n')
cube = {}

def print_cube():
    for z in range(min([a[2] for a in cube.keys()]), max([a[2] for a in cube.keys()])+1):
        print("z=%d" % z)
        for y in range(min([a[1] for a in cube.keys()]), max([a[1] for a in cube.keys()])+1):
            str = ''
            for x in range(min([a[0] for a in cube.keys()]), max([a[0] for a in cube.keys()])+1):
                v = cube[(x,y,z)] if (x,y,z) in cube else '.'
                str += v
            print(str)
        print(" ")

# initialization
for y,line in enumerate(data):
    for x,cell in enumerate(line):
        for p in product([-1,0,1], repeat=4):
            if p == (0,0,0,0):
                cube[(x,y,0,0)] = cell
            else:
                q = (x+p[0],y+p[1],p[2],p[3])
                if q not in cube:
                    cube[q] = '.'

# 6 cycles
for _ in range(6):
    newcube = cube.copy()
    for key in cube:
        active = cube[key] == '#'
        act_cnt = 0
        for p in product([-1,0,1], repeat=4):
            if p == (0,0,0,0): continue
            newkey = (key[0]+p[0],key[1]+p[1],key[2]+p[2],key[3]+p[3])
            if newkey in cube:
                if cube[newkey] == '#': act_cnt += 1
            else:
                newcube[newkey] = '.'
        if active and not 2<=act_cnt<=3:
            newcube[key] = '.'
        elif not active and act_cnt == 3:
            newcube[key] = '#'
    cube = newcube


ans = 0
for c in cube:
    if cube[c] == '#': ans += 1

print(ans)
