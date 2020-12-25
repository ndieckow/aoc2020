# geohot
# https://www.youtube.com/watch?v=OxDp11u-GUo

data = open("input.txt").read().strip().split('\n\n')
rules = data[0].split('\n')
msgs = data[1].split('\n')

dict = {}
for r in rules:
    num, vals = r.split(": ")
    if int(num) == 8:
        vals = "42 | 42 8"
    if int(num) == 11:
        vals = "42 31 | 42 11 31"
    dict[int(num)] = vals

# Does string x satisfy rule r?
def check_str(x, r):
    rule = dict[r]
    if rule[0] == '"':
        rule = rule.strip('"')
        if x.startswith(rule):
            return [len(rule)]
        else:
            return []

    bret = []
    for opt in rule.split(' | '):
        acc = [0]
        for rn in opt.split():
            new_acc = []
            rn = int(rn)
            for ac in acc:
                ret = check_str(x[ac:], rn)
                for re in ret:
                    new_acc.append(re + ac)
            acc = new_acc
        bret += acc
    return bret

acc = 0
for x in msgs:
    acc += len(x) in check_str(x, 0)
print(acc)
