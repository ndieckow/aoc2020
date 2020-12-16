data = open("input.txt").read().strip().split('\n\n')

rules = data[0].split('\n')
mytick = data[1].split('\n')
nearby = [line.split(',') for line in data[2].split('\n')[1:]]

valid_nums = {}
for r in rules:
    r = r.split(': ')
    ranges = r[1].split(' or ')
    r1 = [int(x) for x in ranges[0].split('-')]
    r2 = [int(x) for x in ranges[1].split('-')]
    valid_nums[r[0]] = list(range(r1[0], r1[1]+1)) + list(range(r2[0], r2[1]+1))

valid = [item for sublist in [valid_nums[key] for key in valid_nums] for item in sublist]
ans = 0
invalid = []
for i,tick in enumerate(nearby):
    for num in tick:
        num = int(num)
        if num not in valid:
            ans += num
            invalid.append(i)
print("Part 1:",ans)

assign = {}
while len(assign) < len(rules):
    for i in range(len(nearby[0])):
        valid_fields = [key for key in valid_nums if key not in assign]
        for j in range(len(nearby)):
            if j in invalid:
                continue
            val = int(nearby[j][i])
            for f in valid_fields:
                if val not in valid_nums[f]:
                    valid_fields.remove(f)
        if len(valid_fields) == 1:
            assign[valid_fields[0]] = i
    #print(assign)

prod = 1
my_ticket = [int(x) for x in mytick[1].split(',')]
for key in assign:
    if key.startswith('departure'):
        prod *= my_ticket[assign[key]]
print("Part 2:",prod)
