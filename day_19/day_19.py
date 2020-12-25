from itertools import product

data = open("input.txt").read().strip().split('\n\n')
rules = data[0].split('\n')
msgs = data[1].split('\n')

dict = {}

# modified input:
# 8: 42         --> 8: 74 123 | 65 79
# 95: 65 | 74   --> 95: "b" | "a"

for rule in rules:
    a = rule.split(": ")
    num = int(a[0])
    b = a[1].split(' | ')

    for c in b:
        #if len(c.split()) == 1: print(rule)
        if '"' in c:
            v = c.replace('"','')
            if v in dict:
                dict[v].append(num)
            else:
                dict[v] = [num]
        else:
            lst = tuple([int(x) for x in c.split()])
            if lst in dict:
                dict[lst].append(num)
            else:
                dict[lst] = [num]

cnt = 0
for m in msgs:
    T = [None]*len(m)
    for i in range(len(m)):
        T[i] = [None]*len(m)
        T[0][i] = dict[m[i]]
    for j in range(1,len(m)):
        for i in range(len(m)-j):
            T[j][i] = []
            for k in range(j):
                #print("prod",list(product(T[k][i], T[j-k-1][i+k+1])))
                for (a,b) in product(T[k][i], T[j-k-1][i+k+1]):
                    if (a,b) in dict:
                        T[j][i].extend(dict[(a,b)])
    #print(T)
    if 0 in T[-1][0]:
        cnt += 1
        #return True

print(cnt)
