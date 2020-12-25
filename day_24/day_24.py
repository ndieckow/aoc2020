data = open("input.txt").read().strip().split('\n')

# use x,y coords
grid = {}
black = set()

# 0 = black, 1 = white
def flip_tile(t,coll=black):
    if t in coll:
        coll.remove(t)
    else:
        coll.add(t)

# north-east: same coords
def get_neighbor(t, dir):
    if dir == 'e':
        return (t[0]+2, t[1])
    elif dir == 'se':
        return (t[0]+1, t[1]-1)
    elif dir == 'sw':
        return (t[0]-1, t[1]-1)
    elif dir == 'w':
        return (t[0]-2, t[1])
    elif dir == 'nw':
        return (t[0]-1, t[1]+1)
    elif dir == 'ne':
        return (t[0]+1, t[1]+1)

ref_tile = (0,0)
valid_dirs = ['e', 'se', 'sw', 'w', 'nw', 'ne']
for line in data:
    dirs = []
    st,en = (0,1)
    while en < len(line)+1:
        while line[st:en] not in valid_dirs:
            en += 1
        dirs.append(line[st:en])
        st = en
        en += 1
    ####
    cur = ref_tile
    for dir in dirs:
        cur = get_neighbor(cur, dir)
    flip_tile(cur)

# count black tiles
print("Part 1", len(black))

###########################

for _ in range(100):
    # first, add all neighbours not yet in the grid
    SET = set()
    for t in black:
        SET.add(t)
        for dir in valid_dirs:
            SET.add(get_neighbor(t,dir))
    #for n in add_first:
    #    grid[n] = 1

    #newgrid = grid.copy()
    newblack = black.copy()
    # now, play the game
    for t in SET:
        cnt_black = 0
        for dir in valid_dirs:
            if get_neighbor(t,dir) in black:
                cnt_black += 1
        if t in black:
            if cnt_black == 0 or cnt_black > 2:
                flip_tile(t,newblack)
        else:
            if cnt_black == 2:
                flip_tile(t,newblack)
    black = newblack

# 1: 10.6 s (with floating point arithmetic)
# 2: 8.2 s (with integer arithmetic)
# 3: 1.9 s (with a set instead of a dict, plus (still) integer arithmetic)

print("Part 2", len(black))
