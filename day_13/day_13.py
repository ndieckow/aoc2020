from operator import mul
from functools import reduce

data = open("input.txt").read().strip().split('\n')
estimate = int(data[0])
ids = [int(x) if x is not 'x' else x for x in data[1].split(',')]
# Goal 1: Earliest bus to airport
def part1():
    global estimate, ids
    min,min_id = (1000,None)
    for id in ids:
        if id == 'x': continue
        v = 0
        while v < estimate:
            v += id
        #print(v)
        v = v - estimate
        if v < min:
            (min,min_id) = v,id

    print(min,min_id)
    print(min*min_id)

########## Helper Functions ##########

def mod_exp(a, e, m):
    # Compute binary representation of exponent
    be = [int(x) for x in bin(e)[2:]]
    r = 1
    for i in be:
        r = (r*r) % m
        if i is not 0: r = (r*a) % m
    return r

# Modular inverse that only works for prime numbers.
def mod_inv(a, m):
    return mod_exp(a, m-2, m)

######################################

# Apply the CRT.
nums = [x for x in ids if type(x) == int]
ans = 0
for i in range(len(ids)):
    if ids[i] == 'x': continue
    m = ids[i]
    N = 1
    N = reduce(mul, [n for n in nums if n is not m], 1)
    ans += mod_inv(N, m) * N * (-i)

# This solution is negative. Adding integer multiples of the product
# of all moduli gives us other solutions, out of which we find the minimal
# positive one.
N = reduce(mul, nums, 1)
while ans < 0:
    ans += N
print(ans)
