import re
nec_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
#opt_fields = ['cid']
data = []
with open("input.txt") as f:
    inp = f.read().split('\n\n')
    data = [re.split(' |\n', line) for line in inp]
    data = [list(map(lambda x: tuple(x.split(':')), d)) for d in data]

def is_valid(dp):
    if len(dp) == 1: return True
    t = dp[0]
    v = dp[1]
    bl = True
    if t == 'byr':
        bl = len(v) == 4 and int(v) >= 1920 and int(v) <= 2002
    elif t == 'iyr':
        bl = len(v) == 4 and int(v) >= 2010 and int(v) <= 2020
    elif t == 'eyr':
        bl = len(v) == 4 and int(v) >= 2020 and int(v) <= 2030
    elif t == 'hgt':
        md = v[-2:]
        if md == 'cm':
            bl = int(v[:-2]) >= 150 and int(v[:-2]) <= 193
        elif md == 'in':
            bl = int(v[:-2]) >= 59 and int(v[:-2]) <= 76
        else:
            bl = False
    elif t == 'hcl':
        bl = v[:1] == '#' and len(v) == 7 and all(list(map(lambda x: (ord(x) >= 48 and ord(x) <= 57) or (ord(x) >= 97 and ord(x) <= 102), v[1:])))
    elif t == 'ecl':
        bl = v in ['amb','blu','brn','gry','grn','hzl','oth']
    elif t == 'pid':
        bl = len(v) == 9
    return bl

count = 0
for passport in data:
    names = [field[0] for field in passport]
    vals = list(map(is_valid, [field for field in passport]))
    if set(nec_fields) <= set(names) and all(vals): count += 1
print(count)
