data = open("input.txt").read().strip().split('\n')

ops = {
    "nop" : 0,
    "acc" : 1,
    "jmp" : 2
}

code = []

for line in data:
    sp = line.split(' ')
    code.append([ops[sp[0]], int(sp[1])])

accum = 0
ip = 0

def exec_op(instr):
    global accum, ip
    op = instr[0]
    val = instr[1]
    if op == 0:
        ip += 1
    elif op == 1:
        accum += val
        ip += 1
    elif op == 2:
        ip += val
    return

# changed instruction
ci = 0

def run_prog(code):
    global accum, ip, ci
    run_vals = set()
    thresh = 1000
    cnt = 0
    #print(ip)
    while True:
        if ip >= len(code):
            print("terminated", accum)
            break
        if ip in run_vals:
            break
        run_vals.add(ip)
        exec_op(code[ip])

tried = []
# change code
for i in range(len(code)):
    accum = 0
    ip = 0
    op = code[i][0]
    if op == 1:
        continue # no acc
    elif op == 0:
        code[i][0] = 2
        run_prog(code)
        code[i][0] = 0 # change it back
    elif op == 2:
        code[i][0] = 0
        run_prog(code)
        code[i][0] = 2 # change it back
