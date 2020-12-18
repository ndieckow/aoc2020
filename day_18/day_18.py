from itertools import takewhile

data = open("input.txt").read().strip().split('\n')

# input: string
# output: number
def parse(line):
    # simplify expression
    newline = line
    for i,c in enumerate(line):
        if c == '(':
            depth = 0
            k = i+1
            while line[k] is not ')' or depth > 0:
                if line[k] == '(':
                    depth += 1
                elif line[k] == ')':
                    depth -= 1
                k += 1
            subexpr = line[i+1:k]
            val = parse(subexpr)
            newline = newline.replace('(' + subexpr + ')', str(val))
    # evaluate simple expression
    newline = [x if x == '+' or x == '*' else int(x) for x in newline.split()]
    #return eval_simple_part1(newline)
    return eval_simple_part2(newline)

def eval_simple_part1(lst):
    print(lst)
    while len(lst) > 1:
        op = lst[1]
        if op == '+':
            v = lst[0] + lst[2]
        elif op == '*':
            v = lst[0] * lst[2]
        lst[:3] = [v]
    return lst[0]

def eval_simple_part2(lst):
    # evaluate additions first
    while '+' in lst:
        for i,el in enumerate(lst):
            if el == '+':
                lst[i-1:i+2] = [lst[i-1] + lst[i+1]]
                break
    # evaluate multiplications left-to-right
    while len(lst) > 1:
        if lst[1] == '*':
            v = lst[0] * lst[2]
        lst[:3] = [v]
    return lst[0]

acc = 0
for line in data:
    val = parse(line)
    acc += val
print(acc)
