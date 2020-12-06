data = open("input.txt").read().strip().split('\n\n')
data = [d.split('\n') for d in data]

# Part 1
def part_1():
    sum = 0
    for grp in data:
        for l in range(ord('a'), ord('z')+1):
            if any(map(lambda x: chr(l) in x, grp)): sum += 1
    return sum

# Part 2
def part_2():
    sum = 0
    for grp in data:
        for l in grp[0]:
            if all(map(lambda x: l in x, grp)): sum += 1
    return sum

print('1', part_1())
print('2', part_2())
