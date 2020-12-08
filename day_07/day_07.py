data = open("input.txt").read().strip().split('\n')

def parse_contents_string(cstr):
    if cstr[-1] == '.': cstr = cstr[:-1]
    temp = cstr.split(', ')
    out = []
    for t in temp:
        if t == "no other bags":
            continue
        count = int(t[0])
        type = ' '.join((t[2:].split(' '))[:-1])
        out.append((type,count))
    return out

cont_dict = {}
for line in data:
    (col_str, cont_str) = line.split(" bags contain ")
    cont_dict[col_str] = parse_contents_string(cont_str)
shiny_dict = {}

def analyze_color(col):
    lst = cont_dict[col]
    for (tp,cnt) in lst:
        if tp == 'shiny gold':
            shiny_dict[col] = True
            return True
        if tp in shiny_dict and shiny_dict[tp]:
            shiny_dict[col] = True
            return True
        if tp not in shiny_dict:
            if analyze_color(tp): shiny_dict[col] = True
    if col not in shiny_dict: shiny_dict[col] = False
    return shiny_dict[col]

def num_of_bags_inside(col):
    count = 0
    contents = cont_dict[col]
    for (type,num) in contents:
        count += num
        count += num * num_of_bags_inside(type)
    return count

count = 0
for col_str in cont_dict:
    analyze_color(col_str)
    if shiny_dict[col_str]:
        count += 1
print(count)
print(num_of_bags_inside("shiny gold"))
