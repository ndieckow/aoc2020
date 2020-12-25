data = open("input.txt").read().strip().split('\n\n')
tiles = {}
for tile in data:
    lines = tile.split('\n')
    id = int(lines[0][5:-1])
    tiles[id] = lines[1:]
# top, bottom, left, right
joined = {tid : [None]*4 for tid in tiles}

def print_tile(tid):
    tile = tiles[tid]
    for line in tile:
        print(line)
    print("="*10)

# 0=top, 1=bottom, 2=left, 3=right
def get_boundary(tid,side=None):
    tile = tiles[tid]
    dict = {
        0: tile[0],
        1: tile[-1],
        2: ''.join([s[0] for s in tile]),
        3: ''.join([s[-1] for s in tile])
    }
    if side == None: return dict
    else: return dict.get(side)

def flip(tid,axis):
    tile = tiles[tid]
    if axis == 0: # horizontal flip
        tiles[tid] = list(reversed(tile))
        top = joined[tid][0]
        joined[tid][0] = joined[tid][1]
        joined[tid][1] = top
    elif axis == 1: # vertical flip
        tiles[tid] = [''.join(reversed(s)) for s in tile]
        left = joined[tid][2]
        joined[tid][2] = joined[tid][3]
        joined[tid][3] = left

def rotate_ccw(tid, times):
    times = times % 4
    tile = tiles[tid]
    if times == 0: return
    elif times == 2:
        flip(tid,0)
        flip(tid,1)
        return
    elif times == 1:
        newtile = [''.join([s[i] for s in tile]) for i in range(len(tile)-1,-1,-1)]
        tiles[tid] = newtile
        # neighbours
        return
    elif times == 3:
        newtile = [''.join(reversed([s[i] for s in tile])) for i in range(len(tile))]
        tiles[tid] = newtile
        # neighbours
        return

def opposite(i):
    return {
        0: 1,
        1: 0,
        2: 3,
        3: 2
    }.get(i)

# returns on which sides the boundaries match, and how the SECOND tile needs to be oriented
# --> tuple of two tuples
def match(t1, t2):
    b1 = get_boundary(t1)
    b2 = get_boundary(t2)
    #print(b1,b2)
    sides = None
    rev = False
    found = False
    for i in range(4):
        if found: break
        #if joined[t1][i] is not None: continue
        for j in range(4):
            #if joined[t2][j] is not None: continue
            if b1[i] == b2[j]:
                sides = (i,j)
                rev = False
                found = True
                break
            elif b1[i] == ''.join(reversed(b2[j])):
                sides = (i,j)
                rev = True
                found = True
                break
    return (sides, rev)

for t1 in tiles:
    for t2 in tiles:
        #if t2 == t1 or any(joined[t2]): continue
        if t2 == t1: continue
        ans = match(t1, t2)
        if ans[0] == None or joined[t1][ans[0][0]]:
            continue
        if ans[0][0] == ans[0][1]:
            if 0<=ans[0][0]<=1:
                flip(t2,1)
                if ans[1]:
                    flip(t2,0)
            else:
                flip(t2,0)
                if ans[1]:
                    flip(t2,1)
        elif 0<=ans[0][0]<=1 and 0<=ans[0][1]<=1: # not equal
            if ans[1]: flip(t2,1)
        elif 2<=ans[0][0]<=3 and 2<=ans[0][1]<=3: # not equal
            if ans[1]: flip(t2,0)
        else: # rotation necessary
            if ans[0][0] == 0:
                if ans[0][1] == 2:
                    rotate_ccw(t2,1)
                    if ans[1]: flip(t2,1)
                elif ans[0][1] == 3:
                    rotate_ccw(t2,3)
                    if not ans[1]: flip(t2,1)
            elif ans[0][0] == 1:
                if ans[0][1] == 2:
                    rotate_ccw(t2,3)
                    if not ans[1]: flip(t2,1)
                elif ans[0][1] == 3:
                    rotate_ccw(t2,1)
                    if ans[1]: flip(t2,1)
            elif ans[0][0] == 2:
                if ans[0][1] == 0:
                    rotate_ccw(t2,3)
                    if ans[1]: flip(t2,0)
                elif ans[0][1] == 1:
                    rotate_ccw(t2,1)
                    if ans[1]: flip(t2,0)
            elif ans[0][0] == 3:
                if ans[0][1] == 0:
                    rotate_ccw(t2,1)
                    if not ans[1]: flip(t2,0)
                elif ans[0][1] == 1:
                    rotate_ccw(t2,3)
                    if ans[1]: flip(t2,0)
        # update joined
        if t1 == 1979:
            print("t1 yo",t2)
        if t2 == 1979:
            print("t2 yo",t1)
        joined[t1][ans[0][0]] = t2
        joined[t2][opposite(ans[0][0])] = t1
print(joined)

prod = 1
for tile in joined:
    cnt = sum([0 if not val else 1 for val in joined[tile]])
    #print(tile,cnt)
    if cnt <= 2:
        print(tile)
        prod *= tile
print(prod)
