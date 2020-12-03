inp = []
with open("input.txt") as  f:
    inp = f.read().splitlines()

height = len(inp)
width = len(inp[0])

def is_tree_at(x,y):
    return inp[y][x % width] == '#'

# slope
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
# current position
(x,y) = (0,0)

prod = 1
for (xd,yd) in slopes:
    tree_cnt = 0
    # start moving
    while y < height:
        if is_tree_at(x,y): tree_cnt += 1
        (x,y) = (x + xd, y + yd)
    prod *= tree_cnt
    # reset position
    (x,y) = (0,0)

print(prod)
