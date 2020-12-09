data = open("input.txt").read().strip().split('\n')
data = list(map(int, data))

preamble = data[:25]

l25 = preamble.copy()
for n in data[26:]:
    prop = False
    for m in l25:
        for k in l25:
            if m+k == n:
                prop = True
                break
        if prop == True: break
    if prop == False:
        print("not fulfilled for", n) # part 1
        magic = n
    l25 = l25[1:]
    l25.append(n)

mi = 0
ma = 0
acc = 0
for k in range(len(data)):
    if data[k] == magic: break
    acc += data[k]
    while acc > magic:
        acc -= data[mi]
        mi += 1
    if acc == magic:
        ma = k
        break

r = data[mi:(ma+1)]
print(min(r) + max(r)) # part 2
