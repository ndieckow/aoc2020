def parse_line(line):
    (rule, pwd) = line.split(": ")
    pwd = pwd[:-1]
    (range, letter) = rule.split()
    (val1, val2) = list(map(int, range.split("-")))
    return (letter, val1, val2, pwd)

# Part 1
def check_rule1(letter, val1, val2, pwd):
    cnt = 0
    for c in pwd:
        if c == letter: cnt += 1
    if cnt >= val1 and cnt <= val2: return True
    return False

# Part 2
def check_rule2(letter, val1, val2, pwd):
    return (pwd[val1 - 1] == letter) ^ (pwd[val2 - 1] == letter)

inp = []
with open("input.txt") as f:
    inp = list(map(parse_line, f.readlines()))

cnt = 0
for i in inp:
    if check_rule2(*i): cnt += 1

print(cnt)
