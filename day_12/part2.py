from math import radians,pi,sin,cos

data = open("input.txt").read().strip().split('\n')

xpos = 0
ypos = 0
# waypoint
wp_x = 10
wp_y = 1

for line in data:
    A = line[:1] # action
    val = int(line[1:])
    if A == 'N':
        wp_y += val
    elif A == 'S':
        wp_y -= val
    elif A == 'E':
        wp_x += val
    elif A == 'W':
        wp_x -= val
    elif A == 'L' or A == 'R':
        rad = radians(val) if A == 'L' else -radians(val) + 2*pi
        c = round(cos(rad))
        s = round(sin(rad))
        tx = wp_x*c - wp_y*s
        ty = wp_x*s + wp_y*c
        (wp_x,wp_y) = tx,ty
    elif A == 'F':
        while val > 0:
            xpos += wp_x
            ypos += wp_y
            val -= 1

# Manhattan distance
dist = abs(xpos) + abs(ypos)
print(dist)
