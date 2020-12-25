from copy import deepcopy

data = open("input.txt").read().strip().split('\n\n')
data = [[int(x) for x in cc.split('\n')[1:]] for cc in data]

def new_game(cards):
    states = []
    # returns winner of the round
    def round():
        round_win = 0
        for s in states:
            if cards[0] == s[0] and cards[1] == s[1]:
                return 99
        d = [c.pop(0) for c in cards]
        if all([len(cards[i]) >= d[i] for i in range(2)]):
            round_win = new_game([cards[i][:d[i]].copy() for i in range(2)])
        else:
            round_win = 1 if d[0] > d[1] else 2
        if round_win == 1:
            cards[0].extend(d)
        else:
            cards[1].extend(d[::-1])

        return round_win

    rc = 0
    winner = 0
    while not winner:
    #for _ in range(2):
        #print(winner)
        rc += 1
        cur_state = deepcopy(cards)
        val = round()
        if val == 99:
            winner = 1
        if not cards[1]:
            winner = 1
        if not cards[0]:
            winner = 2
        states.append(cur_state)
    return winner

new_game(data)
score = 0
for c in data:
    if not c: continue
    score = sum([(i+1)*c[len(c)-(i+1)] for i in range(len(c))])
print(score)
