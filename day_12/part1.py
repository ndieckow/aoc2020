from math import radians,pi,sin,cos

data = open("input.txt").read().strip().split('\n')

xpos = 0
ypos = 0
face = 0

for line in data:
    A = line[:1] # action
    val = int(line[1:])
    if A == 'N':
        ypos += val
    elif A == 'S':
        ypos -= val
    elif A == 'E':
        xpos += val
    elif A == 'W':
        xpos -= val
    elif A == 'L':
        face += radians(val)
        while face < 0:
            face += 2*pi
    elif A == 'R':
        face -= radians(val)
        while face < 0:
            face += 2*pi
    elif A == 'F':
        xp = round(cos(face))
        yp = round(sin(face))
        #print(face,cos(face),sin(face))
        xpos += xp*val
        ypos += yp*val

# Manhattan distance
dist = abs(xpos) + abs(ypos)
print(dist)
