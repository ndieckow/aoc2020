from itertools import takewhile

input = open("input.txt").read().strip()
data = input.split('\n')
newdata = []
ingredients = set()
allergens = set()
for line in data:
    p1 = ''
    p2 = ''
    b = False
    for c in line:
        if c == '(':
            b = True
        if b: p2 += c
        else: p1 += c
    ing = set(p1.split())
    al = set(p2[10:-1].split(', '))
    newdata.append((ing, al))
    ingredients.update(ing)
    allergens.update(al)
data = newdata
####################################
dict = {}
ingun = set()
for al in allergens:
    ings = ingredients
    for d in data:
        if al in d[1]:
            ings = ings.intersection(d[0])
    dict[al] = ings
    ingun = ingun.union(ings)

while not all([isinstance(x,str) for x in dict.values()]):
    for al in dict:
        if len(dict[al]) == 1:
            (el,) = dict[al]
            dict[al] = el
            # remove from all other sets
            for o in dict:
                if o != al and el in dict[o]:
                    dict[o].remove(el)

wanted = ingredients.difference(ingun)
lst = input.replace('\n',' ').split()
acc = 0
for ing in wanted:
    cnt = len([x for x in lst if x == ing])
    acc += cnt
print(acc) # part 1

ans2 = sorted([(k,v) for k,v in dict.items()])
print(','.join([x[1] for x in ans2])) # part 2
