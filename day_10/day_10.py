data = open("input.txt").read().strip().split('\n')
data = list(map(int, data))

# variable naming conventions
# p, q, r, s, t     for temporary values
# i, j, k, l, m, n  for counters

data.sort()

# O(n)
def part1():
    diff1 = min(data)
    diff3 = 1
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if diff == 1: diff1 += 1
        elif diff == 3: diff3 += 1
    print(diff1*diff3)

# O(n^2)
def part2():
    dp = [None] * len(data)
    for i in range(len(data)):
        v = data[i]
        dp[i] = 1 if data[i] <= 3 else 0
        for k in range(i):
            if v-data[k] > 3: continue
            dp[i] += dp[k]
    print(dp)

part2()
