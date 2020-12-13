from copy import deepcopy
from time import time

data = open("input.txt").read().strip().split('\n')
data = list(map(list, data))
H = len(data)
W = len(data[0])

prev = data
curr = deepcopy(data)

def seat_occupied(x,y):
    global H,W,prev
    if not (0<=y<H) or not (0<=x<W): return False
    return prev[y][x] == '#'

def seat_type(x,y):
    global H,W,prev
    if not (0<=y<H) or not (0<=x<W): return 'x'
    return prev[y][x]

def occupied_around(x,y):
    ct = 0
    for i in [-1,0,1]:
        for k in [-1,0,1]:
            if i == k == 0: continue
            if seat_occupied(x-i,y-k):
                ct += 1
    return ct

sub_time = 0

def vis_occ_around(x,y):
    global W,H,prev
    ct = 0
    for i in [-1,0,1]:
        for k in [-1,0,1]:
            if i == k == 0: continue
            yy = y+i
            xx = x+k
            while 0<=yy<H and 0<=xx<W and prev[yy][xx]=='.':
                yy += i
                xx += k
            if not (0<=yy<H) or not (0<=xx<W):
                continue
            st = prev[yy][xx]
            if st == '#':
                ct += 1
    return ct

start_time = time()

change = True

while change:
    change = False
    prev = deepcopy(curr)
    for y in range(H):
        for x in range(W):
            s = prev[y][x]
            oa = vis_occ_around(x,y)
            if s == 'L' and oa == 0:
                curr[y][x] = '#'
                change = True
            elif s == '#' and oa >= 5:
                curr[y][x] = 'L'
                change = True

# count seats
ct = 0
for row in curr:
    for s in row:
        if s == '#': ct += 1
print(ct)

print("total time:", time() - start_time, "sub time:", sub_time)
