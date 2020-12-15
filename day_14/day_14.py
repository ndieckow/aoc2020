from itertools import product

data = open("input.txt").read().strip().split('\n')

mem = [0] * 100000
mask = ""

def part1():
    changed = set()
    for line in data:
        a = line.split(' = ')
        if a[0] == 'mask':
            mask = a[1]
        else:
            addr = int(a[0][4:-1])
            val = int(a[1])
            zipped = zip(bin(val)[2:].zfill(36), mask)
            bitstring = ''.join([z[0] if z[1] == 'X' else z[1] for z in zipped])
            mem[addr] = int(bitstring, 2)
            changed.add(addr)

    sum_ = 0
    for addr in changed:
        sum_ += mem[addr]
    print(sum_)

def part2():
    def eval_mask(x,m):
        if m == 'X':
            return m
        elif m == '0':
            return x
        elif m == '1':
            return '1'

    mem = {}

    for line in data:
        a = line.split(' = ')
        if a[0] == 'mask':
            mask = a[1]
        else:
            addr = int(a[0][4:-1])
            val = int(a[1])
            zipped = zip(bin(addr)[2:].zfill(36), mask)
            bitstring = ''.join([eval_mask(*z) for z in zipped])

            Xcount = sum([1 for x in bitstring if x == 'X'])
            for p in product(['0','1'],repeat=Xcount):
                new_addr = list(bitstring)
                i = 0
                for k in range(len(new_addr)):
                    v = new_addr[k]
                    if v == 'X':
                        new_addr[k] = p[i]
                        i += 1
                new_addr = int(''.join(new_addr), 2)
                mem[new_addr] = val

    sum_ = 0
    for key in mem:
        sum_ += mem[key]
    print(sum_)

part2()
