import sys

input = []
with open('input.txt') as f:
    lines = f.readlines();
    input = list(map(int, lines))

# first, sort
input = sorted(input)

def find_numbers(ls):
    n = [0,0,0]
    for i in ls:
        for k in ls:
            for l in ls:
                sum = i + k + l
                if sum > 2020: break
                if i + k + l == 2020:
                    n = [i,k,l]
                    return n
n = find_numbers(input)
print("Numbers:", n[0], n[1], n[2])
print("Product:", n[0]*n[1]*n[2])
