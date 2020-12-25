cards = open("test.txt").read().strip().split('\n\n')
cards = [[int(x) for x in cc.split('\n')[1:]] for cc in cards]

# returns winner of the round
def round():
    d = [c.pop(0) for c in cards]
    if d[0] > d[1]:
        cards[0].extend(d)
        return 1
    else:
        cards[1].extend(d[::-1])
        return 2

rc = 0
while all(cards):
    rc += 1
    round()
score = 0
for c in cards:
    if not c: continue
    score = sum([(i+1)*c[len(c)-(i+1)] for i in range(len(c))])
print(score)
