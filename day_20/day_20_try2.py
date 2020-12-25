import math

# This code is a real mess.

data = open("input.txt").read().strip().split('\n\n')
tiles = {}
for tile in data:
    lines = tile.split('\n')
    id = int(lines[0][5:-1])
    tiles[id] = lines[1:]

def print_tile(tile):
    for line in tile:
        print(''.join(line))
    print("="*10)

def flip(tile, axis):
    if axis == 0: # horizontal flip
        tiles[tid] = list(reversed(tile))
    elif axis == 1: # vertical flip
        tiles[tid] = [''.join(reversed(s)) for s in tile]

# ccw
def rotate90(tile):
    return list(map("".join, zip(*tile)))[::-1]

def all_transforms(tile):
    tiles = []
    tiles.append(tile)
    for _ in range(3):
        tiles.append(rotate90(tiles[-1]))
    tiles.append(tile[::-1])
    for _ in range(3):
        tiles.append(rotate90(tiles[-1]))
    return tiles

# 0=top, 1=bottom, 2=left, 3=right
def get_boundary(tile,side):
    return {
        0: tile[0],
        1: tile[-1],
        2: ''.join([s[0] for s in tile]),
        3: ''.join([s[-1] for s in tile])
    }.get(side)

grid = {}
grid_ids = {}
queue = list(tiles).copy()
tid0 = queue.pop(0)
grid[(0,0)] = tiles[tid0]
grid_ids[(0,0)] = tid0
while queue:
    tid = queue.pop(0)
    tile = tiles[tid]
    added = False
    for x,y in grid:
        #print(x,y)
        tile2 = grid[(x,y)]
        for xd,yd in [(1,0),(0,1),(-1,0),(0,-1)]:
            nc = (x+xd,y+yd)
            if nc in grid:
                continue
            for trans in all_transforms(tile):
                if ((xd,yd) == (1,0) and get_boundary(tile2,3) == get_boundary(trans,2)) \
                or ((xd,yd) == (0,1) and get_boundary(tile2,0) == get_boundary(trans,1)) \
                or ((xd,yd) == (-1,0) and get_boundary(tile2,2) == get_boundary(trans,3)) \
                or ((xd,yd) == (0,-1) and get_boundary(tile2,1) == get_boundary(trans,0)):
                    added = True
                    grid[nc] = trans
                    grid_ids[nc] = tid
                    #for g in grid:
                        #print(grid_ids[g], g)
                        #print_tile(grid[g])
                    break
            if added:
                break
        if added: break
    if not added:
        queue.append(tid)
minx = min([x for x,y in grid_ids])
maxx = max([x for x,y in grid_ids])
miny = min([y for x,y in grid_ids])
maxy = max([y for x,y in grid_ids])
def part1():
    ans = grid_ids[(minx,miny)]*grid_ids[(minx,maxy)]*grid_ids[(maxx,miny)]*grid_ids[(maxx,maxy)]
    print(ans)
#################################
def remove_boundary(tile):
    return [row[1:-1] for row in tile[1:-1]]

SIZE = int(math.sqrt(len(tiles)))
IMG = [[0 for _ in range(SIZE*8)] for _ in range(SIZE*8)]

lel = sorted([(k,v) for k,v in grid.items()],key=lambda x: (-x[0][1],x[0][0]))
#print(lel)
off_x,off_y = -minx,-miny
for (x,y),tile in lel:
    rem = remove_boundary(tile)
    #print(x,y)
    #print_tile(rem)
    for i in range(8):
        IMG[-(y+off_y+1)*8+i][(x+off_x)*8:(x+off_x)*8+8] = rem[i]
print_tile(IMG)

# find those fucking sea monsters
pat = ['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   '] # 15 hashes
print_tile(pat)
# check each transformation

tcnt = 0
max = 0
for trans in all_transforms(IMG):
    tcnt += 1
    smc = 0
    # check each pixel as starting point
    for r in range(len(IMG)):
        if r+len(pat)-1 >= len(IMG): continue
        for c in range(len(IMG[0])):
            if c+len(pat[0])-1 >= len(IMG[0]): continue
            invalid = False
            for ro in range(len(pat)):
                if invalid: break
                for co in range(len(pat[0])):
                    #if tcnt==4: print("kajhong", tcnt,r,c,pat[ro][co],)
                    if pat[ro][co] == '#':
                        if trans[r+ro][c+co] != '#':
                            invalid = True
                            break
            if not invalid:
                smc += 1
    if smc > 0:
        max = smc
        break

# Number of hashes in the image
no_hashes = sum([row.count('#') for row in IMG])
print(no_hashes - max*15)
