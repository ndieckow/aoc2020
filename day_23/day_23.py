from dll import *

input = "135468729"
labels = CyclicDoublyLinkedList()
dict = {}
for n in input:
    dict[int(n)] = labels.append(int(n))
for i in range(10,10**6+1):
    dict[i] = labels.append(i)
MOD = labels.length

cur = labels.start_node
for i in range(10**7+1):
    if i % 100000 == 0:
        print(i)

    picked = [cur.succ, cur.succ.succ, cur.succ.succ.succ]
    #print(picked)
    for p in picked:
        labels.remove(p)
    picked = [p.data for p in picked]

    dest_val = (cur.data-2)%MOD + 1
    while dest_val in picked:
        dest_val = (dest_val-2)%MOD + 1
    dest = dict[dest_val]

    prev = dest
    for i in range(3):
        prev = labels.insert_after(prev, picked[i])
        dict[picked[i]] = prev # update index

    cur = cur.succ
    #print(lab)
want = dict[1]
print(want.succ.data*want.succ.succ.data)
